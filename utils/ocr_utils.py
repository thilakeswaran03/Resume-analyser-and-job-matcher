import pytesseract
from PIL import Image
import pdf2image

# Function to extract text from image using OCR (Tesseract)
def ocr_image(file_path: str) -> str:
    
    try:
        # Check if the input is a PDF file
        if file_path.lower().endswith('.pdf'):
            images = pdf2image.convert_from_path(file_path)  # Convert PDF to images
            text = ""
            for image in images:
                text += pytesseract.image_to_string(image)  # Perform OCR on each page
        else:
            # If it's an image file (JPG, PNG, etc.)
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)  # Perform OCR on the image
            
        return text

    except Exception as e:
        raise Exception(f"Error during OCR processing: {e}")
