# chat_with_doc

#imports
import streamlit as st
from PIL import Image
import pytesseract
import pdfplumber
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import time


