# 🚀 Spam Detection System

## 🛠 Technology Stack

### Programming Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

### Machine Learning & Data Science
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white)

### Web Framework
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-298729?style=flat-square&logo=gunicorn&logoColor=white)

### Deployment
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0B0B?style=flat-square&logo=railway&logoColor=white)

### Version Control
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

### Development Tools
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)

## 🔧 Version Control Workflow

### Git Branching Strategy
- **Main Branch**: `main` (primary development branch)
- **Workflow**: Feature-based branching
- **Commit Conventions**: Descriptive, atomic commits

### Key Git Commands Used
```bash
# Clone the repository
git clone https://github.com/bniladridas/spam-detection-system.git

# Create a new feature branch
git checkout -b feature/new-model-improvement

# Stage changes
git add .

# Commit with a descriptive message
git commit -m "Add comprehensive model performance metrics"

# Push to remote repository
git push origin feature/new-model-improvement

# Merge feature branch (via Pull Request)
git checkout main
git merge feature/new-model-improvement
```

### Version Control Best Practices
- Atomic commits
- Descriptive commit messages
- Regular code reviews
- Branch protection rules
- Continuous integration checks

### Repository Insights
![GitHub commits](https://img.shields.io/github/commit-activity/m/bniladridas/spam-detection-system?style=flat-square)
![GitHub last commit](https://img.shields.io/badge/GitHub%20last%20commit-https://img.shields.io/github/last-commit/bniladridas/spam-detection-system?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/bniladridas/spam-detection-system?style=flat-square)

## 📚 Key Libraries Used
- **Data Processing**: NumPy, Pandas
- **Machine Learning**: scikit-learn (MultinomialNB)
- **Web**: Flask, Gunicorn
- **Visualization**: Matplotlib
- **Logging**: Python logging module
- **Serialization**: joblib

## 🔗 Quick Links
- **Live Demo**: [Spam Detection Web App](https://web-production-4569.up.railway.app)
- **Repository**: [GitHub Project](https://github.com/bniladridas/spam-detection-system)

## 🌐 LinkedIn Showcase

### Project Announcement Post

[![LinkedIn Post](https://img.shields.io/badge/View%20LinkedIn%20Post-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/posts/niladridas_revolutionizing-email-security-with-machine-learning-activity-7292445051278786561-share)

**Key Highlights from the Post:**
- 🚀 95% Spam Detection Accuracy
- ⚡ Real-time Email Classification
- 🔬 Machine Learning Innovation
- 🌐 Open-Source Collaboration

*Note: For the full interactive post, please visit the LinkedIn link above.*

## 📝 License
MIT License

## Git Operations

### Clone Repository
```bash
git clone https://github.com/bniladridas/spam-detection-system.git
cd spam-detection-system
```

### Push Changes
```bash
# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to repository
git push origin main
```

## Running with Docker

### Start Server
```bash
docker-compose up --build
```
- Access the application at [http://localhost:5001/](http://localhost:5001/).

### Stop Server
```bash
docker-compose down
```

### View Server Logs
```bash
docker-compose logs spam-detection-app
```

Example Server Logs:
```
spam-detection-app-1  | [2024-02-04 05:28:45 +0000] [1] [INFO] Starting gunicorn 20.1.0
spam-detection-app-1  | [2024-02-04 05:28:45 +0000] [1] [INFO] Listening at: http://0.0.0.0:5001
spam-detection-app-1  | [2024-02-04 05:28:45 +0000] [1] [INFO] Using worker: sync
```

## Running with Flask Backend

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Application
```bash
python app.py
```
- Access the application at [http://127.0.0.1:5001/](http://127.0.0.1:5001/).

## Using the API
Send a POST request to `/predict` with JSON:
```json
{
  "email_text": "Your email content here"
}
```

#### Response Format
```json
{
  "is_spam": true/false,
  "spam_probability": 0-100,
  "message": "Spam detected!" or "Not spam."
}
```

## 🚀 Deployment

### Railway Deployment
For a detailed guide on deploying this project on Railway.app, check out our [Railway Deployment Guide](/docs/railway_deployment_guide.md).

### Live Demo
- **Platform**: Railway
- **URL**: https://web-production-4569.up.railway.app
- **Endpoint**: `/predict`

### Deployment Methods

#### Local Deployment

##### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

##### Installation
1. Clone the repository
```bash
git clone https://github.com/bniladridas/spam-detection-system.git
cd spam-detection-system
```

2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

## Model Details
- **Algorithm**: Multinomial Naive Bayes
- **Features**: Text classification
- **Performance**: 95% accuracy on test dataset

## Project Structure
- `app.py`: Main Flask application
- `spam_dataset.csv`: Training dataset
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration
- `docker-compose.yml`: Docker Compose setup

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to branch
5. Create pull request