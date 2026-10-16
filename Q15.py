"""
PRACTICAL 15: Pretrained Sentiment Analysis with Hugging Face Transformers
[UNIT 4: Introduction to Large Language Models and Big Data Applications]

Problem Statement:
Write a Python program to perform Sentiment Analysis using the Hugging Face Transformers library. Initialize a pretrained sentiment-analysis pipeline (pipeline('sentiment-analysis')), classify multiple user review statements into POSITIVE or NEGATIVE sentiment labels, and display the confidence prediction scores.

Expected Reference Output:
--- PREDICTED SENTIMENT SCORES ---
Review 1: 'PySpark makes distributed computing on massive datasets incredibly fast and enjoyable!'
Result   : [POSITIVE] with 99.98% confidence

Review 2: 'The dataset had too many corrupted records and missing values, causing the training to crash.'
Result   : [NEGATIVE] with 99.85% confidence

Review 3: 'Transformers and Large Language Models are revolutionizing artificial intelligence.'
Result   : [POSITIVE] with 99.96% confidence

Review 4: 'The data engineering pipeline was slow and poorly documented.'
Result   : [NEGATIVE] with 99.91% confidence
"""

import os
import warnings

# Suppress background TensorFlow/Keras and Hugging Face logging warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
warnings.filterwarnings("ignore")

from transformers import pipeline, logging as hf_logging
hf_logging.set_verbosity_error()

# Step 1: Initialize pretrained Hugging Face Sentiment Analysis Pipeline
print("Loading Hugging Face sentiment-analysis pipeline...")
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", framework="pt")

# Step 2: Define sample product & service customer reviews
reviews = [
    "PySpark makes distributed computing on massive datasets incredibly fast and enjoyable!",
    "The dataset had too many corrupted records and missing values, causing the training to crash.",
    "Transformers and Large Language Models are revolutionizing artificial intelligence.",
    "The data engineering pipeline was slow and poorly documented."
]

# Step 3: Run inference and display results
print("\n--- PREDICTED SENTIMENT SCORES ---")
for i, review in enumerate(reviews, 1):
    result = classifier(review)[0]
    label = result['label']
    score = result['score'] * 100
    print(f"Review {i}: '{review}'")
    print(f"Result   : [{label}] with {score:.2f}% confidence\n")
