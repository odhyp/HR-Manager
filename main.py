from src.spt.pdf import PDF, PAPER_SIZE_F4


def main():
    pdf = PDF('P', 'mm', PAPER_SIZE_F4)
    pdf.set_title('Surat Perintah Tugas')
    pdf.set_author('Odhy Pradhana')

    pdf.print_chapter()

    pdf.output('pdf_2.pdf')


if __name__ == '__main__':
    main()
