To pass the trusted entities as a data block in Terraform, you need to correctly format the IAM policy document. Here's how you can define it:

### Corrected Terraform Configuration

```hcl
provider "aws" {
  region = "us-west-2"  # Update with your desired region
}

variable "permission_boundary_arn" {
  description = "The ARN of the existing permission boundary policy"
  type        = string
}

resource "aws_iam_role" "saml_role" {
  name                 = "saml-role"
  assume_role_policy   = data.aws_iam_policy_document.saml_assume_role_policy.json
  permissions_boundary = var.permission_boundary_arn
}

data "aws_iam_policy_document" "saml_assume_role_policy" {
  statement {
    effect = "Allow"
    principals {
      type        = "Federated"
      identifiers = ["arn:aws:iam::YOUR_ACCOUNT_ID:saml-provider/PFE-AWS-PROD"]
    }
    actions = ["sts:AssumeRoleWithSAML"]
    condition {
      test     = "StringEquals"
      variable = "SAML:aud"
      values   = ["https://signin.aws.amazon.com/saml"]
    }
  }
}
```

### Key Points

- **Condition Block**: Use the `condition` block inside the `statement` to specify conditions. Ensure it's formatted correctly.
- **AWS Credentials**: Make sure your AWS credentials are set up in Terraform Cloud as environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).
- **Permissions**: Ensure the IAM user or role has permissions to perform necessary actions like `sts:AssumeRoleWithSAML`.

### Deployment Steps

1. **Commit and Push Changes**:
   - Ensure your changes are committed and pushed to the `dev` branch.

   ```bash
   git add .
   git commit -m "Fix trust policy configuration"
   git push origin dev
   ```

2. **Configure Terraform Cloud Workspace**:
   - Verify that your workspace is set to use the `dev` branch.
   - Set the `permission_boundary_arn` variable in Terraform Cloud.

3. **Run Terraform Plan and Apply**:
   - Trigger a run in Terraform Cloud to apply your changes.

This setup should resolve the errors and correctly configure the IAM role with SAML federation.

Sources
[1] image.jpg https://pplx-res.cloudinary.com/image/upload/v1728053856/user_uploads/oohxwqvvh/image.jpg
[2] image.jpg https://pplx-res.cloudinary.com/image/upload/v1728054616/user_uploads/uiblbfgwc/image.jpg
[3] image.jpg https://pplx-res.cloudinary.com/image/upload/v1728032335/user_uploads/cjxpvromr/image.jpg
[4] image.jpg https://pplx-res.cloudinary.com/image/upload/v1728033501/user_uploads/trlkyfxoq/image.jpg
[5] image.jpg https://pplx-res.cloudinary.com/image/upload/v1728053112/user_uploads/qkwejujyk/image.jpg
