
resource "docker_image" "nginx" {
  name = "nginx:latest"
}

resource "docker_container" "nginx" {
  count = var.nginx_host.index
  image = docker_image.nginx.image_id
  name = "nginx {{count.index }}"
  ports {
    internal = "80"
    external = "8081"
  }
  volumes {
    read_only = false
    # host_path = abspath("nginx.cfg")
    container_path = "/usr/local/nginx/conf"
    volume_name = docker_volume.shared_volume.name
  }
}

resource "docker_volume" "shared_volume" {
  name = "shared_volume"
  driver = "local"
}

output "nginx" {
  value = docker_volume.shared_volume.mountpoint
}
output "nginx_host" {
  value = var.nginx_host
}