import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SpamDetector:
    def __init__(self):
        """
        Initialize SpamDetector with key components
        """
        self.vectorizer = CountVectorizer()
        self.classifier = MultinomialNB()
        self.is_trained = False

    def preprocess_text(self, text):
        """
        Preprocess text by converting to lowercase and removing special characters
        
        Args:
            text (str): Input text to preprocess
        
        Returns:
            str: Preprocessed text
        """
        # Convert to lowercase and remove special characters
        preprocessed = re.sub(r'[^a-zA-Z\s]', '', text.lower()).strip()
        return preprocessed

    def train(self, X_train, y_train, verbose=True):
        """
        Train the spam detection model
        
        Args:
            X_train (list): Training email texts
            y_train (list): Corresponding labels
            verbose (bool): Whether to print training details
        
        Returns:
            dict: Training metrics
        """
        # Preprocess training data
        X_processed = [self.preprocess_text(email) for email in X_train]
        
        # Vectorize text
        X_vectorized = self.vectorizer.fit_transform(X_processed)
        
        # Train classifier
        self.classifier.fit(X_vectorized, y_train)
        self.is_trained = True
        
        # Optional: Compute and print training metrics
        if verbose:
            # Split data for validation
            X_train_vec, X_val_vec, y_train_val, y_val = train_test_split(
                X_vectorized, y_train, test_size=0.2, random_state=42
            )
            
            # Predict on validation set
            y_pred = self.classifier.predict(X_val_vec)
            
            # Generate classification report
            report = classification_report(y_val, y_pred, output_dict=True)
            
            logging.info("\n🚀 Training Metrics:")
            logging.info(f"Total Training Samples: {len(X_train)}")
            logging.info(f"Validation Samples: {len(y_val)}")
            logging.info("\nClassification Report:")
            logging.info(f"Accuracy: {report['accuracy']:.2%}")
            logging.info(f"Spam Precision: {report['spam']['precision']:.2%}")
            logging.info(f"Spam Recall: {report['spam']['recall']:.2%}")
            logging.info(f"Not Spam Precision: {report['not_spam']['precision']:.2%}")
            logging.info(f"Not Spam Recall: {report['not_spam']['recall']:.2%}")
        
        return {
            'trained': self.is_trained,
            'total_samples': len(X_train)
        }

    def predict(self, emails, verbose=True):
        """
        Predict spam probability for new emails
        
        Args:
            emails (list): List of email texts to classify
            verbose (bool): Whether to print prediction details
        
        Returns:
            list: Predictions with probabilities
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before prediction")
        
        # Preprocess test emails
        X_processed = [self.preprocess_text(email) for email in emails]
        
        # Vectorize test emails
        X_vectorized = self.vectorizer.transform(X_processed)
        
        # Predict probabilities
        probabilities = self.classifier.predict_proba(X_vectorized)
        
        # Classify emails
        predictions = []
        if verbose:
            logging.info("\n🔍 Prediction Results:")
        
        for email, prob in zip(emails, probabilities[:, 1]):
            if prob > 0.7:
                classification = 'Spam'
            else:
                classification = 'Not Spam'
            
            predictions.append({
                'email': email,
                'classification': classification,
                'spam_probability': prob
            })
            
            if verbose:
                logging.info(f"\nEmail: {email}")
                logging.info(f"Classification: {classification}")
                logging.info(f"Spam Probability: {prob:.2%}")
        
        return predictions

def main():
    """
    Demonstration of SpamDetector training and inference
    """
    # Sample training data
    X_train = [
        'Urgent! You\'ve won a free iPhone. Click here now!',
        'Meeting scheduled for next week. Please confirm.',
        'Limited offer: Get rich quick with this amazing investment!',
        'Hi, can we discuss the project timeline?',
        'CONGRATULATIONS! You are today\'s lucky winner of $10,000!',
        'Special discount for loyal customers',
        'Verify your account immediately',
        'Project report attached for review'
    ]
    y_train = ['spam', 'not_spam', 'spam', 'not_spam', 'spam', 'spam', 'spam', 'not_spam']
    
    # Test emails
    test_emails = [
        'Free money guaranteed! Don\'t miss this opportunity!',
        'Quick project update for the team',
        'Claim your prize now! Huge winnings await!'
    ]
    
    # Initialize and train SpamDetector
    detector = SpamDetector()
    training_result = detector.train(X_train, y_train)
    
    # Perform prediction
    predictions = detector.predict(test_emails)

if __name__ == '__main__':
    main()
