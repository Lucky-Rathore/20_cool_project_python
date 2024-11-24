import PyPDF2

def merge_pdfs(pdf_list, output):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for n_page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[n_page])

    with open(output, 'wb') as out_file:
        pdf_writer.write(out_file)

# List of PDFs to merge
pdf_files = ['a1.pdf', 'a2.pdf']

# Merge them into a single output PDF
merge_pdfs(pdf_files, 'merged_output.pdf')