import os
from pdfminer.high_level import extract_text
from docx import Document
from ocr_utils import ocr_image

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file. If the PDF is scanned (image-based), OCR will be applied.
    """
    try:
        # Attempt to extract text using pdfminer
        text = extract_text(pdf_path)
        
        # If extracted text is empty, apply OCR
        if not text.strip():  # In case of image-based PDFs
            print("No text found, applying OCR...")
            text = ocr_image(pdf_path)
        return text
    
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {e}")

# Function to extract text from DOCX files
def extract_text_from_docx(docx_path: str) -> str:
    """
    Extract text from a DOCX file.
    """
    try:
        doc = Document(docx_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    
    except Exception as e:
        raise Exception(f"Error extracting text from DOCX: {e}")
