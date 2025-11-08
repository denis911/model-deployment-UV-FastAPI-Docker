# Machine Learning Model Deployment with UV, FastAPI, and Docker

A production-ready template for deploying a lead conversion prediction model as a REST API using UV, FastAPI, and Docker.

## 🎯 Project Overview

This project demonstrates how to containerize and serve a machine learning model that predicts lead conversion probability. It uses modern, high-performance Python tools to create an efficient and scalable inference service.

- **Model**: Predicts the probability of a lead converting based on their source, courses viewed, and annual income.
- **API**: A FastAPI application provides a `/predict` endpoint to get predictions from the model.
- **Deployment**: The application is containerized using Docker for consistent and reproducible deployments.

## 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| **UV** | Ultra-fast Python package management |
| **FastAPI** | High-performance web framework for the API |
| **Docker** | Containerization for consistent deployment |
| **Pydantic** | Data validation for API requests and responses |
| **Uvicorn** | High-performance ASGI server |

## 📦 Prerequisites

- **Python 3.10+**
- **Docker**
- **Git**
- **UV** (Python package manager)

To install UV:
```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 📁 Project Structure

```
model-deployment-UV-FastAPI-Docker/
│
├── Dockerfile               # Instructions for building the Docker container
├── pyproject.toml           # Project metadata and dependencies
├── uv.lock                  # Locked versions of dependencies
├── predict.py               # FastAPI script for local development (churn model)
├── predict_hw5.py           # FastAPI script for Docker deployment (lead conversion model)
├── model.bin                # Churn prediction model
├── pipeline_v1.bin          # Lead conversion prediction model
└── README.md                # This file
```

## 🔧 Installation and Local Development

This setup is for running the **customer churn** model found in `predict.py`.

```bash
# 1. Clone the repository
git clone https://github.com/denis911/model-deployment-UV-FastAPI-Docker.git
cd model-deployment-UV-FastAPI-Docker

# 2. Create a virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
```

## 🎮 Usage

### Running the Local Server

This will run the `predict.py` (churn prediction) application.

```bash
uvicorn predict:app --reload --host 0.0.0.0 --port 9696
```

The server will be available at `http://localhost:9696`.

### API Documentation

FastAPI provides interactive API documentation:

- **Swagger UI**: `http://localhost:9696/docs`
- **ReDoc**: `http://localhost:9696/redoc`

## 🐳 Docker Deployment

The Docker container runs the **lead conversion** model from `predict_hw5.py`.

### Building the Docker Image

The `Dockerfile` is configured to build an image named `predict-convert`.

```bash
docker build -t predict-convert .
```

### Running the Container

This command runs the container and maps the container's port `9696` to the same port on your local machine.

```bash
docker run -it --rm -p 9696:9696 predict-convert
```

### Making Predictions with Docker

Once the container is running, you can send requests to the `/predict` endpoint.

#### Using cURL

```bash
curl -X POST "http://localhost:9696/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "lead_source": "organic_search",
    "number_of_courses_viewed": 5,
    "annual_income": 80000.0
  }'
```

#### Expected Response

```json
{
  "conversion_probability": 0.85,
  "convert": true
}
```

## 🤝 Acknowledgments

This project is based on the [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) by DataTalks.Club.

