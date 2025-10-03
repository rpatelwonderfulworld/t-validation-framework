# Architecture Overview
- Ingestion modules per domain (ERP, Finance, HR)
- Validation modules with shared core validator
- Reporting module generates summary JSON
- Docker + Kubernetes used for scaling and orchestration

Components/Technologies involved:

Services / Modules: Inventory Service, Auth Service, Support Service, API Gateway

Messaging / Event Bus: Kafka, RabbitMQ

Orchestration / Scaling: Kubernetes, Docker

ETL / Validation: Python/PySpark scripts for validation

CI/CD: GitHub Actions / Jenkins

Database / Storage: PostgreSQL, Aurora, Redshift, S3

Monitoring / Dashboard: Tableau / QuickSight

Flow:

Users access the API Gateway.

Gateway routes requests to microservices (Inventory, Support, Auth).

Microservices communicate asynchronously using Kafka and RabbitMQ.

Validation pipelines run in Python/PySpark, fetching data from databases and ERP modules.

ETL outputs are stored in PostgreSQL / S3 / Redshift.

Kubernetes orchestrates scaling of microservices and pipelines.

CI/CD pipeline deploys changes automatically.

Dashboards monitor validation results.


inventory-service/
├─ app/
│  ├─ controllers/   <-- REST API endpoints (CRUD)
│  ├─ models/        <-- DB models
│  ├─ services/      <-- business logic
│  └─ repositories/  <-- DB queries
├─ Dockerfile
├─ requirements.txt
└─ main.py           <-- FastAPI app
