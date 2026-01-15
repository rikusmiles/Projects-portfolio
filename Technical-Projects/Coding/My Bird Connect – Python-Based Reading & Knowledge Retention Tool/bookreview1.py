import PyPDF2
import re
from collections import defaultdict

# Keywords for categorization
categories = {
    "philosophy": ["meaning", "life", "existence", "purpose", "ethics", "wisdom"],
    "productivity": ["efficiency", "focus", "task", "time", "goals", "productivity"],
    "work-life balance": ["balance", "stress", "harmony", "family", "relaxation", "leisure"],
    "nutrition": ["diet", "health", "nutrition", "food", "exercise", "well-being"]
}

def extract_highlights_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    highlights = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                highlights.extend(re.split(r'(?<=[.!?]) +', text))  # Split into sentences
    return highlights

def classify_sentences(sentences, categories):
    """Classifies sentences into different categories based on keywords."""
    categorized_sentences = defaultdict(list)
    for sentence in sentences:
        categorized = False
        for category, keywords in categories.items():
            if any(keyword.lower() in sentence.lower() for keyword in keywords):
                categorized_sentences[category].append(sentence)
                categorized = True
                break
        if not categorized:
            categorized_sentences["uncategorized"].append(sentence)
    return categorized_sentences

def save_to_file(categorized_sentences, output_file):
    """Saves categorized sentences to a text file."""
    with open(output_file, 'w') as file:
        for category, sentences in categorized_sentences.items():
            file.write(f"\n=== {category.upper()} ===\n")
            for sentence in sentences:
                file.write(f"- {sentence}\n")

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    output_file = "categorized_highlights.txt"

    print("Extracting highlights from the PDF...")
    highlights = extract_highlights_from_pdf(pdf_path)

    print("Classifying sentences...")
    categorized_sentences = classify_sentences(highlights, categories)

    print("Saving categorized highlights to file...")
    save_to_file(categorized_sentences, output_file)

    print(f"Highlights categorized and saved to {output_file}")
