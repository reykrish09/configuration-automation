terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
    backend "s3" {
    bucket = "kkama-terraform-state-2026-001"
    key    = "terraform-aws-lab/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region  = "us-east-1"
}

resource "aws_s3_bucket" "demo_bucket" {
  bucket = "kkama-terraform-demo-2026-001"
}
