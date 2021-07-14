variable "component" {}
variable "mesh_name" {}
variable "instances" { default = 1 }

provider "aws" {
  region = "us-east-1"
}

resource "aws_lightsail_instance" "this" {
  count             = var.instances
  name              = "${var.mesh_name}-${var.component}${count.index + 1}"
  availability_zone = "us-east-1a"
  blueprint_id      = "ubuntu_20_04"
  bundle_id         = "medium_2_0"
  key_pair_name     = "id_rsa"

  tags = {
    component    = var.component
    service-mesh = var.mesh_name
  }
}

output "instance_ip" {
  value = aws_lightsail_instance.this[*].public_ip_address
}