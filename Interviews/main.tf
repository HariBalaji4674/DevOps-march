terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = ">5.22.0"
    }
  }
}
provider "aws " {
  region = "us-east-1"

}
resource "aws_instance" "jenkins" {

  ami = "ami-012938"
  instance_type = "t2.micro"
  
}