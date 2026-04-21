Got it 👍 — here’s your final, clean, summarized Confluence page including everything we built so far:

* Config-driven extraction
* Stored procedures
* SA-based execution
* Extract table
* File generation
* Liquibase format
* GitHub Actions

👉 Optimized for developer usage (execution-focused, not deep logic)

⸻

📘 DDL-DML Extraction using Stored Procs & GitHub Actions

⸻

🔷 Overview

This solution enables developers to:

* Extract DDL & DML using Sub Area (SA)
* Use config-driven approach (no code change)
* Generate SQL / Liquibase-ready files
* Push output to GitHub (manual / automated)

⸻

🔷 End-to-End Flow

Config (DML_DDL_CONFIG_DTLS)
        ↓
Extraction Stored Procedure
        ↓
Extract Table (DML_DDL_EXTRACT_DTLS)
        ↓
Python File Generator
        ↓
Liquibase SQL Files
        ↓
GitHub (Manual / Actions)

⸻

🔷 Key Components

⸻

🔹 1. Config Table

DML_DDL_CONFIG_DTLS

Purpose

* Defines what to extract (tables, DML objects, etc.)
* Fully drives extraction logic

Developer Role

* Add/remove entries when needed
* No change in stored procedure

⸻

🔹 2. Config Setup Procedure (Optional)

POPULATE_DML_DDL_CONFIG_DTLS

Usage

CALL POPULATE_DML_DDL_CONFIG_DTLS();

When to Use

* Initial setup
* New schema onboarding

⸻

🔹 3. Extraction Stored Procedure

POPULATE_DML_DDL_EXTRACT_MERGED

Purpose

* Reads config
* Filters by SA
* Generates SQL into extract table

⸻

🔹 4. Extract Table

DML_DDL_EXTRACT_DTLS

Contains

* SA_INPUT
* OBJECT_NAME
* TYPE (DDL/DML)
* GENERATED SQL

⸻

🔷 Developer Execution Steps

⸻

🔹 Step 1: Provide SA Input

Single SA

CALL POPULATE_DML_DDL_EXTRACT_MERGED('CUSTOMER', ...);

Multiple SA

CALL POPULATE_DML_DDL_EXTRACT_MERGED('CUSTOMER,PRODUCT', ...);

✔ Only given SA will be processed

⸻

🔹 Step 2: Execute Extraction

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

🔹 Step 3: Validate Extract Data

SELECT *
FROM DML_DDL_EXTRACT_DTLS
WHERE SA_INPUT IN ('CUSTOMER','PRODUCT');

✔ Ensure data exists before file generation

⸻

🔹 Step 4: Generate SQL Files

python generate_sql_files.py

⸻

🔹 Step 5: Push to GitHub

git add .
git commit -m "DDL DML extraction"
git push

⸻

🔷 Liquibase Output (Standardized)

⸻

🔹 Format

-- liquibase formatted sql
-- changeset cicd:customer_etl_param_dtls_1
-- comment: DML for CUSTOMER - ETL_PARAM_DTLS
INSERT INTO ETL_PARAM_DTLS (...)
SELECT ...
;

⸻

🔹 Rules Implemented

* Author → cicd
* Full object names (no short forms)
* One file per object per SA
* Sequential changesets
* Clean SQL (regex formatted)

⸻

🔹 File Naming

<sequence>_<sa>_<type>_<object>.sql

Example

01_customer_dml_etl_param_dtls.sql

⸻

🔷 Output Structure

snowflake/
 ├── ddl/
 ├── dml/
 │    ├── customer_etl_param_dtls.sql
 │    ├── customer_etl_inbound_dtls.sql

⸻

🔷 GitHub Actions (Automation)

⸻

🔹 Trigger Steps

1. Go to GitHub → Actions
2. Select workflow
3. Click Run Workflow
4. Enter:

CUSTOMER,PRODUCT

⸻

🔹 Pipeline Flow

Input SA
   ↓
Run Stored Proc
   ↓
Populate Extract Table
   ↓
Generate SQL Files
   ↓
Commit & Push to GitHub

⸻

🔷 Important Guidelines

* Always pass SA input
* Use comma-separated values for multiple SA
* Do not modify stored procedures
* Update config for new objects
* Validate extract table before generating files

⸻

🔷 Troubleshooting

⸻

🔸 No Data Generated

SELECT * FROM DML_DDL_CONFIG_DTLS;

⸻

🔸 Wrong Data

* Check SA input
* Validate config entries

⸻

🔸 Empty SQL Files

SELECT COUNT(*) FROM DML_DDL_EXTRACT_DTLS;

⸻

🔷 Final Summary

Config decides WHAT
Procedure decides WHEN
Script decides FORMAT
Git decides WHERE

⸻

✅ This is now:

* Fully structured
* Covers everything you implemented
* Developer-friendly
* Confluence-ready (new editor compatible)

⸻

If you want next level:
🚀 Add diagram image for Confluence
🚀 Add actual GitHub Actions YAML
🚀 Add Python script (final version)
