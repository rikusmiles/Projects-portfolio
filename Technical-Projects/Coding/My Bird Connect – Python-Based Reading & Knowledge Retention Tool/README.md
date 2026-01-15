# My Bird Connect – Python-Based Reading & Knowledge Retention Tool

## 📌 Project Overview
My Bird Connect is a Python-based application designed to help readers retain and apply insights from books more effectively. The tool extracts highlighted text from PDF books, categorizes the content into meaningful zones, and presents the insights through an interactive graphical dashboard.

This project demonstrates practical use of Python for document processing, text categorization, and GUI-based visualization.

---

## 🎯 Problem Statement
Modern information consumption is at an all-time high, yet readers often struggle to retain or apply what they read. Highlights remain scattered across documents with no structured way to organize or revisit them meaningfully.

---

## ✅ Project Objective
The goal of this project is to:
- Extract highlighted text directly from PDF files
- Categorize highlights into predefined zones using keyword-based logic
- Display insights in a clean, user-friendly dashboard
- Support actionable learning and long-term retention

---

## 🛠️ Project Approach
The application follows a modular and scalable approach:

1. **Extracting Highlights**  
   Uses the PyMuPDF (fitz) library to scan PDF annotations and accurately extract highlighted text based on annotation coordinates.

2. **Categorizing Highlights**  
   Extracted text is assigned to predefined categories (zones) using keyword matching logic.

3. **Dashboard Display**  
   A tkinter-based GUI displays categorized highlights in separate windows, each with its own visual styling.

4. **Zone-Based Organization**  
   Each category is rendered in a dedicated window with distinct colors and branding elements for clarity.

---

## 📚 Technologies & Libraries Used
- **Python 3**
- **PyMuPDF (fitz)** – PDF annotation and highlight extraction
- **Pillow (PIL)** – Image handling for GUI elements
- **tkinter** – GUI development (standard Python library)
- **collections.defaultdict** – Efficient data categorization

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x installed

### Install Required Libraries
```bash
pip install pymupdf
pip install pillow
