import pandas as pd
import numpy as np
import random
import re
from typing import List, Tuple

class SpamDatasetGenerator:
    def __init__(self, seed: int = 42):
        """
        Initialize dataset generator with configurable randomness
        
        Args:
            seed (int): Random seed for reproducibility
        """
        np.random.seed(seed)
        random.seed(seed)
        
        # Spam-related word collections
        self.spam_keywords = [
            'free', 'winner', 'urgent', 'click', 'limited', 
            'offer', 'prize', 'lottery', 'congratulations', 
            'investment', 'rich', 'million', 'guaranteed'
        ]
        
        self.professional_keywords = [
            'meeting', 'report', 'project', 'strategy', 
            'team', 'proposal', 'quarterly', 'agenda', 
            'review', 'performance', 'client'
        ]
    
    def _generate_spam_email(self) -> str:
        """
        Generate a synthetic spam email
        
        Returns:
            str: Randomly generated spam email
        """
        spam_templates = [
            f"Urgent! {random.choice(self.spam_keywords).capitalize()} offer for you!",
            f"Congratulations! You've won a {random.choice(self.spam_keywords)} prize!",
            f"Limited time {random.choice(self.spam_keywords)} opportunity. Act now!",
            f"Get {random.randint(10000, 1000000)} dollars {random.choice(self.spam_keywords)}!",
            f"Exclusive {random.choice(self.spam_keywords)} investment. Guaranteed returns!"
        ]
        return random.choice(spam_templates)
    
    def _generate_legitimate_email(self) -> str:
        """
        Generate a synthetic legitimate email
        
        Returns:
            str: Randomly generated professional email
        """
        professional_templates = [
            f"{random.choice(self.professional_keywords).capitalize()} scheduled for next week",
            f"{random.choice(self.professional_keywords).capitalize()} review meeting invitation",
            f"Quarterly {random.choice(self.professional_keywords)} report attached",
            f"Team {random.choice(self.professional_keywords)} and discussion points",
            f"Client {random.choice(self.professional_keywords)} update"
        ]
        return random.choice(professional_templates)
    
    def generate_dataset(
        self, 
        total_emails: int = 1000, 
        spam_ratio: float = 0.3
    ) -> pd.DataFrame:
        """
        Generate a synthetic email dataset
        
        Args:
            total_emails (int): Total number of emails to generate
            spam_ratio (float): Proportion of spam emails
        
        Returns:
            pd.DataFrame: Generated dataset with emails and labels
        """
        spam_count = int(total_emails * spam_ratio)
        legitimate_count = total_emails - spam_count
        
        emails = []
        labels = []
        
        # Generate spam emails
        for _ in range(spam_count):
            emails.append(self._generate_spam_email())
            labels.append('spam')
        
        # Generate legitimate emails
        for _ in range(legitimate_count):
            emails.append(self._generate_legitimate_email())
            labels.append('not_spam')
        
        # Create DataFrame
        df = pd.DataFrame({
            'email': emails,
            'label': labels
        })
        
        # Shuffle dataset
        df = df.sample(frac=1).reset_index(drop=True)
        
        return df
    
    def save_dataset(
        self, 
        df: pd.DataFrame, 
        filename: str = 'spam_dataset.csv'
    ) -> None:
        """
        Save generated dataset to CSV
        
        Args:
            df (pd.DataFrame): Dataset to save
            filename (str): Output filename
        """
        df.to_csv(filename, index=False)
        print(f"Dataset saved to {filename}")
        print(f"Total Emails: {len(df)}")
        print(f"Spam Emails: {len(df[df['label'] == 'spam'])}")
        print(f"Legitimate Emails: {len(df[df['label'] == 'not_spam'])}")
    
    def analyze_dataset(self, df: pd.DataFrame) -> None:
        """
        Provide basic dataset analysis
        
        Args:
            df (pd.DataFrame): Dataset to analyze
        """
        print("\n📊 Dataset Analysis:")
        
        # Basic statistics
        print("\nBasic Statistics:")
        print(f"Total Emails: {len(df)}")
        print(f"Spam Emails: {len(df[df['label'] == 'spam'])}")
        print(f"Legitimate Emails: {len(df[df['label'] == 'not_spam'])}")
        
        # Email length analysis
        df['email_length'] = df['email'].apply(len)
        print("\nEmail Length Analysis:")
        print(df.groupby('label')['email_length'].describe())

def main():
    # Create dataset generator
    generator = SpamDatasetGenerator()
    
    # Generate dataset
    dataset = generator.generate_dataset(
        total_emails=10000,  # Adjust as needed
        spam_ratio=0.3
    )
    
    # Save and analyze dataset
    generator.save_dataset(dataset)
    generator.analyze_dataset(dataset)

if __name__ == "__main__":
    main()
