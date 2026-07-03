# ABC Technologies DevOps Project Report

## Student Details

- Register Number: 24BSA10188
- Name: Abhishek Nayak
- Course: DevOps
- Assignment: Assignment 2
- Use Case: Case 1 - Corporate Company Website Deployment

## Mandatory Submission Links

| No. | Submission Item | Details |
| --- | --- | --- |
| 1 | GitHub Repository Link | https://github.com/iabhishekn/24BSA10188-DevOps-Project |
| 2 | Jenkins Build URL or Screenshots | Jenkins ran locally at http://localhost:8085. Screenshots are included in the final PDF and `docs/screenshots/`. |
| 3 | Docker Hub Repository Link | Not used. The Docker image was built and run locally as `abc-technologies/corporate-website:latest`. |
| 4 | Application URL | Local: http://localhost:8080, Docker: http://localhost:8081, Kubernetes port-forward: http://localhost:8082 |
| 5 | Grafana Dashboard Screenshot | Included in final PDF and `docs/screenshots/grafana_dashboard_healthy.png`. |
| 6 | Nagios Monitoring Screenshot | Included in final PDF and `docs/screenshots/nagios_hosts_up.png`, `docs/screenshots/nagios_services_ok_clear.png`. |
| 7 | Graphite Metrics Screenshot | Included in final PDF and `docs/screenshots/graphite_browser_metric_available.png`. |

## Project Overview

ABC Technologies required a corporate website with automated deployment, containerized hosting, Kubernetes orchestration, and continuous monitoring. The implemented solution includes a responsive website, Jenkins pipeline, Docker container, Kubernetes Deployment and Service, Nagios HTTP monitoring, Graphite metrics ingestion, and a Grafana dashboard.

## Website Pages

- Home
- About Us
- Services
- Careers
- Contact Us
- Gallery

## Tools Used

- Git and GitHub for source code management
- Maven for packaging validation
- Jenkins for continuous integration and deployment automation
- Docker for containerized hosting
- Kubernetes for orchestration
- Nagios for availability monitoring
- Graphite for metrics storage
- Grafana for dashboard visualization

## Implementation Steps

1. Created the corporate website using HTML, CSS, JavaScript, and image assets.
2. Added project files to a Git repository for collaboration and version history.
3. Added a Maven `pom.xml` so the static website can be packaged during the build checklist.
4. Created a `Dockerfile` to host the website using Nginx.
5. Created a Jenkins pipeline to validate files, run Maven packaging, build Docker image, run a smoke test, and optionally deploy to Kubernetes.
6. Created Kubernetes Deployment and NodePort Service YAML files.
7. Added Nagios configuration for host and HTTP service checks.
8. Added Graphite and Grafana Docker Compose setup.
9. Added a Grafana dashboard showing CPU, memory, network usage, HTTP availability, and uptime.
10. Added a sample Graphite metrics sender script.

## Commands Used

```bash
mvn -DskipTests package
docker build -t abc-technologies/corporate-website:latest .
docker run -d --name abc-technologies-site -p 8081:80 abc-technologies/corporate-website:latest
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get svc
kubectl port-forward service/abc-technologies-service 8082:80
cd monitoring
docker compose -f docker-compose.monitoring.yml up -d
python scripts/send_graphite_metrics.py --target-url http://localhost:8082 --graphite-host localhost --graphite-port 2003
```

## Expected Final Output

- Source code stored in Git repository
- Jenkins automated build executed successfully
- Maven build completed successfully
- Docker image created successfully
- Docker container running
- Kubernetes pods and services running
- Website accessible through browser
- Nagios displays Host UP and HTTP Service OK
- Graphite receives monitoring metrics
- Grafana dashboard displays CPU, memory, network usage, HTTP availability, and uptime

## Screenshot Checklist

- GitHub repository page
- Jenkins dashboard
- Jenkins successful console output
- Maven build success
- Docker image build
- Docker running container
- Kubernetes pods
- Kubernetes service
- Website browser output
- Nagios Host UP and HTTP Service OK
- Graphite metrics
- Grafana dashboard
