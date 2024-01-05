import os

from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(pdf_list, output_path):
    pdf_writer = PdfWriter()

    for pdf_file in pdf_list:
        with open(pdf_file, "rb") as file:
            pdf_reader = PdfReader(file)

            if pdf_reader.is_encrypted:
                password = input(f"Enter password for {pdf_file}: ")
                pdf_reader.decrypt(password)

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)


def merge_pdfs_in_folder(folder_path, output_path):
    pdf_files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.endswith(".pdf")
    ]

    pdf_files = sorted(pdf_files)
    merge_pdfs(pdf_files, output_path)


# Folder containing PDF files to merge
input_folder = "/Users/ruonan.zhang/Library/CloudStorage/OneDrive-LynchpinAnalyticsLimited/Personal/Personal photo and docs/Xero/2023"  # Replace 'folder_path' with your folder path containing PDFs

# Output file path for merged PDF
output_pdf_path = "merged_file.pdf"  # Change the output file path as needed

merge_pdfs_in_folder(input_folder, output_pdf_path)
