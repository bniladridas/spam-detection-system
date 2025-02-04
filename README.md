# Spam Detection System

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

## License

This project is licensed under the MIT License.