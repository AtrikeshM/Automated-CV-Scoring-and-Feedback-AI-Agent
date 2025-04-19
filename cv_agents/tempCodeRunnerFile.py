import os
import re
import pandas as pd
from docx import Document
import PyPDF2
import fitz  # PyMuPDF

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else 'Not Found'

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def process_resumes(folder_path):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing: {filename}")

            if filename.endswith('.docx'):
                text = extract_text_from_docx(file_path)
            else:
                text = extract_text_from_pdf(file_path)

            email = extract_email(text)
            name = filename.split('.')[0].replace('_', ' ').title()

            # Ensure 'resume_text' is the text extracted from the resume
            resume_text = text

            data.append({
                "masked_name": name,  # Replace with your masking logic if needed
                "masked_email": email,  # Apply any email masking if required
                "original_name": name,
                "original_email": email,
                "text": resume_text  # Include extracted text from resume
            })

    return pd.DataFrame(data)

if __name__ == "__main__":
    resumes_folder = "resumes"
    output_csv = "output/resume_data.csv"
    os.makedirs("output", exist_ok=True)

    # Call the function and store the result in df
    df = process_resumes(resumes_folder)

    # Save the DataFrame to CSV
    df.to_csv(output_csv, index=False)
    print(f"\n✅ Data saved to: {output_csv}")
