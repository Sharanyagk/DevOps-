# Tracking the Effectiveness of Automation in DevOps

## Overview
This project focuses on automating the deployment and monitoring of a containerized application while tracking the effectiveness of DevOps automation. It leverages **CI/CD pipelines, Prometheus, and Grafana** to measure and visualize key metrics related to automation efficiency.

## Features
✅ **CI/CD Pipeline**: Automated deployment using GitHub Actions.  
✅ **Kubernetes Deployment**: Deploys a Flask app with Prometheus metrics.  
✅ **Prometheus Monitoring**: Tracks build, deployment, and application performance.  
✅ **Grafana Dashboard**: Visualizes key automation effectiveness metrics.  
✅ **Logging & Analysis**: Captures build and deployment times.  

---

## Project Structure
```
📂 tracking_automation_devops
├── deploy.yml                # CI/CD pipeline for automation tracking
├── app.py                    # Flask app exposing Prometheus metrics
├── requirements.txt          # Dependencies for Flask, Gunicorn, Prometheus
├── backend-deployment.yaml   # Kubernetes deployment for backend service
├── backend-service.yaml      # Kubernetes service for backend app
├── grafana-dashboard.json    # Pre-configured Grafana dashboard
└── README.md                 # Project documentation
```

---

## Installation & Setup

### 1️⃣ Prerequisites
- **Cloud Account (e.g., IBM Cloud, AWS, GCP)**
- **Kubernetes Cluster**
- **Docker & kubectl installed**
- **GitHub Actions setup**

### 2️⃣ Clone Repository
```bash
git clone <repository-url>
cd tracking_automation_devops
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Flask Application Locally
```bash
python app.py
```

---

## Deployment Guide

### 🔹 **Step 1: Build & Push Docker Image**
```bash
docker build -t backend-app:latest .
docker tag backend-app:latest gcr.io/project-id/backend-app:1.0
docker push gcr.io/project-id/backend-app:1.0
```

### 🔹 **Step 2: Deploy to Kubernetes**
```bash
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
```

### 🔹 **Step 3: Verify Deployment**
```bash
kubectl get pods
kubectl get svc
```

---

## Monitoring & Observability

### ✅ **Prometheus Setup**
1. Deploy Prometheus to Kubernetes.
2. Configure `prometheus.yml` to scrape the Flask app metrics.
3. Access Prometheus UI to verify metrics.

### ✅ **Grafana Dashboard**
1. Deploy Grafana to Kubernetes.
2. Load `grafana-dashboard.json` in Grafana.
3. View **CPU usage, memory, and request rate** graphs.

---

## CI/CD Pipeline Automation
This project includes a **GitHub Actions** workflow (`deploy.yml`) that automates:
1. **Build**: Creates a Docker image of the app.
2. **Push**: Uploads the image to a container registry.
3. **Deploy**: Deploys the app to Kubernetes.
4. **Monitor**: Logs build and deployment times for tracking automation effectiveness.

---

## Metrics to Track Automation Effectiveness
- **Build Time**: Time taken to build the Docker image.
- **Deployment Time**: Time taken to deploy the application to Kubernetes.
- **Application Performance**: CPU, memory usage, and request rates.
- **Failure Rates**: Frequency of build or deployment failures.
- **Recovery Time**: Time taken to recover from failures.

---

## Future Enhancements
🚀 **Auto-Rollbacks**: Implement rollback mechanisms on failure.  
🚀 **Multi-Cloud Support**: Extend monitoring to AWS/GCP.  
🚀 **Cost Optimization**: Analyze usage and optimize resource allocation.  
🚀 **Alerting**: Set up alerts for critical metrics using Prometheus and Grafana.  
🚀 **Historical Data Analysis**: Store and analyze historical data to identify trends and improve automation processes.  

---

## Contributors
👤 **Sharanya G K**  
📧 Contact: your-sharanyagkmys@gmail.com  
🔗 GitHub: [your-github-profile](https://github.com/Sharanyagk/DevOps-)

---

## License
MIT License © 2025

---

This project provides a comprehensive framework for tracking the effectiveness of automation in DevOps, enabling teams to measure and improve their CI/CD pipelines and deployment processes.
