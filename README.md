# Machine Learning Model Deployment with UV, FastAPI, and Docker

A modern, production-ready template for deploying machine learning models as REST APIs using cutting-edge Python tooling. This project demonstrates how to containerize and serve ML models efficiently using UV (ultra-fast package manager), FastAPI (high-performance web framework), and Docker.

## 🎯 Why This Project Matters

In the real world, training a machine learning model is only half the battle. The true value comes from deploying it so others can use it. This project solves several critical challenges that data scientists and ML engineers face daily:

### Real-World Problems This Solves

1. **"It works on my machine" syndrome** - Docker ensures your model runs identically everywhere
2. **Slow dependency installation** - UV reduces Python package installation time by 10-100x compared to pip
3. **Complex API development** - FastAPI provides automatic API documentation and data validation
4. **Production readiness** - Learn industry-standard deployment patterns used by tech companies
5. **Scalability concerns** - Build a foundation that can scale from prototype to production

### Who Should Use This

- **Data Scientists** transitioning from notebooks to production
- **ML Engineers** building scalable inference services
- **Software Engineers** integrating ML models into applications
- **Students** learning modern MLOps practices
- **Startups** needing fast, reliable ML deployment

## 🚀 What You'll Learn

By working through this project, you'll understand:

- How to structure ML projects for production deployment
- Modern Python dependency management with UV
- Building REST APIs with FastAPI for ML inference
- Containerizing applications with Docker
- Best practices for serving ML models at scale
- API documentation and testing workflows

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Docker Deployment](#-docker-deployment)
- [Real-World Use Cases](#-real-world-use-cases)
- [Troubleshooting](#-troubleshooting)
- [Learning Resources](#-learning-resources)

## ✨ Features

- **⚡ Lightning-fast dependency management** with UV (10-100x faster than pip)
- **🚀 High-performance API** built with FastAPI
- **🐳 Production-ready Docker container** with optimized layers
- **📚 Automatic API documentation** (Swagger UI and ReDoc)
- **✅ Data validation** using Pydantic models
- **🔄 Hot reload** for rapid development
- **📦 Minimal Docker image size** using multi-stage builds
- **🛡️ Type safety** throughout the codebase

## 🛠 Technology Stack

### Why These Technologies?

| Technology | Purpose | Why It's Better |
|------------|---------|-----------------|
| **UV** | Package Management | 10-100x faster than pip, written in Rust, resolves dependencies instantly |
| **FastAPI** | Web Framework | Automatic validation, async support, fastest Python framework, built-in docs |
| **Docker** | Containerization | Ensures consistency across environments, easy deployment to cloud platforms |
| **Pydantic** | Data Validation | Type safety, automatic validation, clear error messages |
| **Uvicorn** | ASGI Server | High-performance async server for production use |

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+** - Modern Python for best performance and features
- **Docker** - For containerization (optional but recommended)
- **Git** - For version control

### Installing UV

UV is a revolutionary Python package manager that's dramatically faster than pip:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify installation
uv --version
```

## 📁 Project Structure

```
model-deployment-UV-FastAPI-Docker/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── models.py            # Pydantic data models
│   └── ml_model/
│       ├── __init__.py
│       └── model.pkl        # Trained ML model
│
├── Dockerfile               # Multi-stage Docker build
├── pyproject.toml          # UV project configuration
├── uv.lock                 # Locked dependencies
├── .dockerignore           # Files to exclude from Docker
└── README.md               # This file
```

### Key Files Explained

- **`main.py`** - Entry point for the FastAPI application, defines API endpoints
- **`models.py`** - Pydantic schemas for request/response validation
- **`Dockerfile`** - Instructions for building the Docker container
- **`pyproject.toml`** - Project metadata and dependencies (UV's equivalent to requirements.txt)
- **`uv.lock`** - Exact versions of all dependencies for reproducibility

## 🔧 Installation

### Option 1: Local Development with UV (Recommended)

```bash
# Clone the repository
git clone https://github.com/denis911/model-deployment-UV-FastAPI-Docker.git
cd model-deployment-UV-FastAPI-Docker

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies (this is blazingly fast!)
uv pip install -e .

# Or use uv sync for locked dependencies
uv sync
```

### Option 2: Traditional pip Installation

```bash
# If you prefer using pip
pip install -r requirements.txt  # If requirements.txt exists
# Or
pip install fastapi uvicorn scikit-learn pandas numpy
```

## 🎮 Usage

### Running Locally

Start the development server with hot reload:

```bash
# Using UV (recommended)
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or if using traditional activation
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The server will start at `http://localhost:8000`

### Making Predictions

Once the server is running, you can make predictions via HTTP requests:

#### Using cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "feature1": 5.1,
    "feature2": 3.5,
    "feature3": 1.4,
    "feature4": 0.2
  }'
```

#### Using Python

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "feature1": 5.1,
    "feature2": 3.5,
    "feature3": 1.4,
    "feature4": 0.2
}

response = requests.post(url, json=data)
print(response.json())
```

#### Using the Interactive Docs

Navigate to `http://localhost:8000/docs` for the Swagger UI where you can:
- See all available endpoints
- Test API calls directly in your browser
- View request/response schemas
- See example payloads

## 📖 API Documentation

FastAPI automatically generates beautiful, interactive documentation:

- **Swagger UI** - `http://localhost:8000/docs`
- **ReDoc** - `http://localhost:8000/redoc`
- **OpenAPI JSON** - `http://localhost:8000/openapi.json`

### Available Endpoints

#### `GET /`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "message": "ML Model API is running"
}
```

#### `POST /predict`
Make predictions using the trained model.

**Request Body:**
```json
{
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2
}
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.95,
  "model_version": "1.0.0"
}
```

#### `GET /model-info`
Get information about the deployed model.

**Response:**
```json
{
  "model_type": "RandomForestClassifier",
  "version": "1.0.0",
  "features": ["feature1", "feature2", "feature3", "feature4"],
  "trained_date": "2024-01-15"
}
```

## 🐳 Docker Deployment

Docker containerization ensures your application runs identically across all environments.

### Building the Docker Image

```bash
# Build the image
docker build -t ml-model-api:latest .

# Verify the image was created
docker images | grep ml-model-api
```

### Running the Container

```bash
# Run the container
docker run -d \
  --name ml-api \
  -p 8000:8000 \
  ml-model-api:latest

# Check if it's running
docker ps

# View logs
docker logs ml-api

# Stop the container
docker stop ml-api

# Remove the container
docker rm ml-api
```

### Docker Compose (Alternative)

For more complex setups, create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MODEL_VERSION=1.0.0
      - LOG_LEVEL=info
    restart: unless-stopped
```

Then run:
```bash
docker-compose up -d
```

### Optimizing Docker Images

The Dockerfile uses multi-stage builds to minimize image size:

1. **Builder stage** - Installs UV and dependencies
2. **Runtime stage** - Copies only necessary files
3. **Result** - Smaller, more secure production image

## 🌍 Real-World Use Cases

This deployment pattern is used in production by companies worldwide:

### 1. E-commerce Product Recommendations
**Scenario:** An online store needs real-time product recommendations.

**How this helps:**
- FastAPI handles thousands of requests per second
- Docker ensures consistent predictions across regions
- Easy to scale horizontally with Kubernetes

### 2. Financial Fraud Detection
**Scenario:** Banks need to score transactions for fraud in milliseconds.

**How this helps:**
- Low-latency API responses (< 50ms)
- Docker enables deployment in secure, isolated environments
- Easy to update models without downtime

### 3. Medical Diagnosis Assistance
**Scenario:** Healthcare apps need to run ML models for patient data analysis.

**How this helps:**
- Data validation ensures only correct inputs reach the model
- API documentation helps medical teams integrate safely
- Containerization ensures HIPAA-compliant deployment

### 4. Manufacturing Quality Control
**Scenario:** Factories need real-time defect detection from camera images.

**How this helps:**
- Edge deployment with Docker on factory hardware
- Fast inference for real-time assembly line monitoring
- Version control of models across multiple facilities

### 5. Content Moderation
**Scenario:** Social platforms need to classify content automatically.

**How this helps:**
- Async processing for high throughput
- Easy A/B testing of different models
- Scalable across data centers worldwide

## 🔧 Customizing for Your Model

To adapt this template for your own ML model:

1. **Replace the model file:**
   ```python
   # In app/ml_model/model.pkl
   import joblib
   joblib.dump(your_trained_model, 'app/ml_model/model.pkl')
   ```

2. **Update the Pydantic models:**
   ```python
   # In app/models.py
   class PredictionInput(BaseModel):
       your_feature1: float
       your_feature2: str
       # Add your features here
   ```

3. **Modify the prediction logic:**
   ```python
   # In app/main.py
   @app.post("/predict")
   async def predict(data: PredictionInput):
       # Your preprocessing logic
       features = prepare_features(data)
       prediction = model.predict(features)
       return {"prediction": prediction}
   ```

4. **Update dependencies:**
   ```bash
   uv add numpy pandas scikit-learn
   # Or whatever packages your model needs
   ```

## 🐛 Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Error: Address already in use
# Solution: Use a different port or kill the process
lsof -ti:8000 | xargs kill -9
# Then restart on a different port
uvicorn app.main:app --port 8001
```

#### Docker Build Fails
```bash
# Clear Docker cache and rebuild
docker system prune -a
docker build --no-cache -t ml-model-api:latest .
```

#### Model File Not Found
```bash
# Ensure the model file is in the correct location
ls app/ml_model/model.pkl

# Check your .dockerignore isn't excluding it
cat .dockerignore
```

#### Slow Predictions
- Consider using async processing for I/O-bound operations
- Profile your preprocessing code
- Use model quantization or optimization techniques
- Add caching for repeated requests

#### Memory Issues in Docker
```bash
# Increase Docker memory allocation
# Docker Desktop → Settings → Resources → Memory
# Or run with memory limits
docker run -m 2g ml-model-api:latest
```

## 📚 Learning Resources

### Recommended Reading

- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Official FastAPI docs
- [UV Documentation](https://docs.astral.sh/uv/) - Learn about UV package manager
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/) - Docker optimization
- [ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) - Original workshop materials

### Next Steps

1. **Add authentication** - Protect your API with API keys or OAuth
2. **Implement monitoring** - Add Prometheus metrics and logging
3. **Set up CI/CD** - Automate testing and deployment with GitHub Actions
4. **Deploy to cloud** - Try AWS ECS, Google Cloud Run, or Azure Container Instances
5. **Add caching** - Use Redis to cache frequent predictions
6. **Implement rate limiting** - Protect against abuse
7. **Add batch processing** - Handle multiple predictions at once

### Community

- **DataTalks.Club** - Join the Slack community for ML engineering discussions
- **FastAPI Discord** - Get help with FastAPI-specific questions
- **ML in Production** - Follow best practices from the industry

## 🤝 Acknowledgments

This project is based on the [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) Workshop 5 by DataTalks.Club. Special thanks to Alexey Grigorev and the DataTalks.Club community for creating excellent free educational content.

---

*Last updated: October 2025*
