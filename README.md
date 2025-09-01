# Economic-Indicator-Data-Pipeline
[![CI-CD](https://github.com/jibbs1703/Economic-Indicator-Data-Pipeline/actions/workflows/ci-cd.yaml/badge.svg?branch=main)](https://github.com/jibbs1703/Economic-Indicator-Data-Pipeline/actions/workflows/ci-cd.yaml)
![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
![license](https://img.shields.io/github/license/peaceiris/actions-gh-pages.svg)
![Docker](https://img.shields.io/badge/Docker-v43-blue?logo=docker&style=flat)
![Terraform](https://img.shields.io/badge/Terraform-v6.0.0-blue?logo=terraform&style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-v16.0-blue?logo=postgresql&style=flat)


## Overview

This repository contains an ETL (Extract, Transform, Load) pipeline designed to automate the extraction, transformation, and loading of economic indicator data into a data warehouse in AWS S3. The pipeline is scripted in Python and orchestrated via Apache Airflow, providing robust scheduling, monitoring, and dependency management. 

The entire process is hosted on an AWS EC2 instance, which is provisioned and configured using Infrastructure as Code (IaC) principles. The EC2 instance deployment is automated via Terraform, ensuring repeatable and consistent infrastructure management. The configuration and updates to the pipeline are handled through GitHub Actions as part of the CI/CD workflow.

To optimize resource usage and cost efficiency, the EC2 instance is automatically started and stopped at specific intervals using AWS Lambda and Amazon EventBridge. This ensures that the pipeline runs periodically without keeping the server running unnecessarily.

## Pipeline Features

- Apache Airflow Orchestration: The ETL workflow is managed using Apache Airflow DAGs, enabling seamless scheduling, dependency handling, and monitoring of data processing tasks.

- Infrastructure as Code (IaC) Deployment: The AWS EC2 instance and its dependencies are provisioned using Terraform, ensuring that infrastructure changes are trackable, repeatable, and maintainable.

- Cloud-Based Hosting: The entire ETL process runs on an AWS EC2 instance, ensuring scalability and flexibility in managing data workflows.

- Automated CI/CD Deployment: The EC2 instance is configured and updated via GitHub Actions, automating the deployment of new features, updates, and patches.

- Scheduled EC2 Start/Stop: The EC2 instance is automatically started and stopped using AWS Lambda and Amazon EventBridge, reducing unnecessary costs while ensuring timely pipeline execution.

- Secure Environment Variables: Sensitive data such as API keys and database credentials are securely managed using Airflow Variables, AWS Secrets Manager, and Terraform.

- Logging and Monitoring: Airflow’s built-in monitoring tools provide detailed execution logs and task tracking, helping identify failures and streamline debugging.

## Pipeline Orchestration

1. Infrastructure Provisioning (IaC): The EC2 instance and necessary resources (IAM roles, S3 permissions, networking) are provisioned using Terraform, ensuring a structured and automated deployment.

2. EC2 Instance Configuration: Upon provisioning, GitHub Actions applies configurations, installs dependencies, and sets up Apache Airflow on the server.

3. Airflow DAG Execution: The pipeline is controlled by an Airflow DAG, which defines the sequence of ETL tasks and their dependencies. Tasks are executed based on a predefined schedule or manual trigger.

4. Setup Virtual Environment: A Python virtual environment (`etl-venv`) is created, and all required dependencies are installed from `requirements.txt`, ensuring an isolated execution environment.

5. Run ETL Tasks: The `etl.py` script executes data extraction, transformation, and loading steps, leveraging Airflow’s task dependencies to ensure a smooth workflow.

6. Scheduled EC2 Start/Stop: The EC2 instance is started and stopped periodically using AWS Lambda and Amazon EventBridge, ensuring resource optimization and cost efficiency.

7. Post Deployment Actions: Temporary files such as `.env` are deleted to maintain security and cleanliness. The pipeline workspace is cleaned, and Airflow logs are collected for analysis.

## Tech Stack
- Python
- SQL
- Apache Airflow
- AWS EC2
- Terraform
- AWS Lambda
- Amazon EventBridge
- GitHub Actions
- AWS S3
- AWS Secrets Manager
- AWS RDS (PostgreSQL Engine)
- Docker (for local development and testing)

## Clone the Repository

```bash
git clone https://github.com/jibbs1703/Economic-Indicator-Data-Pipeline.git
cd Economic-Indicator-Data-Pipeline
```

```bash
docker compose up airflow-init
```

```bash
docker compose up
```