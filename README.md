Got it 👍 — here’s a developer-focused Confluence page with minimal theory and clear steps to execute + get extracted SQL + push to GitHub.

⸻

📘 DDL/DML Extraction – Developer Quick Guide

⸻

🔹 1. What You Need

Before running:

* Access to Snowflake
* Permission to execute procedure
* Python installed (for file generation)
* Git access to repo

⸻

🔹 2. Step 1: Provide Sub Area (SA)

You only need to decide which SA you want to extract

✔ Single SA

CALL POPULATE_DML_DDL_EXTRACT_MERGED('CUSTOMER', ...);

✔ Multiple SA

CALL POPULATE_DML_DDL_EXTRACT_MERGED('CUSTOMER,PRODUCT', ...);

👉 Only these SAs will be extracted (nothing extra)

⸻

🔹 3. Step 2: Execute Stored Procedure

Run in Snowflake:

CALL POPULATE_DML_DDL_EXTRACT_MERGED(
   'CUSTOMER,PRODUCT',
   '<SRC_DB>',
   '<SRC_SCHEMA>',
   '<TGT_DB>',
   '<TGT_SCHEMA>',
   '<EXTRACT_DB>',
   '<EXTRACT_SCHEMA>',
   'DML_DDL_CONFIG_DTLS'
);

⸻

🔹 4. Step 3: Verify Extracted Data

Check output table:

SELECT *
FROM DML_DDL_EXTRACT_DTLS
WHERE SA_INPUT IN ('CUSTOMER','PRODUCT');

⸻

🔸 What You Will See

SA	OBJECT_NAME	TYPE	QUERY
CUSTOMER	ETL_PARAM_DTLS	DML	INSERT SQL
CUSTOMER	ETL_INBOUND_DTLS	DML	INSERT SQL

⸻

👉 Each row = one SQL file content

⸻

🔹 5. Step 4: Generate SQL Files (Python)

Run script:

python generate_sql_files.py

⸻

🔸 What It Does

* Reads extract table
* Creates .sql files
* Formats SQL cleanly

⸻

🔸 Output Location

snowflake/
 ├── dml/
 │    ├── customer_etl_param_dtls.sql
 │    ├── customer_etl_inbound_dtls.sql

⸻

🔹 6. Step 5: Push to GitHub

If running manually:

git add .
git commit -m "DML extraction for CUSTOMER, PRODUCT"
git push

⸻

🔹 7. GitHub Actions (Auto Mode)

You can skip manual steps and just trigger pipeline 👇

⸻

🔸 How to Run

1. Go to GitHub repo
2. Click Actions
3. Select workflow: DDL DML Extraction
4. Click Run Workflow
5. Enter SA:

CUSTOMER,PRODUCT

⸻

🔸 What Happens Automatically

Trigger
 ↓
Stored Procedure Runs
 ↓
Extract Table Updated
 ↓
SQL Files Generated
 ↓
Git Commit + Push

⸻

🔹 8. Final Output in GitHub

repo/
 ├── dml/
 │    ├── customer_etl_param_dtls.sql
 │    ├── customer_etl_inbound_dtls.sql

⸻

🔹 9. Important Rules (Must Follow)

✔ Always pass SA (mandatory)
✔ Use comma-separated values for multiple SA
✔ Do not leave SA blank
✔ Check extract table before pushing

⸻

🔹 10. Quick Troubleshooting

⸻

❌ No data generated

✔ Check:

SELECT * FROM DML_DDL_CONFIG_DTLS;

⸻

❌ Wrong SA data coming

✔ Ensure correct input:

CALL ... ('CUSTOMER');

⸻

❌ Empty SQL files

✔ Check extract table:

SELECT COUNT(*) FROM DML_DDL_EXTRACT_DTLS;

⸻

🔹 11. One-Line Flow

Pass SA → Run Procedure → Check Extract Table → Run Script → Push to GitHub

⸻

If you want, I can next:
✅ Give ready-to-use Python script (your exact table structure)
✅ Or add input parameter to GitHub Actions (dynamic SA input)
✅ Or auto-trigger on schedule (daily extraction) 🚀
