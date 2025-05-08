import os

# Function to validate if file exists
def is_file_valid(file_path: str) -> bool:
    """
    Check if the file exists at the given path.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return True

# Function to get the file extension and route accordingly
def get_file_extension(file_path: str) -> str:
    """
    Get the file extension to determine how to process the file.
    """
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension not in ['.pdf', '.docx', '.jpg', '.jpeg', '.png']:
        raise ValueError("Unsupported file format. Supported formats: PDF, DOCX, JPG, PNG")
    return file_extension

# Main function to handle the file and extract text
def handle_file(file_path: str) -> str:
    """
    Handle the file based on its extension and return extracted text.
    """
    # Validate the file path
    if is_file_valid(file_path):
        # Get the file extension
        file_extension = get_file_extension(file_path)

        # Route to the respective extraction process
        if file_extension == '.pdf':
            from extract_text import extract_text_from_pdf
            return extract_text_from_pdf(file_path)
        elif file_extension == '.docx':
            from extract_text import extract_text_from_docx
            return extract_text_from_docx(file_path)
