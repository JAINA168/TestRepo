variable "use_vpc" {
  description = "Whether to use VPC configuration"
  type        = bool
  default     = false
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
  default     = ""
}

variable "subnet_ids" {
  description = "List of subnet IDs"
  type        = list(string)
  default     = []
}

variable "security_group_ids" {
  description = "List of security group IDs"
  type        = list(string)
  default     = []
}

provider "aws" {
  region = "eu-west-1"
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/lambda_function"
  output_path = "${path.module}/lambda_function.zip"
}

resource "aws_lambda_function" "example" {
  function_name    = var.function_name
  runtime          = var.runtime
  handler          = var.handler
  role             = var.role_arn
  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  dynamic "vpc_config" {
    for_each = var.use_vpc ? [1] : []
    content {
      subnet_ids         = var.subnet_ids
      security_group_ids = var.security_group_ids
    }
  }

  layers = [var.layer_arn]
}

module "lambda_function" {
  source             = "./path/to/lambda-module"
  function_name      = "cuspfe-sfa-serverless-schedule-overlap-validator"
  role_arn           = "<your-role-arn>"
  use_vpc            = true # Set to false if not using VPC
  vpc_id             = "vpc-0704639f39dd42648"
  subnet_ids         = ["subnet-0eed0ad970e0de4da", "subnet-0d27155305a528e91"]
  security_group_ids = ["sg-06ae8c6079c387c1b"]
  layer_arn          = "arn:aws:lambda:eu-west-1:638200722556:layer:serverless:4"
}

