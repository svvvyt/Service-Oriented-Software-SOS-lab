# "Service-Oriented Software" Subject Project

This project demonstrates the deployment of a Python application using a service-oriented architecture with Kubernetes and Docker. The application is built with Flask and interacts with a MariaDB database.

## Features

- **Python Application**: A Flask web app that connects to a MariaDB database and lists available databases.
- **MariaDB Database**: A relational database for storing and retrieving data.
- **Containerization**: Docker images used to package the application and database.
- **Orchestration**: Kubernetes configuration for deploying the services.

## Project Structure

### Files and Configurations

1. **`main.py`**: The main Flask application that connects to MariaDB and lists databases.
2. **`Dockerfile`**: Builds the Python Flask application image.
3. **`docker-compose.yaml`**: Local setup to run the Flask application and MariaDB using Docker Compose.
4. **`deployment.yaml`**: Kubernetes configurations for deploying the application and database.

### Kubernetes Components

- **StorageClass**: Defines a local-path provisioner for persistent volumes.
- **Deployment**: Manages the Flask application pods.
- **StatefulSet**: Ensures the MariaDB service runs with a persistent volume.
- **Service**: Exposes MariaDB within the cluster.

### Docker Compose Components

- **app**: Flask application container built from the `Dockerfile`.
- **mariadb**: MariaDB container configured with environment variables for root access.

## Requirements

### Software
- Python 3.13+
- Docker & Docker Compose
- Kubernetes (Minikube, Kind, or any Kubernetes cluster)
- `kubectl` CLI tool

### Python Dependencies
Defined in `requirements.txt`:
- Flask
- PyMySQL

Install with:
```bash
pip install -r requirements.txt
```

## Usage
### Local deployment
1. Build and run the services:
```bash
docker-compose up --build
```
2. Access the Flask app at http://localhost:8080.

### Kubernetes deployment
1. Apply the Kubernetes configuration:
```bash
kubectl apply -f deployment.yaml 
```
2. Verify pods are running:
```bash
kubectl get pods -n pavlenko-korolyov
```
3. Expose the Python app using a `kubectl port-forward` or a Kubernetes `Service`. 

### Expected output:
Access the application via a web browser or a tool like curl:
```bash
curl http://<your-service-endpoint>
```
The app will return a list of databases in the MariaDB instance.

## Project Objectives
This project is part of the Service-Oriented Software course and showcases:
- Usage of containerization technologies for service deployment.
- Configuration of Kubernetes resources for scalable and reliable application deployment.
- Interaction between a web application and a relational database in a service-oriented architecture.

## License
This project is developed for educational purposes. No explicit license is applied.