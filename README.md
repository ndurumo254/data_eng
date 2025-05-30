# 🚚 Real-Time Data Pipeline Using Kafka, Spark & AWS  
### For a Logistics Company Operating Between Konstanz and Stuttgart, Germany

This project demonstrates a real-time data pipeline using **Apache Kafka**, **Apache Spark**, and **AWS Cloud** services. It simulates vehicle telemetry data (e.g., GPS coordinates, speed, timestamp) for a logistics company operating in Germany. The data flows through Kafka for ingestion, Spark for processing, and AWS for storage and analytics.

---

## 💻 Operating System

This project is developed and tested on:

- **Linux Ubuntu 24.04 LTS**

> ✅ All commands and installation steps in this guide are tailored for Ubuntu 24.04 users.

---
- ## Data pipeline structure

![alt text](data_pipeline.png)

## 🔧 Technologies Used

- **Apache Kafka** – Real-time streaming platform for ingesting vehicle data  
- **Apache Spark** – Stream processing engine for data transformation and analytics  
- **AWS Services** – Cloud-based storage (S3), data warehousing (Redshift), and visualization (QuickSight)  
- **Docker** – For containerized deployment of Kafka and Zookeeper  
- **Python** – For simulating vehicle data producers  

---


## 🛠️ Prerequisites

Make sure you have the following installed:

- Docker: [Install Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- Docker Compose (optional, for multi-container setup)
- Apache Kafka CLI (included in most Kafka Docker containers)
- AWS CLI (configured with your credentials)
- Java (for Spark)
- Python 3 (for vehicle data simulation)

---

## 🐳 Step 1: Access Kafka Broker in Docker

Start your Kafka container, then access it:

```bash
docker exec -it kafka-broker bash
 List of brokers

Consume Messages from a Topic

kafka-topics --bootstrap-server localhost:9092 --list
[appuser@b0d3b9da8cb8 ~]$ kafka-topics --bootstrap-server localhost:9092 --list
emergency_alerts
gps_data
vehicle_data
weather_data


Consume Messages from a Topic

kafka-console-consumer --bootstrap-server localhost:9092 --topic vehicle_data --from-beginning
