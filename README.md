Cloud-Native Monitoring Application
This project demonstrates the creation of a cloud-native monitoring application using Python, Flask, Docker, and Kubernetes, with deployment on AWS EKS (Elastic Kubernetes Service).

Project Overview
The application monitors system metrics and is designed to be deployed as a containerized service using Docker and managed by Kubernetes. The deployment is carried out on AWS EKS, leveraging AWS services for scalability and reliability.

Technologies Used
Python: Programming language used for the application.
Flask: Web framework for building the monitoring application.
Docker: Containerization tool for packaging the application.
Kubernetes: Container orchestration platform for managing deployment.
AWS EKS: Managed Kubernetes service for running the application.
boto3: Python SDK for interacting with AWS services.
psutil: Library for retrieving system and process information.
plotly: Library for creating interactive plots.
Getting Started
Prerequisites
Docker
Kubernetes CLI (kubectl)
AWS CLI
AWS Account
Setup
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/cloud-native-monitoring-app.git
cd cloud-native-monitoring-app
Build the Docker Image

bash
Copy code
docker build -t monitoring-app .
Push the Docker Image to AWS ECR

Follow the instructions in the AWS ECR documentation to push the image to your repository.

Deploy to AWS EKS

Apply the Kubernetes deployment and service configuration:

bash
Copy code
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
Access the Application

Get the external IP address or DNS name of the service using:

bash
Copy code
kubectl get services
Article
For a detailed walkthrough of the project, visit the Medium article.
