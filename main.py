from src.spt.pdf import PDF
from src.spt import constants


def create_pdf():
    pdf = PDF(orientation='P',
              unit='mm',
              format=constants.PAPER_SIZE)
    pdf.print_section()


if __name__ == '__main__':
    create_pdf()
