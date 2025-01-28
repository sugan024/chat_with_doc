# chat_with_doc

#An AI-powered document question-answering system that leverages Google's Gemini Pro model and Cohere embeddings. Upload PDF documents and get instant, accurate answers to your questions about the content.

#imports
import streamlit as st
from PIL import Image
import pytesseract
import pdfplumber
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import time

## 🛠️ Prerequisites
- Python 3.8 or higher
- Virtual environment (pip)

- ###  Set Up Virtual Environment
#### Using venv
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
- 
- ### requirements
- streamlit
Pillow
pytesseract
pdfplumber
transformers
sentence-transformers
torch
faiss-cpu

###quesion and answering
#upload th document
#it starts processing
#ask question realated to doc
#answer is provided
#get embeddings too

##process
# pdf reader
# extract chunks
# makes enbedding
# vectore store
# question answering model

