### **GitHub Repository Overview**
| **Category**         | **Details**                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Repository Name**   | terraform-devops-pipeline-automation                                                          |
| **Purpose**           | Automates AWS Lambda deployment using Terraform and integrates CI/CD practices.               |
---
### **Key Files**
| **File Name**         | **Description**                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------|
| `main.tf`             | Defines AWS Lambda function (`hello_world_lambda`) with runtime Python 3.9, S3 source, and IAM role. |
| `variables.tf`        | Contains variables: `aws_account_id`, `s3_bucket_name`, and `lambda_zip_path`.                  |
| `outputs.tf`          | Likely defines outputs for Terraform deployment.                                               |
| `versions.tf`         | Specifies required Terraform and provider versions.                                            |
| `.gitignore`          | Lists files and directories to ignore in version control.                                      |
| `.pfizer.yml`         | Configuration for internal workflows.                                                          |
| `README.md`           | Documentation about the repository's purpose and usage.                                        |
---
### **Folders**
| **Folder Name**       | **Contents**                                                                                   |
|-----------------------|-------------------------------------------------------------------------------------------------|
| `src/`                | - `app.py`: Python script for Lambda function.<br>- `requirements.txt`: Lists Python dependencies. |
| `.github/workflows/`  | Likely contains CI/CD workflows (not visible in detail).                                        |
---
### **Terraform Configuration Highlights**
| **Resource**          | **Details**                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Lambda Function       | - Name: `hello_world_lambda`.<br>- Runtime: Python 3.9.<br>- Handler: `app.lambda_handler`.    |
| S3 Bucket             | - Name: `lambda-deployments-devops-poc`.<br>- Key: `artifact/lambda_function.zip`.            |
| IAM Role              | - Referenced from existing role: `CUSPFE-Pfizer-Connect-application-deployment-pipeline`.      |
| Environment Variable  | - `BUCKET_NAME`: Set to the S3 bucket name.                                                   |
---
### **Variables in `variables.tf`**
| **Variable**          | **Description**                              | **Default Value**                          |
|-----------------------|----------------------------------------------|-------------------------------------------|
| `aws_account_id`      | AWS Account ID                              | `864033247427`                            |
| `s3_bucket_name`      | S3 bucket name for Lambda ZIP file           | `lambda-deploy-github-actions`            |
| `lambda_zip_path`     | Path to the Lambda deployment ZIP file       | `artifact/lambda_function.zip`            |
---
