from fpdf import FPDF

# Layout    P, L
# Unit      mm, cm, in
# format    A3, A4 (default), A5, Letter, Legal, (100, 150)
pdf = FPDF('P', 'mm', 'Letter')

pdf.add_page()

# font      times, courier, helvetica, symbol, zpdfingbats
#           B, I, U, '', combinations (BI)
pdf.set_font('helvetica', '', 16)

# adding text
# width
# height
pdf.cell(120, 100, 'Hello World', ln=True, border=True)
pdf.cell(80, 10, 'Hi This is Python')

pdf.output('pdf_1.pdf')
