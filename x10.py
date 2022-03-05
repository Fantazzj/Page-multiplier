import PyPDF2
import sys
from pathlib import Path

filename_in = sys.argv[1]
filename_out = filename_in
pages = int(Path(__file__).stem.replace("x",""))
template = sys.argv[2] if len(sys.argv) >= 5 else None

pdf_reader = PyPDF2.PdfFileReader(filename_in)
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

with open(filename_out, 'wb') as output_file:
    pdf_writer.write(output_file)
