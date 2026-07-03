# ABC Technologies DevOps Project

Case 1 implementation for the DevOps Assignment: Corporate Company Website Deployment.

## Project Contents

- Multi-page corporate website: Home, About Us, Services, Careers, Contact Us, Gallery
- Maven project file for assignment checklist packaging
- Jenkins declarative pipeline
- Dockerfile using Nginx
- Kubernetes Deployment and NodePort Service
- Nagios HTTP monitoring configuration
- Graphite and Grafana monitoring setup
- Grafana dashboard JSON for CPU, memory, network, HTTP availability, and uptime
- Documentation report template in `docs/`

## Local Website Preview

Open `index.html` in a browser, or serve the folder locally:

```bash
python -m http.server 8080
```

Then visit:

```text
http://localhost:8080
```

## Maven Build

```bash
mvn -DskipTests package
```

Expected output:

```text
BUILD SUCCESS
```

The packaged artifact is created in `target/corporate-website-1.0.0.jar`.

## Docker Build And Run

```bash
docker build -t abc-technologies/corporate-website:latest .
docker run -d --name abc-technologies-site -p 8080:80 abc-technologies/corporate-website:latest
docker ps
```

Open:

```text
http://localhost:8080
```

Useful screenshot points:

- Docker build success
- Running container from `docker ps`
- Browser output at `http://localhost:8080`

## Kubernetes Deployment

For Minikube or another local cluster:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -l app=abc-technologies-website
kubectl get svc abc-technologies-service
```

The NodePort is configured as `30080`.

For Minikube:

```bash
minikube service abc-technologies-service --url
```

Useful screenshot points:

- Deployment created
- Pods in Running state
- Service with NodePort
- Browser output from the Kubernetes URL

## Jenkins Pipeline

1. Push this folder to a GitHub repository named `RegisterNumber-DevOps-Project`.
2. Create a Jenkins Pipeline job.
3. Use "Pipeline script from SCM".
4. Select Git and paste the GitHub repository URL.
5. Set the script path to `Jenkinsfile`.
6. Build the job.

Optional Jenkins environment variables:

```text
DOCKERHUB_REPO=your-dockerhub-user/corporate-website
PUSH_IMAGE=true
DEPLOY_K8S=true
```

Set `PUSH_IMAGE=true` only after Docker Hub login or Jenkins credentials are configured.
Set `DEPLOY_K8S=true` only when Jenkins has access to the Kubernetes cluster.

Useful screenshot points:

- Jenkins dashboard
- Job configuration
- Successful pipeline stages
- Console output

## Monitoring With Nagios

Copy `monitoring/nagios/abc-technologies.cfg` into the Nagios object configuration directory and include it from `nagios.cfg`.

The file checks:

- Host availability
- Home page HTTP availability on port `8080`
- Careers page HTTP availability on port `8080`

Update the `address` and port if the website is hosted on another host or Kubernetes URL.

Useful screenshot points:

- Host status UP
- HTTP Service status OK

## Graphite And Grafana

Start Graphite and Grafana:

```bash
cd monitoring
docker compose -f docker-compose.monitoring.yml up -d
```

Open:

```text
Graphite: http://localhost:8081
Grafana:  http://localhost:3000
```

Grafana login:

```text
Username: admin
Password: admin
```

Send sample metrics to Graphite:

```bash
python scripts/send_graphite_metrics.py --target-url http://localhost:8080 --graphite-host localhost --graphite-port 2003
```

The dashboard file is automatically provisioned at:

```text
ABC Technologies / ABC Technologies Website Health
```

Useful screenshot points:

- Graphite receiving metrics
- Grafana dashboard showing CPU, memory, network usage, HTTP availability, and uptime

## Submission Checklist

- GitHub repository link
- Jenkins dashboard, configuration, console output, successful build screenshots
- Maven build success screenshot
- Docker image build screenshot
- Docker container running screenshot
- Kubernetes pods and services screenshots
- Application browser screenshot
- Nagios Host UP and HTTP Service OK screenshot
- Graphite metrics screenshot
- Grafana dashboard screenshot
- Final documentation report PDF

