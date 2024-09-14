resource "docker_image" "nginx" {
  name = "nginx:latest"
}

resource "docker_container" "nginx" {
  count = length(var.nginx_host)
  image = docker_image.nginx.image_id
  name = var.nginx_host[count.index]
  depends_on = [ docker_image.nginx, docker_volume.shared_volume ]
  ports {
    internal = "80"
    external = "808${count.index}"
  }
  volumes {
    read_only = false
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