"""
PRACTICAL 14: Vocabulary Frequency Profiling & Stopword Filtering
[UNIT 4: Introduction to Large Language Models and Big Data Applications]

Problem Statement:
Write a Python program to profile vocabulary in a text corpus: clean sentences, filter out common English stopwords (e.g., 'the', 'is', 'in', 'and'), calculate word occurrence frequencies using collections.Counter, and display the top 5 most frequent keywords.

Expected Reference Output:
--- VOCABULARY FREQUENCY ANALYSIS ---
Total Raw Words         : 42
After Stopword Removal  : 31
Total Unique Vocabulary : 20

--- TOP 5 MOST FREQUENT KEYWORDS ---
Keyword: data            | Frequency: 4
Keyword: big             | Frequency: 3
Keyword: apache          | Frequency: 1
Keyword: spark           | Frequency: 1
Keyword: distributed     | Frequency: 1
"""

from collections import Counter

# Step 1: Text Corpus
corpus = """
Big data refers to massive volumes of structured and unstructured data.
Apache Spark is a distributed computing system designed for big data processing.
Machine learning models learn patterns from large scale big data.
Natural language processing and transformers enable intelligent understanding of text data.
"""

# Step 2: Define basic English stop words list
stopwords = {'to', 'of', 'and', 'a', 'is', 'for', 'from', 'in'}

# Step 3: Clean and tokenize corpus
words = corpus.lower().replace('.', '').replace(',', '').split()

# Step 4: Filter out stop words
filtered_words = [w for w in words if w not in stopwords]

# Step 5: Count word frequencies
frequency_counter = Counter(filtered_words)

print("--- VOCABULARY FREQUENCY ANALYSIS ---")
print(f"Total Raw Words         : {len(words)}")
print(f"After Stopword Removal  : {len(filtered_words)}")
print(f"Total Unique Vocabulary : {len(frequency_counter)}")

print("\n--- TOP 5 MOST FREQUENT KEYWORDS ---")
for word, freq in frequency_counter.most_common(5):
    print(f"Keyword: {word:<15} | Frequency: {freq}")
