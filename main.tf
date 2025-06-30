terraform {
  backend "s3" {
    bucket = "upeu-terraform-state"
    key    = "s3/producer.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "input_bucket" {
  bucket        = var.x_bucket
  force_destroy = true
}

output "input_bucket_name" {
  value = aws_s3_bucket.input_bucket.id
}
