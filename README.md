Markdown

# Bank Marketing Prediction API 🏦

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7?logo=render&logoColor=white)

## 📋 Project Overview

This project is an **End-to-End Machine Learning solution** designed to predict whether a bank client will subscribe to a term deposit.

Unlike standard data science notebooks, this project takes the model out of the research environment and deploys it as a production-ready **REST API** using **FastAPI** and **Docker**. It demonstrates the complete MLOps lifecycle: from data training to cloud deployment.

### 🚀 Live Demo
The API is deployed and accessible publicly. You can test the interactive documentation (Swagger UI) here:

👉 **[PEGAR TU LINK DE RENDER AQUÍ]**

*(Note: The service is hosted on a free tier, so it might take 30-50 seconds to wake up on the first request).*

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Data Processing:** Pandas, Numpy, Scikit-Learn Pipelines
* **API Framework:** FastAPI
* **Data Validation:** Pydantic
* **Containerization:** Docker
* **Cloud Deployment:** Render

---

## 📂 Project Structure

```text
├── app.py                # Main application file (FastAPI endpoints)
├── bank_pipeline.pkl     # Serialized trained model (Scikit-learn Pipeline)
├── Dockerfile            # Instructions to build the Docker image
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
⚙️ How to Run Locally
You can run this project on your local machine using Docker (recommended) or Python directly.

Option A: Using Docker
Bash

# 1. Build the image
docker build -t bank-api .

# 2. Run the container
docker run -p 80:80 bank-api
Option B: Using Python
Bash

# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the server
uvicorn app:app --reload
Access the API at http://localhost:80/docs.

📡 API Usage
Endpoint: POST /predict
Receives client data and returns the prediction result.

Input Example (JSON):

JSON

{
  "age": 45,
  "duration": 350,
  "campaign": 1,
  "pdays": -1,
  "previous": 0,
  "job": "management",
  "marital": "married",
  "education": "university.degree",
  "default": "no",
  "housing": "yes",
  "loan": "no",
  "contact": "cellular",
  "month": "may",
  "day_of_week": "mon",
  "poutcome": "unknown"
}

Output Example (JSON):
{
  "prediction": 0,
  "outcome": "NOT_SUBSCRIBED",
  "confidence_score": [0.88, 0.12]
}

Carlos Barrios: Mathematician | University Professor | Data Scientist

LinkedIn: https://www.linkedin.com/in/carlos-barrios-matematicas-fisica-machinelearning/
GitHub: https://github.com/Carlosmaths
