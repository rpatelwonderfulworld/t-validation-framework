# T ERP Validation Framework

## Overview
This project is a **T-style ERP Data Validation Framework** designed to simulate ingestion, validation, and reporting of data from multiple modules: **ERP, Finance, and HR**.  
It demonstrates **modular design, automated validation, and scaling using Docker and Kubernetes**, suitable for enterprise-scale data pipelines.

---

## Project Structure
t-validation-framework/
│── README.md
│── docker-compose.yml
│── requirements.txt
│
├── docs/
│ ├── architecture.md # System design & flow diagrams
│ └── validation_rules.md # Sample rules per module
│
├── ingestion/
│ ├── load_erp.py # ERP data ingestion simulation
│ ├── load_finance.py # Finance data ingestion simulation
│ └── load_hr.py # HR data ingestion simulation
│
├── validation/
│ ├── core_validator.py # Shared validation logic
│ ├── erp_validation.py
│ ├── finance_validation.py
│ └── hr_validation.py
│
├── reporting/
│ ├── generate_report.py # Generates summary JSON/CSV
│ └── dashboard_mockup.md # Placeholder for dashboards
│
├── automation/
│ ├── k8s_deploy.yaml # Kubernetes deployment placeholder
│ └── cicd_pipeline.yml # CI/CD pipeline placeholder
│
└── tests/
├── test_ingestion.py
├── test_validation.py
└── test_reporting.py


---
**data validation framework for  ERP modules**
It demonstrates:
ETL pipelines for ERP data
Validation rules for ensuring data quality
Message-driven architecture using Kafka & RabbitMQ
Scaling with Docker + Kubernetes
CI/CD pipeline with unit tests (GitHub Actions)
real-world enterprise data engineering practices

⚡ Features

✅ ERP Data Ingestion (Finance, HR, Inventory)
✅ ETL Pipelines with Python
✅ Data Validation across modules (cross-checks, missing values, duplicates)
✅ Message-driven pipeline with Kafka & RabbitMQ
✅ Docker + Kubernetes scaling for horizontal load management
✅ CI/CD automation with GitHub Actions (unit testing + linting)

tesla-validation-framework/
│── data/                     # Sample CSV input data
│── src/
│   ├── etl/                  # Extract, Transform, Load scripts
│   ├── validation/            # Data validation rules
│   ├── messaging/             # Kafka + RabbitMQ integration
│   │   ├── kafka_producer.py
│   │   ├── kafka_consumer.py
│   │   ├── rabbit_producer.py
│   │   └── rabbit_consumer.py
│   ├── scaling/               # Kubernetes deployment YAMLs
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── utils/                 # DB connector, helper functions
│   └── run_validation.py      # Orchestration script
│── tests/                     # Unit tests for CI/CD
│── docker-compose.yml         # Local multi-service setup
│── requirements.txt           # Python dependencies
│── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD pipeline
│── README.md

## Features

- **Ingestion Modules:** Simulate loading data from ERP, Finance, and HR systems.  
- **Validation Modules:** Modular rules per domain; shared `core_validator.py` enforces consistency.  
- **Reporting:** Generate JSON/CSV reports; placeholder for dashboard visualizations.  
- **Automation & Scaling:**  
  - Docker containers per module.  
  - Kubernetes manifests demonstrate scaling via replicas.  
  - CI/CD pipeline placeholder for automated testing.  
- **Tests:** Pytest-ready tests for ingestion and validation.

---

## Validation Rules (Sample)

- **ERP:** Orders must have positive amounts.  
- **Finance:** Invoice totals must be positive.  
- **HR:** Employee names cannot be null.  

> More rules can be easily added to each module without changing the core framework.

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/tesla-validation-framework.git
cd tesla-validation-framework

