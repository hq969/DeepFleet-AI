provider "aws" {
  region = "us-east-1"
}

resource "aws_sagemaker_model" "fleet_model" {
  name = "deepfleet-model"
  execution_role_arn = "arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole"
  primary_container {
    image = "123456789012.dkr.ecr.us-east-1.amazonaws.com/fleet-ml"
    model_data_url = "s3://bucket/fleet/model.tar.gz"
  }
}
