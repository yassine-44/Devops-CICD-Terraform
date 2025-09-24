terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.6.2"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_container" "wiki_app" {
  name  = "wiki-app"
  image = "yassinekrout/wiki-app:latest"  # Will be pushed soon
  ports {
    internal = 5000
    external = 5000
  }
  restart = "always"
}