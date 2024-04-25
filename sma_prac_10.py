# -*- coding: utf-8 -*-
"""sma prac 10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1479SbyFx_L8v8nL0wzf2gVAjRQmhmFS3
"""

import csv
import random

# Function to generate random reviews and sentiments
def generate_random_review():
    sentiments = ['positive', 'negative', 'neutral']
    review = f"This is a {random.choice(sentiments)} review."
    return review, random.choice(sentiments)

# Create a CSV file with headers 'text' and 'label'
with open('sample_reviews.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['text', 'label'])

    # Generate 25 rows of random reviews
    for _ in range(25):
        review, sentiment = generate_random_review()
        writer.writerow([review, sentiment])

print("CSV file 'sample_reviews.csv' generated successfully.")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline

# Assuming you have a dataset with columns 'text' and 'label' (positive, negative, neutral)
# You may need to adjust this based on your actual dataset structure.

# Load your dataset
df = pd.read_csv('sample_reviews.csv')

# Split the dataset into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Create a pipeline with TF-IDF vectorizer and Naive Bayes classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(train_data['text'], train_data['label'])

# Make predictions on the test set
predictions = model.predict(test_data['text'])

# Evaluate the model
accuracy = accuracy_score(test_data['label'], predictions)
print(f'Accuracy: {accuracy:.2f}')

# Display classification report
print('\nClassification Report:')
print(classification_report(test_data['label'], predictions))