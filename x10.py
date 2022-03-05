import PyPDF2
import sys
import os
import shutil

FILENAME_IN = sys.argv[1]
FILENAME_OUT = FILENAME_IN
BACKUP_FOLDER = 'BACKUP'
TEMPLATE_NAME = 'template.pdf'

if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)
shutil.copy(FILENAME_IN, BACKUP_FOLDER)
template = TEMPLATE_NAME if os.path.exists(TEMPLATE_NAME) else None
pages = int(os.path.basename(__file__).split('.')[-2][1:])

pdf_reader = PyPDF2.PdfFileReader(FILENAME_IN)
pdf_writer = PyPDF2.PdfFileWriter()

if template is not None:
    template_reader = PyPDF2.PdfFileReader(template)
    page = template_reader.getPage(0)
else:
    page = pdf_reader.getPage(-1)

for n in range(0, pdf_reader.getNumPages()):
    pdf_writer.addPage(pdf_reader.getPage(n))
for n in range(1, pages+1):
    pdf_writer.addPage(page)

with open(FILENAME_OUT, 'wb') as output_file:
    pdf_writer.write(output_file)
