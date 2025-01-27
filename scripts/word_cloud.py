import os
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

def preprocess_text(text):
    """Clean and preprocess the text."""
    # Remove special characters and numbers, keep only words
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

def remove_stopwords(words, stopwords):
    """Remove common stopwords from the list of words."""
    return [word for word in words if word not in stopwords]

def calculate_word_frequencies(descriptions, stopwords):
    """Calculate word frequencies from a list of descriptions."""
    # Combine all descriptions into a single string
    all_text = ' '.join(descriptions)
    # Preprocess the text
    cleaned_text = preprocess_text(all_text)
    # Split into words
    words = cleaned_text.split()
    # Remove stopwords
    filtered_words = remove_stopwords(words, stopwords)
    # Count word frequencies
    word_counts = Counter(filtered_words)
    return word_counts

def calculate_percentage(word_counts):
    """Calculate the percentage of each word's appearance."""
    total_count = sum(word_counts.values())
    word_percentages = {word: (count / total_count) * 100 for word, count in word_counts.items()}
    return word_percentages

def create_word_cloud(word_counts):
    """Generate and display a word cloud."""
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def analyze_by_modularity_class(data, stopwords):
    """Analyze word frequencies and generate word clouds for each modularity class."""
    modularity_classes = data['modularity_class'].unique()
    for modularity_class in modularity_classes:
        print(f"\nAnalyzing modularity class {modularity_class}...")
        class_data = data[data['modularity_class'] == modularity_class]
        descriptions = class_data['Description'].dropna().tolist()

        # Calculate word frequencies
        word_counts = calculate_word_frequencies(descriptions, stopwords)

        # Calculate percentages
        word_percentages = calculate_percentage(word_counts)

        # Display the most common words with their percentages
        print("Most common words and their percentages:")
        for word, percentage in sorted(word_percentages.items(), key=lambda x: x[1], reverse=True)[:20]:
            print(f"{word}: {percentage:.2f}%")

        # Create a word cloud
        create_word_cloud(word_counts)

def main():
    # Get the absolute path of the current script
    script_dir = os.path.abspath(os.path.dirname(__file__))

    # Move up to the project root and navigate to the data directory
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    data_path = os.path.join(project_root, 'data', 'nodes.csv')

    # Load the CSV files
    data = pd.read_csv(data_path)

    # Extract the 'Description' column
    descriptions = data['Description'].dropna().tolist()

    # Define a list of stopwords
    stopwords = set([
        'i', 'im', 'own', 'me', 'no','the', 'of', 'at', 'am', 'for', 'you', 'in', 'and', 'to', 'on', 'with', 'a', 'an', 
        'is', 'by', 'my', 'it', 'as', 'own', 'that', 'from', 'your', 'or', 'we', 'are', 'be', 'was', 'will', 'can', 'all',
        'this', 'that', 'from', 'your', 'or', 'we', 'are', 'be', 'was', 'will', 'can', 'all', 'about', 'not', 'has', 'have', 
        'dms', 'dm', 'if', 'so', 'but', 'just', 'get', 'got', 'dont', 'do', 'done', 'doing', 'done', 'does', 'did', 'doing',
    ])

    # Calculate word frequencies
    word_counts = calculate_word_frequencies(descriptions, stopwords)

    # Calculate percentages
    word_percentages = calculate_percentage(word_counts)

    # Display the most common words with their percentages
    print("Most common words and their percentages:")
    for word, percentage in sorted(word_percentages.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"{word}: {percentage:.2f}%")

    # Create a word cloud for the entire dataset
    create_word_cloud(word_counts)

    # Analyze word frequencies and generate word clouds for each modularity class
    analyze_by_modularity_class(data, stopwords)

if __name__ == '__main__':
    main()