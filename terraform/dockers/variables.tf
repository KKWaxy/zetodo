variable "nginx_host" {
    type = list(string)
    default = [
        "nginx_1",
        "nginx_2",
        "nginx_3"
    ]
}