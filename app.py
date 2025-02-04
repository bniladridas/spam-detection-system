import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import logging
import sys
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Determine the absolute path to the dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, 'spam_dataset.csv')

# Load and preprocess dataset
df = pd.read_csv(DATASET_PATH)
X = df['email']
y = df['label']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train Multinomial Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Save model and vectorizer
joblib.dump(model, os.path.join(BASE_DIR, 'spam_detection_model.joblib'))
joblib.dump(vectorizer, os.path.join(BASE_DIR, 'vectorizer.joblib'))

app = Flask(__name__, static_folder=BASE_DIR)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes

@app.route('/')
def serve_index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/predict', methods=['POST'])
def predict_spam():
    try:
        # Get email text from request
        email_text = request.json.get('email_text', '')
        
        # Load saved model and vectorizer
        loaded_model = joblib.load(os.path.join(BASE_DIR, 'spam_detection_model.joblib'))
        loaded_vectorizer = joblib.load(os.path.join(BASE_DIR, 'vectorizer.joblib'))
        
        # Vectorize the input
        email_vectorized = loaded_vectorizer.transform([email_text])
        
        # Predict
        prediction = loaded_model.predict(email_vectorized)
        probability = loaded_model.predict_proba(email_vectorized)[0]
        
        # Prepare response
        result = {
            'is_spam': bool(prediction[0]),
            'spam_probability': float(probability[1]) * 100,
            'message': 'Spam detected!' if prediction[0] == 1 else 'Not spam.'
        }
        
        return jsonify(result)
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# For local development
if __name__ == '__main__':
    port = 5001
    if len(sys.argv) > 1 and sys.argv[1] == '--port':
        port = int(sys.argv[2])
    app.run(debug=True, port=port)
