from PyPDF2 import PdfMerger

pdf_files = ["doc.pdf", "doc.pdf"]
merger = PdfMerger()

for pdf in pdf_files:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
print("Merged PDF files successfully and saved as merged.pdf")