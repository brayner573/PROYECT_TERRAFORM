
terraform {
  backend "s3" {
    bucket = "upeu-terraform-state"
    key    = "producer/main.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region
}
