# Highly Available AWS Feedback Application with Hybrid Architecture and CI/CD Pipeline

A scalable, highly available web application built on AWS that combines server-based and serverless architectures to collect user feedback with image attachments. The application features automated deployment through CI/CD pipelines and implements enterprise-level high availability patterns.

## 🏗️ Architecture Overview

This project demonstrates a hybrid cloud architecture pattern that combines:
- **Traditional Infrastructure**: EC2 instances with Auto Scaling Groups and Application Load Balancer
- **Serverless Components**: Lambda functions, API Gateway, and DynamoDB
- **Storage Solutions**: S3 for image storage
- **DevOps Pipeline**: Complete CI/CD using AWS developer tools

## 🚀 Features

- **High Availability**: Multi-AZ deployment with auto-scaling capabilities
- **Hybrid Architecture**: Combines EC2-based web servers with serverless backend processing
- **Image Upload**: Secure image storage in S3 with base64 encoding
- **Data Persistence**: Form data stored in DynamoDB with unique identifiers
- **Automated Deployment**: Complete CI/CD pipeline from code commit to production
- **Network Security**: Custom VPC with public/private subnet architecture
- **Health Monitoring**: SNS notifications for scaling events and health checks

## 🏛️ Architecture Diagram


<img width="1205" height="1158" alt="image" src="https://github.com/user-attachments/assets/915eafc0-bdd4-47fb-a440-c49e457cae93" />


- **Frontend**: Static web application hosted on EC2 instances
- **Load Balancing**: Application Load Balancer for high availability
- **Backend API**: Serverless API using API Gateway and Lambda
- **Data Layer**: DynamoDB for structured data, S3 for image storage

## 🛠️ Technology Stack

### AWS Services Used:
- **Compute**: EC2, Lambda, Auto Scaling Groups
- **Networking**: VPC, Application Load Balancer, NAT Gateway
- **Storage**: S3, DynamoDB
- **API**: API Gateway
- **DevOps**: CodeCommit, CodeDeploy, CodePipeline, CloudShell
- **Monitoring**: SNS, CloudWatch
- **Security**: IAM roles, Security Groups

### Development Tools:
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python 3.9 (Lambda runtime)
- **Version Control**: Git with AWS CodeCommit
- **Deployment**: AWS CodePipeline

## 📋 Prerequisites

- AWS Account with appropriate permissions
- Basic knowledge of AWS services
- Understanding of networking concepts (VPC, subnets, routing)
- Familiarity with Git version control

## 📈 Monitoring & Alerts

- **CloudWatch Metrics**: CPU utilization, request counts, error rates
- **SNS Notifications**: Auto Scaling events, deployment status
- **Health Checks**: Application Load Balancer health monitoring
- **Logging**: Lambda function logs, EC2 system logs

## 🔒 Security Considerations

- **Network Security**: Custom VPC with isolated private subnets
- **Access Control**: IAM roles with least privilege principles
- **Data Security**: Encrypted data transmission, secure S3 bucket policies
- **API Security**: API Gateway with proper CORS configuration

## 💰 Cost Optimization

- **Compute**: t2.micro instances for cost-effective hosting
- **Serverless**: Pay-per-request Lambda pricing
- **Storage**: S3 Standard for frequently accessed images
- **Auto Scaling**: Automatic capacity adjustment to optimize costs


## 📝 Lessons Learned

1. **Hybrid Architecture Benefits**: Combines reliability of traditional infrastructure with serverless cost-efficiency
2. **CI/CD Importance**: Automated pipelines reduce deployment time by 80%
3. **High Availability Design**: Multi-AZ deployment ensures business continuity
4. **Security Best Practices**: Proper network segmentation and IAM policies are crucial

