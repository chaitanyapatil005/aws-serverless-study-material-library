# ☁️ Automated Serverless Study Material Library Using AWS

A serverless, event-driven cloud application that automates the publishing of study materials using AWS services. The system enables teachers to upload documents and makes published resources accessible through a static website, with access control and execution monitoring.

## 📌 Project Overview

Managing and distributing study materials manually can be time-consuming. This project implements an AWS-based serverless solution that automates document publishing and provides a centralized platform for students to access learning resources.

The application uses Amazon S3 for storage, AWS Lambda for event-driven processing, AWS IAM for access control, and Amazon CloudWatch for execution monitoring.

## 🎯 Objectives

- Automate the publishing of uploaded study materials.
- Use event-driven processing to eliminate manual publishing steps.
- Maintain a JSON index of published documents.
- Separate private uploads from publicly accessible website content.
- Apply role-based access permissions for teachers and students.
- Monitor Lambda execution using CloudWatch logs.
- Host a static website for accessing published study materials.

## 🏗️ System Architecture

The application follows a serverless architecture using managed AWS services.

```text
             TEACHER
                 |
                 | Upload study document
                 v
      +------------------------+
      | Private Amazon S3      |
      | Upload Bucket          |
      +------------------------+
                 |
                 | S3 Object-Created Event
                 v
      +------------------------+
      | AWS Lambda             |
      | library-publisher      |
      | Python + Boto3         |
      +------------------------+
                 |
          +------+------+
          |             |
          v             v
  +---------------+  +----------------+
  | Website S3    |  | Amazon         |
  | Bucket        |  | CloudWatch     |
  |               |  | Execution Logs |
  +---------------+  +----------------+
          |
          | Published files and JSON index
          v
  +------------------------+
  | Static Study Material  |
  | Website                |
  +------------------------+
                 |
                 v
              STUDENTS

      AWS IAM: Access permissions
      for authorized identities
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Amazon S3 | Stores uploaded documents and hosts website files |
| AWS Lambda | Executes document-publishing logic |
| AWS IAM | Controls identities, permissions, and access |
| Amazon CloudWatch | Records Lambda execution logs |
| Python | Implements the Lambda function |
| Boto3 | Python SDK used to interact with AWS services |
| HTML | Structures the website |
| CSS | Styles the website |
| JavaScript | Supports website-side functionality |
| JSON | Maintains the published-document index |

**AWS Region:** Asia Pacific (Mumbai) — `ap-south-1`

## ⚙️ How the Project Works

### 1. Document Upload

A teacher uploads a study document to the private Amazon S3 upload bucket. The bucket acts as the initial storage location for incoming documents.

### 2. Event Trigger

Amazon S3 generates an object-creation event when a supported upload occurs. This event invokes the configured AWS Lambda function.

### 3. Serverless Processing

The `library-publisher` Lambda function runs Python code using Boto3 to process the S3 event and handle the publishing workflow.

### 4. Document Publishing

The Lambda function copies the uploaded document to the website bucket so that it can be accessed through the published website.

### 5. JSON Index Update

The publishing function updates the JSON index containing information used by the website to list available study materials.

### 6. Student Access

Students access the published resources through the static website without needing direct access to the private upload bucket.

### 7. Monitoring and Logging

Amazon CloudWatch collects Lambda execution logs. The project report records messages such as `S3 event received` and `Published: <file name>`.

## 🔐 Security and Access Control

AWS IAM is used to manage access according to the user's role.

- **Teacher:** Authorized to upload study materials.
- **Student:** Given restricted permissions appropriate to student access.
- **Private upload bucket:** Separates incoming files from published website content.
- **Lambda permissions:** The function requires suitable permissions to read uploaded objects, publish files, and update the index.
- **Access validation:** The report documents an unsuccessful student delete attempt that returned `Access Denied`.

Permissions should follow the principle of least privilege, granting only the actions required by each role.

> Note: Public website access should be limited to the intended published content. The upload bucket and AWS credentials must remain protected.

## 📊 AWS CloudWatch Monitoring

Amazon CloudWatch provides visibility into Lambda execution.

**Configured log group:**

`/aws/lambda/library-publisher`

The report includes log messages that help confirm event receipt and document publishing. It also records a Lambda invocation duration of **428.37 ms** for the displayed execution.

This monitoring helps with troubleshooting and verifying the publishing workflow.

## 🌐 Website Components

The static website uses web technologies to display published study materials.

- `index.html` — main website page.
- CSS — website layout and styling.
- JavaScript — client-side functionality.
- JSON index — data used to list published documents.
- `error.html` — custom error page for HTTP 404 responses.

The website files are hosted separately from the private upload location.

## ✨ Key Features

- Event-driven document publishing.
- Automated copying of uploaded documents.
- Automatic JSON index maintenance.
- Separate upload and website storage locations.
- Role-based access control with IAM.
- Serverless execution using AWS Lambda.
- CloudWatch-based execution logging.
- Static website hosting.
- Custom website error page.

## 🧪 Testing and Validation

The project report documents the following validation activities:

| Test | Expected or recorded outcome |
|---|---|
| Teacher uploads a document | Upload is accepted with the configured permissions |
| S3 object-creation event | Invokes the publishing function |
| Lambda processing | Copies the document and updates the index |
| Student delete attempt | Access denied, as documented in the report |
| CloudWatch logging | Records event and publishing messages |
| Lambda execution duration | 428.37 ms for the displayed invocation |



## 🚀 Deployment Overview

The project uses the following high-level deployment workflow:

1. Create the upload and website S3 buckets.
2. Configure the website files and static website hosting.
3. Create the `library-publisher` Lambda function using Python.
4. Configure the Lambda execution role and required S3 permissions.
5. Configure an S3 object-creation event notification for the upload bucket.
6. Deploy the publishing logic and JSON index update.
7. Configure IAM permissions for teacher and student access.
8. Verify publishing behavior and inspect the CloudWatch logs.

Exact configuration details depend on the deployed bucket names, IAM policies, and Lambda code.

## 📈 Learning Outcomes

Through this project, I explored:

- Serverless cloud application design.
- Event-driven architecture using Amazon S3 and AWS Lambda.
- Cloud storage and static website hosting.
- AWS service integration using Python and Boto3.
- Identity and access management.
- Execution logging and troubleshooting using CloudWatch.
- Automated document publishing and JSON-based website data.

## 🔮 Future Enhancements

- Add user authentication for authorized students and teachers.
- Add document categories, search, and filtering.
- Display document upload dates and file metadata.
- Add notifications for successful or failed publishing.
- Introduce improved error handling and retry mechanisms.
- Add automated testing and deployment using CI/CD.
- Improve the website's mobile responsiveness.
- Add document versioning and audit capabilities.

The repository can also include architecture diagrams, workflow illustrations, and screenshots of the actual AWS implementation.

## 👨‍💻 Skills Demonstrated

`AWS Cloud Computing` · `Serverless Architecture` · `Amazon S3` · `AWS Lambda` · `AWS IAM` · `Amazon CloudWatch` · `Python` · `Boto3` · `Event-Driven Architecture` · `Static Website Hosting` · `HTML` · `CSS` · `JavaScript` · `JSON`

## 👤 Author

**Chaitanya Patil**

Electronics and Telecommunication Engineering

Interested in Embedded Systems, IoT, Cloud Computing, and AWS-based solutions.

- GitHub: [Chaitanya GitHub Profile ](https://github.com/chaitanyapatil005)
- LinkedIn: [Chaitanya LinkedIn Profile](https://www.linkedin.com/in/chaitanya-patil-7a922a30a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Bn2ij6XMwQtuoJJyeXlH3LA%3D%3D)

---

⭐ If you find this project useful, feel free to explore the repository and its documentation.
