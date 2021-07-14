module "node" {
  source = "./compute"

  instances = 2
  component = "node"
  mesh_name = var.mesh_name
}

module "control_plane" {
  source = "./compute"

  component = "control-plane"
  mesh_name = var.mesh_name
}

output "node_ips" {
  value = module.node.instance_ip
}

output "control_plane_ips" {
  value = module.control_plane.instance_ip
}
