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

## Running Jupyter Notebook
```bash
jupyter notebook
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

## Running Jupyter Notebook
```bash
jupyter notebook