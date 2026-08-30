terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "dev"
}

resource "aws_s3_bucket" "demo_bucket" {
  bucket = "kkama-terraform-demo-2026-001"
}
