Perfect 👍 — here’s your final Confluence-ready page with Liquibase formatted SQL output section added (copy-paste directly).

⸻

📘 DDL/DML Extraction – Developer Execution Guide

⸻

🔷 Overview

{panel:title=Overview|borderStyle=solid|borderColor=#ccc|bgColor=#F4F5F7}
This guide helps developers to:

* Execute extraction using Sub Area (SA)
* Retrieve generated SQL
* Generate SQL files
* Push output to GitHub (manual / automated)
* Generate Liquibase-ready SQL files
    {panel}

⸻

🔷 Prerequisites

{panel:title=Prerequisites|borderStyle=dashed|borderColor=#ccc}

* Snowflake access (execute permission)
* Database & schema access
* Python installed
* GitHub repo access
    {panel}

⸻

🔷 Step 1: Provide Sub Area (SA)

{expand:title=Click to see examples}

Single SA
{code:sql}
CALL POPULATE_DML_DDL_EXTRACT_MERGED(‘CUSTOMER’, …);
{code}

Multiple SA
{code:sql}
CALL POPULATE_DML_DDL_EXTRACT_MERGED(‘CUSTOMER,PRODUCT’, …);
{code}

Only provided SAs will be processed

{expand}

⸻

🔷 Step 2: Execute Stored Procedure

{code:sql}
CALL POPULATE_DML_DDL_EXTRACT_MERGED(
‘CUSTOMER,PRODUCT’,
‘<SRC_DB>’,
‘<SRC_SCHEMA>’,
‘<TGT_DB>’,
‘<TGT_SCHEMA>’,
‘<EXTRACT_DB>’,
‘<EXTRACT_SCHEMA>’,
‘DML_DDL_CONFIG_DTLS’
);
{code}

⸻

🔷 Step 3: Verify Extracted Data

{expand:title=Query Extract Table}

{code:sql}
SELECT *
FROM DML_DDL_EXTRACT_DTLS
WHERE SA_INPUT IN (‘CUSTOMER’,‘PRODUCT’);
{code}

Expected Output

|| SA_INPUT || OBJECT_NAME || TYPE || QUERY ||
| CUSTOMER | ETL_PARAM_DTLS | DML | INSERT SQL |
| PRODUCT  | ETL_INBOUND_DTLS | DML | INSERT SQL |

Each row = one SQL file content

{expand}

⸻

🔷 Step 4: Generate SQL Files

{panel:title=Run Python Script|bgColor=#E3FCEF}
{code:bash}
python generate_sql_files.py
{code}
{panel}

⸻

🔹 Output Structure

{code:bash}
snowflake/
├── ddl/
├── dml/
{code}

⸻

🔷 🔥 Liquibase Formatted Output (NEW)

⸻

{panel:title=Liquibase Support|bgColor=#EAE6FF}
All generated SQL files are automatically formatted for Liquibase execution.
{panel}

⸻

🔹 File Naming Convention

{code}
.sql
{code}

Example:
{code}
01_emea_customer_dml_etl_param_dtls.sql
{code}

⸻

🔹 Liquibase File Format

Each file follows this structure:

{code:sql}
– liquibase formatted sql

– changeset cicd:customer_etl_param_dtls_1
– comment: DML for CUSTOMER - ETL_PARAM_DTLS

INSERT INTO ETL_PARAM_DTLS (…)
SELECT …
;

– changeset cicd:customer_etl_param_dtls_2
– comment: Additional data

INSERT INTO ETL_PARAM_DTLS (…)
SELECT …
;
{code}

⸻

🔹 Key Standards Implemented

{panel:title=Standards Applied|bgColor=#FFF4E5}

* Author is always: cicd
* No duplicate changesets
* No extra blank spaces
* Proper SQL formatting (readable like normal SQL)
* Full object names used (no short forms)
* One file per object per SA
    {panel}

⸻

🔹 Changeset Naming Rule

{code}
cicd:
{code}

Example:
{code}
cicd:customer_etl_param_dtls_1
cicd:customer_etl_param_dtls_2
{code}

⸻

🔹 Folder Separation

{code:bash}
snowflake/
├── ddl/
│    ├── customer_tables.sql
│    ├── customer_views.sql
│
├── dml/
│    ├── customer_etl_param_dtls.sql
│    ├── customer_etl_inbound_dtls.sql
{code}

⸻

🔷 Step 5: Push to GitHub (Manual)

{code:bash}
git add .
git commit -m “DDL DML extraction for CUSTOMER, PRODUCT”
git push
{code}

⸻

🔷 Step 6: GitHub Actions (Automated)

{expand:title=Run via GitHub UI}

1. Open repository
2. Go to Actions
3. Select DDL DML Extraction
4. Click Run Workflow
5. Enter:

{code}
CUSTOMER,PRODUCT
{code}

{expand}

⸻

🔹 Pipeline Flow

{panel:title=Execution Flow|bgColor=#DEEBFF}
Trigger Workflow
↓
Execute Stored Procedure
↓
Populate Extract Table
↓
Generate Liquibase SQL Files
↓
Commit & Push to GitHub
{panel}

⸻

🔷 Final Output in Repository

{code:bash}
repo/
├── snowflake/
│    ├── ddl/
│    ├── dml/
{code}

⸻

🔷 Important Guidelines

{panel:title=Important|bgColor=#FFF4E5}

* Always provide SA input
* Use comma-separated values for multiple SA
* Do not leave SA empty
* Verify extract table before generating files
* Do not manually edit generated Liquibase changesets
    {panel}

⸻

🔷 Troubleshooting

{expand:title=Common Issues & Fixes}

No Data Generated
{code:sql}
SELECT * FROM DML_DDL_CONFIG_DTLS;
{code}

Incorrect Data

* Check SA input
* Verify SA names

Duplicate Changesets

* Ensure sequence logic is not reset in script

Formatting Issues

* Ensure latest regex formatter is used

{expand}

⸻

🔷 Quick Flow

{panel:title=Summary|bgColor=#F4F5F7}
Provide SA → Execute Procedure → Verify Extract Table → Generate Liquibase SQL → Push to GitHub
{panel}

⸻

✅ Now this includes:

* Confluence macros
* Execution steps
* Liquibase-ready output
* Naming + formatting standards

⸻

If you want next upgrade, I can:
🚀 ￼ Add master changelog.xml auto-generation
🚀 ￼ Add Liquibase deploy command section
🚀 ￼ Add rollback scripts generation
