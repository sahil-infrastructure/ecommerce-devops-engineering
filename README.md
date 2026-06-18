# 🚀 E-Commerce Devops Engineering Project

## Overview

This project demonstrates the deployment, monitoring, troubleshooting, and recovery of a containerized e-commerce platform using industry-standard Platform Engineering and DevOps practices.

The objective was to simulate a production-style environment and gain hands-on experience with:

* Containerization
* Service orchestration
* Infrastructure monitoring
* Observability
* Incident response
* Deployment rollback strategies

The project follows operational workflows commonly used by DevOps Engineers, Platform Engineers, and Site Reliability Engineers (SREs).

---

# 🏗 Architecture

![Architecture Diagram](screenshots/architecture-diagram.png)

### Application Flow

```text
User
 │
 ▼
Flask Application
 │
 ▼
PostgreSQL Database
```

### Monitoring Flow

```text
Application Containers
        │
        ▼
     cAdvisor
        │
        ▼
    Prometheus
        │
        ▼
      Grafana
```

---

# ⚙ Technology Stack

| Category              | Technology     |
| --------------------- | -------------- |
| Application           | Python Flask   |
| Database              | PostgreSQL     |
| Containerization      | Docker         |
| Orchestration         | Docker Compose |
| Monitoring            | Prometheus     |
| Container Metrics     | cAdvisor       |
| Visualization         | Grafana        |
| Version Control       | Git            |
| Repository Management | GitHub         |

---

# ✨ Key Features

## Application Layer

* Flask-based REST API
* Health Check Endpoint
* PostgreSQL Integration
* Containerized Deployment

## Containerization

* Custom Docker Image
* Docker Compose Orchestration
* Persistent Storage
* Internal Container Networking

## Monitoring & Observability

* Real-time Container Metrics
* Resource Utilization Tracking
* Infrastructure Monitoring
* Service Availability Monitoring

## Dashboards

* CPU Utilization
* Memory Utilization
* Running Container Count
* Filesystem Usage
* Container Health Monitoring

## Incident Management

* Failure Simulation
* Service Recovery Validation
* Version Rollback Testing
* Health Verification

---

# 📊 Monitoring Stack

## Prometheus

Prometheus is responsible for collecting and storing metrics from monitored services.

Features:

* Metric Scraping
* Time-Series Storage
* Service Monitoring
* Availability Tracking

### Prometheus Targets

![Prometheus Targets](screenshots/prometheus-targets.png)

---

## cAdvisor

cAdvisor collects container-level resource metrics including:

* CPU Usage
* Memory Usage
* Filesystem Utilization
* Network Statistics

---

## Grafana

Grafana provides visualization and monitoring dashboards.

### Grafana Dashboard

![Grafana Dashboard](screenshots/grafana-dashboard.png)

Monitored Metrics:

* CPU Usage
* Memory Usage
* Container Health
* Filesystem Utilization
* Running Containers

---

# 🐳 Running Containers

The application stack is deployed using Docker Compose.

### Active Containers

![Docker Containers](screenshots/docker-containers.png)

Components:

* Flask Application
* PostgreSQL
* Prometheus
* Grafana
* cAdvisor

---

# 🔍 Health Verification

Verify application health:

```bash
curl http://localhost:5000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

# 🚨 Incident Simulation & Rollback

To simulate a real-world deployment failure, a faulty application version (v1.1.0) was intentionally deployed.

## Failure Scenario

Observed behavior:

* Application startup failure
* Service unavailability
* Container restart loop
* Health check failure

## Recovery Procedure

Rollback actions:

1. Reverted deployment from v1.1.0 to v1.0.0
2. Recreated application containers
3. Validated service health
4. Confirmed application availability
5. Verified monitoring recovery

## Outcome

Service was successfully restored with minimal downtime using a controlled rollback procedure.

---

# 📁 Repository Structure

```text
ecommerce-platform/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│
├── compose/
│   └── docker-compose.yml
│
├── monitoring/
│   └── prometheus/
│       └── prometheus.yml
│
├── screenshots/
│   ├── architecture-diagram.png
│   ├── docker-containers.png
│   ├── prometheus-targets.png
│   └── grafana-dashboard.png
│
└── README.md
```

---

# 🎯 Skills Demonstrated

* Docker
* Docker Compose
* Python Flask
* PostgreSQL
* Infrastructure Monitoring
* Prometheus
* Grafana
* Container Observability
* Incident Troubleshooting
* Deployment Rollback
* Git Version Control
* GitHub Collaboration

---

# 📚 Learning Outcomes

Through this project I gained practical experience in:

* Building containerized applications
* Managing multi-container deployments
* Monitoring infrastructure and services
* Implementing observability practices
* Troubleshooting production-style incidents
* Validating service recovery procedures
* Understanding rollback strategies
* Maintaining infrastructure through version control

---

# 🔮 Future Enhancements

Planned improvements:

* Kubernetes Deployment
* GitHub Actions CI/CD Pipeline
* Terraform Infrastructure Provisioning
* Alertmanager Integration
* Centralized Logging
* Blue-Green Deployments
* Horizontal Scaling
* Automated Rollback Workflows

---

# 👨‍💻 Author

**Sahil**
Senior IT Support Engineer
Aspiring Platform Engineer

This project was created as part of my hands-on Platform Engineering and DevOps learning journey, focusing on real-world operational practices used in modern cloud-native environments.
