import re
from collections import Counter

def find_most_frequent_word(file_path):
    # Read the file content
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Convert to lowercase for case-insensitive counting
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    # Remove punctuation and split into words
    words = re.findall(r'\b[a-z]+\b', text)  # Matches words consisting of letters only
    
    if not words:
        print("No words found in the file.")
        return None

    # Count word frequencies
    word_counts = Counter(words)
    
    # Find the most common word(s)
    most_common = word_counts.most_common(1)
    
    return most_common[0]  


if __name__ == "__main__":
    file_path = 'sample.txt'  
    result = find_most_frequent_word(file_path)
    
    if result:
        word, count = result
        print(f"The most frequent word is '{word}' appearing {count} times.")