from src.spt.pdf import PDF
from src.spt import constants


def main():
    pdf = PDF('P', 'mm', constants.PAPER_SIZE)
    pdf.set_title('Surat Perintah Tugas')
    pdf.set_author('Odhy Pradhana')

    pdf.print_chapter()

    pdf.output('pdf_2.pdf')


if __name__ == '__main__':
    main()
