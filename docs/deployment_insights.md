# 🚀 Spam Detection System: Deployment Architecture

## 🌐 Deployment Platform Overview
- **Platform**: Railway.app
- **Deployment URL**: [web-production-4569.up.railway.app](https://web-production-4569.up.railway.app)
- **Repository**: [bniladridas/spam-detection-system](https://github.com/bniladridas/spam-detection-system)

## 🔧 Technical Architecture

### Web Framework
- **Primary Framework**: Flask
- **Entry Point**: `app.py`
- **Server**: Gunicorn WSGI HTTP Server

### Containerization Strategy
- **Technology**: Docker
- **Purpose**: Consistent, reproducible deployment environment
- **Key Benefits**:
  1. Isolates application dependencies
  2. Ensures consistent runtime across different environments
  3. Simplifies deployment and scaling

### Deployment Configuration
- **Branch**: `main`
- **Region**: `us-west2`
- **Replicas**: 1
- **Restart Policy**: On failure (max 10 retries)

## 🧠 Machine Learning Components
- **Model**: Multinomial Naive Bayes
- **Feature Extraction**: CountVectorizer
- **Training Data**: `spam_dataset.csv`

## 🔍 Deployment Workflow
1. Docker builds container with Python 3.8
2. Installs system dependencies
3. Copies application code
4. Installs Python requirements
5. Starts Gunicorn with Flask application

## 💡 Key Insights
- Docker does NOT replace Flask
- Docker provides the environment to run Flask
- Gunicorn serves the Flask application
- Entire stack is Python-based, containerized for reliability

## 🚦 Deployment Command
```bash
gunicorn app:app
```
This command tells Gunicorn to run the Flask application defined in `app.py`

---

**Last Updated**: February 4, 2025
**Version**: 1.0.0

---

**Version**: 1.0.0
**Last Updated**: 2025-02-04
