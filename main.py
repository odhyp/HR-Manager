from fpdf import FPDF

# create FPDF object
# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'A4')

# Add a page
pdf.add_page()

# Specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpdfingbats'
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
# font size = int
pdf.set_font('times', '', 12)

# Add text
# w=width, (if set to 0 means the width is the entire width of the pdf)
# h=height,
# txt='your text',
# ln (False; True - move cursor down to next line)
# border (False; True - add border around cell)
pdf.cell(120, 10, 'Hello World!', border=True)
pdf.cell(80, 10, 'Good Bye World!')

# Output the PDF
# If the file isn't closed, it will return error
pdf.output('pdf_1.pdf')
