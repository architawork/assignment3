# Async Data Pipeline & Report Generation

This repository demonstrates:
1. An asynchronous producer–consumer data pipeline
2. A report generation workflow using files stored in Amazon S3

---

## 1. Asynchronous Producer–Consumer Pipeline

### Overview
- **Producers** fetch data asynchronously from external sources (e.g., APIs, S3, message queues).
- **Consumers** process, transform, and persist the data (e.g., save to disk, database, or S3).

---

### Architecture


How would you avoid file conflicts? How would you handle files of different sizes?
