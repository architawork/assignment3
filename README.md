
## 1. Asynchronous Producer–Consumer Pipeline

### Overview
- **Producers** fetch data asynchronously from external sources (e.g., APIs, S3, message queues).
- **Consumers** process, transform, and persist the data (e.g., save to disk, database, or S3).

---

### Architecture


How would you avoid file conflicts? How would you handle files of different sizes?

## 2. Report Generation from S3 Files

### Problem Statement
You have **12 data files stored in Amazon S3**.  
The goal is to:
- Download each file
- Calculate statistics (row count, missing values)
- Generate individual reports
- Create a master summary
- Upload all reports back to S3

