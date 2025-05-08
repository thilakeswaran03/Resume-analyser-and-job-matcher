import os
from file_handler import handle_file
from ocr_utils import ocr_image

def main():
    """
    Main function to run the resume analysis process.
    """
    try:
        # Specify the input file path (could be a PDF, Word, Image, etc.)
        file_path = "D:/Resume_project/Screenshot 2025-05-08 211746.png"

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at {file_path} does not exist.")
        
        # Extract the text based on file type (PDF, DOCX, Image)
        if file_path.lower().endswith(('.pdf', '.docx', '.txt')):
            extracted_text = handle_file(file_path)
        elif file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            extracted_text = ocr_image(file_path)
        else:
            raise ValueError("Unsupported file type. Please provide a PDF, DOCX, or Image file.")
        
        # Display extracted text (for testing)
        print("Extracted Text: ")
        print(extracted_text)

        # Continue with the rest of the resume analysis process (like job matching)
        # For now, we simply print the extracted text.
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
