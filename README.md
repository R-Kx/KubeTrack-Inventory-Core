# 🚀 KubeTrack Inventory API: Automated CI/CD Infrastructure
[![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.28%2B-blue?logo=kubernetes)](https://kubernetes.io/)
[![Helm](https://img.shields.io/badge/Helm-v3-white?logo=helm)](https://helm.sh/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange?logo=githubactions)](https://github.com/features/actions)
[![Docker Hub](https://img.shields.io/badge/Docker-Hub-blue?logo=docker)](https://hub.docker.com/)

## 📖 Overview
This repository hosts the **KubeTrack Inventory API**, integrated with a robust, production-grade **CI/CD pipeline**. The project demonstrates a full GitOps-oriented workflow, moving from code commit to automated deployment on a local **K3s (Kubernetes)** cluster.

---

## 🏗️ Architecture & Infrastructure
The infrastructure is designed for speed and reliability, utilizing a hybrid-cloud approach with on-premise orchestration.

* **Orchestration:** [K3s](https://k3s.io/) (Lightweight Kubernetes) running on a dedicated Linux node.
* **Networking:** * **MetalLB:** Layer 2 Load-Balancer for internal/external IP management.
    * **Nginx Ingress Controller:** Advanced traffic routing and SSL termination.
* **Storage & Config:** Managed via **Helm Charts** for dynamic environment configuration.

---

## ⚙️ CI/CD Pipeline Logic
The pipeline is powered by **GitHub Actions** interacting with a **Self-hosted Runner** for direct cluster access.

### The Workflow:
1.  **Build Phase:** Triggered on every `push`. Builds a Docker image using `docker/metadata-action` for precise tagging.
2.  **Versioning:** Implements **Git SHA tagging** alongside `latest` for traceability and immediate updates.
3.  **Artifact Management:** Helm Charts are packaged and stored as build artifacts to ensure deployment consistency.
4.  **Deployment Phase:** The self-hosted runner executes a `Helm Upgrade --Install` command, ensuring **Zero-Downtime** updates.
5.  **Pull Policy:** Set to `Always` to guarantee the cluster pulls the freshest image from Docker Hub.

---

## 📊 Observability Stack
A DevOps project is incomplete without visibility. This cluster is monitored via the **LG Stack**:
* **Loki:** Centralized log aggregation from all Kubernetes namespaces.
* **Grafana:** Real-time dashboards visualizing cluster health, pod metrics, and deployment history.

> **Note:** Log retention and metric scraping are optimized for low-resource environments using the K3s agent.

---

## 🚀 Deployment Guide

### Prerequisites
* A running **K3s** or **K8s** cluster.
* **Helm v3** installed.
* Kubeconfig configured in your environment.

### Installation

# Clone the repository
git clone [https://github.com/R-Kx/KubeTrack-Inventory-Core.git](https://github.com/R-Kx/KubeTrack-Inventory-Core.git)

# Deploy using Helm
helm upgrade --install inventory-api ./charts/KubeTrack-inventory-api \
  --namespace default \
  --values ./charts/KubeTrack-inventory-api/values.yaml

---

### 🛠️ Tech Stack & Tools

    Cloud/Infra: K3s, Ubuntu Server, MetalLB.

    Tools: Helm, Docker, GitHub Actions, Nginx Ingress.

    Monitoring: Loki, Grafana, Promtail.

---

### Developed by R-Kx – Building scalable, automated systems one pod at a time.
