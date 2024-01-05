import time

from src.common.constants import PAPER_SIZE
from src.common.utils import get_username, get_password

from src.drivers.driver_presensi import DriverPresensi
from src.drivers.driver_simpeg import DriverSimpeg

from src.managers.file_manager import FileManager
from src.managers.excel_manager import ExcelManager

from src.spt.pdf import PDF
from src.spt.text_generator import TextGenerator


def create_pdf():
    pdf = PDF(orientation='P',
              unit='mm',
              format=PAPER_SIZE)
    pdf.print_sections()


def run_drivers():
    # Initialization
    username = get_username()
    password = get_password()
    file_manager = FileManager()
    excel_manager = ExcelManager()

    # Running PRESENSI
    presensi = DriverPresensi(username, password)
    presensi.login()
    presensi.rekap_presensi("2024-01-01", "2024-01-05")
    file_manager.wait_for_download('presensi')
    presensi.rekap_prestasi("01/2024")
    file_manager.wait_for_download('prestasi')
    presensi.quit()

    # Running SIMPEG
    simpeg = DriverSimpeg(username, password)
    simpeg.login()
    simpeg.nominatif()
    file_manager.wait_for_download('nominatif')
    simpeg.duk()
    file_manager.wait_for_download('duk')
    simpeg.quit()

    # Converts 'xls' to 'xlsx'
    def converting(file_type: str):
        try:
            input_file = file_manager.get_file_path(file_type)
            excel_manager.convert_xls_to_xlsx(input_file)
        except Exception as e:
            print(e)

    converting('presensi')
    converting('prestasi')
    converting('nominatif')
    converting('duk')


def format_excel():
    # Initialization
    file_manager = FileManager()
    excel_manager = ExcelManager()

    # Format 'Nominatif.xlsx'
    def formatting_nominatif():
        try:
            input_file = file_manager.get_file_path('nominatif')
            print(input_file)
            excel_manager.format_nominatif(input_file)
        except Exception as e:
            print(e)

    formatting_nominatif()


def main():
    create_pdf()
    run_drivers()
    format_excel()


if __name__ == '__main__':
    main()
