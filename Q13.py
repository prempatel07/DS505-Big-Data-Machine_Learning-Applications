"""
PRACTICAL 13: Text Data Cleaning & Custom Tokenization using Python
[UNIT 4: Introduction to Large Language Models and Big Data Applications]

Problem Statement:
Write a Python program to clean raw, noisy text data: convert characters to lowercase using lower(), remove special punctuation symbols using replace(), eliminate redundant whitespace using strip(), and tokenize sentences into individual word tokens using split().

Expected Reference Output:
--- RAW TEXT INPUT ---
'   *** Big Data Handling & Machine Learning with Apache Spark, PySpark & LLMs! Are you Ready???   '

--- CLEANED & NORMALIZED TEXT ---
'big data handling machine learning with apache spark pyspark llms are you ready'

--- EXTRACTED WORD TOKENS ---
Token Count : 12
Tokens List : ['big', 'data', 'handling', 'machine', 'learning', 'with', 'apache', 'spark', 'pyspark', 'llms', 'are', 'you', 'ready']
"""

import string

# Step 1: Raw noisy text string
raw_text = "   *** Big Data Handling & Machine Learning with Apache Spark, PySpark & LLMs! Are you Ready???   "

print("--- RAW TEXT INPUT ---")
print(f"'{raw_text}'")

# Step 2: Text Normalization (Lowercasing & Whitespace Stripping)
cleaned_text = raw_text.strip().lower()

# Step 3: Punctuation Removal using replace / string translation
punctuation_marks = string.punctuation
for char in punctuation_marks:
    cleaned_text = cleaned_text.replace(char, " ")

# Step 4: Normalize multiple spaces to single space
cleaned_text = " ".join(cleaned_text.split())

print("\n--- CLEANED & NORMALIZED TEXT ---")
print(f"'{cleaned_text}'")

# Step 5: Word Tokenization using split()
tokens = cleaned_text.split()

print("\n--- EXTRACTED WORD TOKENS ---")
print(f"Token Count : {len(tokens)}")
print(f"Tokens List : {tokens}")
