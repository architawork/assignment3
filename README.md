
## 1. Asynchronous Producer–Consumer Pipeline
## Question
Producers fetch data asynchronously and consumers transform and save it.

How would you use:
- Backpressure  
- Multiple producers and consumers

## Answer
Backpressure is handled by setting a maximum size on the queue, so producers automatically wait when the queue is full and consumers wait when the queue is empty. Multiple producers and consumers can run at the same time, allowing data to be fetched and processed in parallel.


## 2. Report Generation from S3 Files

### Problem Statement
You have 12 data files stored in Amazon S3.  
The goal is to:
- Download each file
- Calculate statistics (row count, missing values)
- Generate individual reports
- Create a master summary
- Upload all reports back to S3

## Answer
File conflicts are avoided by processing each file separately and using unique file names or folders. Files of different sizes are handled by processing them in parallel and streaming or chunking large files instead of loading them fully into memory.


