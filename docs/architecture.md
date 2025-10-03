# Architecture Overview
- Ingestion modules per domain (ERP, Finance, HR)
- Validation modules with shared core validator
- Reporting module generates summary JSON
- Docker + Kubernetes used for scaling and orchestration