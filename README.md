
## 1. Asynchronous Producer–Consumer Pipeline
## Question
Producers fetch data asynchronously and consumers transform and save it.

How would you use:
- Backpressure  
- Multiple producers and consumers



## 2. Report Generation from S3 Files

### Problem Statement
You have 12 data files stored in Amazon S3.  
The goal is to:
- Download each file
- Calculate statistics (row count, missing values)
- Generate individual reports
- Create a master summary
- Upload all reports back to S3

