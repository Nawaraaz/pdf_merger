PDF merger
Setup guide:
Create a folder name pdfmerger
For Ubuntu:
creating a virtual environment: python3 -m venv env

activate env
 source/env/bin/activate

 why installation of packages in side virtual environment?

-Keep project dependencies isolated:
 Projects can exist with their own independent versions of libraries without disturbing each other.

Keep system Python intact:
 Don't break the system Python in Ubuntu by isolating your project libraries.

Keep projects portable:
 Recreate or share the setup of the project easily using a requirements.txt file.

Keep the project clean and organized:
 Each project contains just necessary packages within its own venv directory.

After sucessfully activating Virtual environment follow the below steps:

Add the pdf files you want to merge inside this folder
Step:1
 Installing PyPDF2: pip install PyPDF2

Step:2
 Creating a merger file
 create a file named merger.py

step:3
 Add the code inside the file merger.py

step:4
 Look for the pdf_files = ["doc.pdf", "doc.pdf"] in merger.py
 replace the doc.pdf by your pdf file name you can merge multiple pdf file by just adding inside your pdfmerger folder and by replacing the name.

step:5
 Run the merger.py file: python merger.py

If the above steps are correct you will see "Merged PDF files successfully and saved as merged.pdf" in terminal. A new pdf file will be appear inside pdfmerger folder by the name merged.pdf
