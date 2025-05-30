# 🚗 Real-Time Data Streaming Using Kafka and AWS  
### For a Logistics Company Operating Between Konstanz and Stuttgart, Germany

This project demonstrates a real-time data streaming pipeline using **Apache Kafka** and **AWS**, tailored for a logistics company operating in Germany. It simulates vehicle telemetry data between **Konstanz** and **Stuttgart** using Kafka topics. Docker is used to manage the Kafka environment, while Kafka CLI tools are used to interact with the data streams.

---

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- Docker container running a Kafka broker (e.g., `kafka-broker`)
- Kafka CLI tools (usually included in Kafka Docker images)

---

## 🐳 Step 1: Access the Kafka Broker Container

Open a terminal and enter the Kafka container shell:

```bash
docker exec -it kafka-broker bash


