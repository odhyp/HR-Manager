from src.spt.pdf import PDF
from src.spt import constants


def create_pdf():
    pdf = PDF('P', 'mm', constants.PAPER_SIZE)
    pdf.set_title('Surat Perintah Tugas')
    pdf.set_author('Odhy Pradhana')
    pdf.print_section()
    pdf.output('pdf_3.pdf')


if __name__ == '__main__':
    create_pdf()
