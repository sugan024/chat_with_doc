import streamlit as st
from PIL import Image
import pytesseract
import pdfplumber
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import time

# Load pre-trained models
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Function to extract text from PDFs
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to extract text from images (OCR)
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

# Function to process uploaded file and extract content
def process_uploaded_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type.startswith("image/"):
        img = Image.open(uploaded_file)
        return extract_text_from_image(img)
    else:
        return None

# Function to chunk text into smaller parts
def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Streamlit App with Enhanced UI/UX
st.set_page_config(
    page_title="your chat_with_document",
    page_icon="📄",
    layout="wide",
)

st.title("📄 your chat_with_document")
st.markdown(
    "<style>h1 { color: #2c3e50; } .stButton button { background-color: #1abc9c; color: white; border-radius: 5px; }</style>",
    unsafe_allow_html=True
)

# Sidebar for file upload and document preview
with st.sidebar:
    st.header(" Upload Document")
    st.write("Upload a PDF or an image to analyze its content.")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "jpg", "jpeg", "png"], label_visibility='collapsed')

    
# Main Content
if uploaded_file:
    with st.spinner("document is getting process..."):
        document_text = process_uploaded_file(uploaded_file)
        time.sleep(2)  # Simulating processing delay

    if document_text:
        st.success("Document text extracted successfully!")
        st.markdown(
            f"<div style='padding:10px; background-color:#ecf0f1; border-radius:5px;'>Preview: {document_text[:200]}...</div>",
            unsafe_allow_html=True
        )

        # Chunk the document for efficient processing
        text_chunks = chunk_text(document_text)

        # User query input
        st.write("### Ask your Question")
        user_question = st.text_input("Enter your question :")

        if st.button("Get Answer"):
            if user_question:
                with st.spinner("Analyzing your question..."):
                    context = " ".join(text_chunks)
                    qa_response = qa_model(question=user_question, context=context)
                    time.sleep(1.5)  # Simulating response time
                st.write("#### Answer:")
                st.success(qa_response["answer"])

        st.markdown("---")

        # Advanced embedding visualization
        st.write("### Document Embedding and Analysis")
        with st.spinner("Calculating embeddings..."):
            embeddings = embedding_model.encode(text_chunks, convert_to_tensor=True)
            time.sleep(1.5)  # Simulating embedding calculation delay
        st.success("Embeddings calculated completed!")

        st.write("You can now use these embeddings to integrate.")

    else:
        st.error("Unable to extract text from the uploaded document. Please upload a valid PDF or image file.")
else:
    st.info("Please upload a document to get started.")