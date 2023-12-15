from src.spt.pdf import PDF
from src.spt import constants
from src.spt.text_generator import TextGenerator


def create_pdf():
    pdf = PDF(orientation='P',
              unit='mm',
              format=constants.PAPER_SIZE)
    pdf.print_sections()


if __name__ == '__main__':
    create_pdf()
