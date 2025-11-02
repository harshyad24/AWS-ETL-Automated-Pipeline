# 🚀 AWS ETL Automated Pipeline
https://github.com/user-attachments/assets/78f7675e-356b-4862-acac-de1a512391ca


An automated **ETL (Extract, Transform, Load)** pipeline built on **AWS Cloud Services** to demonstrate **data deduplication, automation, and monitoring** using **S3, Glue, Lambda, EventBridge, SNS, and CloudWatch**.

---

## 🧩 Overview

This project automates the process of extracting raw data from an **S3 source bucket**, removing duplicates with **AWS Glue**, and loading cleaned data into a **target S3 bucket**. Automation and monitoring are achieved with **Lambda**, **EventBridge**, **SNS**, and **CloudWatch**.

---

## 🏗️ Architecture Diagram



> This diagram shows the flow from **S3 → Lambda → Glue → S3**, including notifications and monitoring.

---

## ⚙️ Workflow

1. Upload a file with raw data to the **source S3 bucket**.
2. **EventBridge** detects the upload and triggers a **Lambda function**.
3. Lambda starts the **Glue ETL job** (`s3-glue-s3.py`).
4. Glue removes duplicates and writes cleaned data to the **target S3 bucket**.
5. On completion/failure:
   - **SNS** sends a notification
   - **CloudWatch Logs** capture detailed execution info

---

## 🧠 AWS Services Used

| Service | Purpose |
|---------|---------|
| Amazon S3 | Stores raw and processed data |
| AWS Glue | Performs ETL and deduplication |
| AWS Lambda | Triggers Glue jobs automatically |
| Amazon EventBridge | Detects events and schedules jobs |
| Amazon SNS | Sends notifications on success/failure |
| Amazon CloudWatch | Logs and monitors pipeline execution |

---

## 🧰 Project Structure

```

AWS-ETL-Automated-Pipeline/
├── README.md
├── LICENSE
├── .gitignore
├── template.yml
├── src/
│   └── lambda_function.py
├── Glue Monitoring/
│   ├── s3-glue-s3.py
│   ├── Glue_Monitoring.png
│   ├── s3-glue-s3_desgin.png
│   └── s3-glue-s3_Status.png
├── docs/
│   └── architecture-diagram.png
└── AWS ETL Automated Pipeline.mp4

````

---

## 🔍 ETL Logic (Deduplication)

The **Glue script** (`s3-glue-s3.py`) performs:

1. Reads raw dataset from the **source S3 bucket**
2. Converts it into a **DynamicFrame**
3. Removes duplicates based on unique keys (like `id` or `email`)
4. Writes cleaned dataset to the **target S3 bucket**

Example snippet:

```python
deduplicated_df = input_df.dropDuplicates(["id"])
deduplicated_df.write.mode("overwrite").parquet(output_path)
````

---

## 🚀 Deployment Guide

### Prerequisites

* AWS Account with permissions for S3, Glue, Lambda, EventBridge, and SNS
* AWS CLI and SAM CLI installed
* Python 3.8+
* IAM roles configured for Glue and Lambda

---

### Step 1: Clone Repo

```bash
git clone https://github.com/harshyad24/AWS-ETL-Automated-Pipeline.git
cd AWS-ETL-Automated-Pipeline
```

### Step 2: Deploy Using SAM

```bash
sam build
sam deploy --guided
```

### Step 3: Configure Resources

* Set **source/target S3 bucket names** in `template.yml`
* Verify **IAM roles** have access to S3 and Glue

### Step 4: Upload a Sample File

```bash
aws s3 cp sample-data.csv s3://my-source-bucket/input/
```

### Step 5: Observe Automation

* EventBridge triggers Lambda
* Lambda starts Glue job
* Cleaned data written to target S3 bucket
* Notifications sent via SNS

---

## 📊 Monitoring

| Service      | Details                                          |
| ------------ | ------------------------------------------------ |
| CloudWatch   | Logs for Lambda and Glue job executions          |
| Glue Console | Job status and history                           |
| SNS          | Email/SMS notifications on completion or failure |

---

## 🧩 Example Use Cases

* Automated cleaning of daily sales or sensor data
* Maintain clean datasets for analytics
* Build a serverless ETL layer in AWS

---

## 🪄 Future Enhancements

* Add **Glue Data Quality rules** for profiling
* Integrate **Step Functions** for multi-stage workflows
* Send metrics to **Amazon QuickSight or Power BI**
* Implement CI/CD with GitHub Actions

---

## 🔐 Security Notes

* Do **NOT** store AWS credentials in code
* Use **IAM roles** and environment variables
* `.gitignore` prevents committing sensitive files

---

## 👤 Author

**Harsh Yadav**

[GitHub](https://github.com/harshyad24) | [LinkedIn](https://www.linkedin.com/in/harshyadav577/)

---

## 🏁 License

This project is licensed under the **MIT License** — free to use and modify.

```

---

This README:  
- **Includes your asset image** via the GitHub URL  
- Fully documents **architecture, workflow, deployment, ETL logic, monitoring, and structure**  
- Is **GitHub-ready**  

---

If you want, I can also **add all your images from `Glue Monitoring` and `src/`** inline in the README so they appear directly under each section — making it **visually complete** on GitHub.  

Do you want me to do that?
```
