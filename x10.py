import PyPDF2
import sys

FILENAME_IN = sys.argv[1]
FILENAME_OUT = FILENAME_IN
PAGES = int(sys.argv[2])
TEMPLATE = sys.argv[3] if len(sys.argv) >= 4 else None

pdf_reader = PyPDF2.PdfFileReader(FILENAME_IN)
pdf_writer = PyPDF2.PdfFileWriter()

if TEMPLATE is not None:
    template_reader = PyPDF2.PdfFileReader(TEMPLATE)
    page = template_reader.getPage(0)
else:
    page = pdf_reader.getPage(-1)

for n in range(0, pdf_reader.getNumPages()):
    pdf_writer.addPage(pdf_reader.getPage(n))
for n in range(1, PAGES+1):
    pdf_writer.addPage(page)

with open(FILENAME_OUT, 'wb') as output_file:
    pdf_writer.write(output_file)
