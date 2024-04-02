provider "google" {
  project = "groovy-camera-409915"
  region  = "us-central1"
  zone    = "us-central1-a"
  credentials = file("credentials.json")
}

resource "google_compute_instance" "webserver" {
  name         = "my-webserver"
  machine_type = "n2-standard-2"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
      # nat_ip = "automatic"
    }
  }
}
