import os
import time

from src.common.constants import PAPER_SIZE
from src.common.utils import get_username, get_password

from src.drivers.driver_presensi import DriverPresensi
from src.drivers.driver_simpeg import DriverSimpeg

from src.managers.file_manager import FileManager
from src.managers.excel_manager import ExcelManager

from src.pdfs.pdf_spt import PDF
from src.pdfs.text_generator import TextGenerator


def create_pdf():
    pdf = PDF(orientation='P',
              unit='mm',
              format=PAPER_SIZE)
    pdf.print_sections()


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


class Drivers:
    def __init__(self):
        self.username = get_username()
        self.password = get_password()
        self.file_manager = FileManager()
        self.excel_manager = ExcelManager()

    def download_nominatif(self):
        file_type = 'nominatif'

        print(f"> Downloading: {file_type}")
        simpeg = DriverSimpeg(self.username, self.password)
        simpeg.login()
        simpeg.nominatif()
        self.file_manager.wait_for_download(file_type)
        simpeg.quit()
        print("> Download success!\n")

        print("> Converting xls to xlsx")
        xls_path = self.file_manager.get_file_path(file_type, 'xls')
        self.excel_manager.convert_xls(xls_path)
        self.file_manager.remove_file(xls_path)
        print("> Convert success!\n")

        print(f"> Formatting {file_type}")
        xlsx_path = self.file_manager.get_file_path(file_type, 'xlsx')
        self.excel_manager.format_nominatif(xlsx_path)
        print("> Format success!\n")

    def download_duk(self):
        file_type = 'duk'

        print(f"> Downloading: {file_type}")
        simpeg = DriverSimpeg(self.username, self.password)
        simpeg.login()
        simpeg.duk()
        self.file_manager.wait_for_download(file_type)
        simpeg.quit()
        print("> Download success!\n")

        print("> Converting xls to xlsx")
        xls_path = self.file_manager.get_file_path(file_type, 'xls')
        self.excel_manager.convert_xls(xls_path)
        self.file_manager.remove_file(xls_path)
        print("> Convert success!\n")

        print(f"> Formatting {file_type}")
        xlsx_path = self.file_manager.get_file_path(file_type, 'xlsx')
        self.excel_manager.format_nominatif(xlsx_path)
        print("> Format success!\n")

    def download_rekap_harian(self,
                              start_date: str,
                              end_date: str,
                              report_type: str = "detail"):
        file_type = 'presensi'

        print(f"> Downloading: {file_type}")
        presensi = DriverPresensi(self.username, self.password)
        presensi.login()
        presensi.rekap_presensi(start_date, end_date, report_type)
        self.file_manager.wait_for_download(file_type)
        presensi.quit()
        print("> Download success!\n")

        print("> Converting xls to xlsx")
        xls_path = self.file_manager.get_file_path(file_type, 'xls')
        self.excel_manager.convert_xls(xls_path)
        self.file_manager.remove_file(xls_path)
        print("> Convert success!\n")

        print(f"> Formatting {file_type}")
        xlsx_path = self.file_manager.get_file_path(file_type, 'xlsx')
        self.excel_manager.format_nominatif(xlsx_path)
        print("> Format success!\n")

    def download_rekap_prestasi(self,
                                month: str):
        file_type = 'prestasi'

        print(f"> Downloading: {file_type}")
        presensi = DriverPresensi(self.username, self.password)
        presensi.login()
        presensi.rekap_prestasi(month)
        self.file_manager.wait_for_download(file_type)
        presensi.quit()
        print("> Download success!\n")

        print("> Converting xls to xlsx")
        xls_path = self.file_manager.get_file_path(file_type, 'xls')
        self.excel_manager.convert_xls(xls_path)
        self.file_manager.remove_file(xls_path)
        print("> Convert success!\n")

        print(f"> Formatting {file_type}")
        xlsx_path = self.file_manager.get_file_path(file_type, 'xlsx')
        self.excel_manager.format_nominatif(xlsx_path)
        print("> Format success!\n")


class Menu:
    def clear(self):
        os.system("cls")

    def menu_screen(self):
        self.clear()

        print("--- HR Manager ---\n")
        print("[1] Download Nominatif")
        print("[2] Download DUK")
        print("[3] Download Rekap Harian")
        print("[4] Download Rekap Prestasi")
        print("[0] Exit\n")

    def menu_selection(self):
        self.clear()
        self.menu_screen()
        choice = str(input("> ")).lower()

        if choice == '0':
            print("Thank you")
        elif choice == '1':
            Drivers().download_nominatif()
        elif choice == '2':
            Drivers().download_duk()
        elif choice == '3':
            print('Date format: "yyyy-mm-dd"')
            start_date = str(input("> Start date:\n> "))
            end_date = str(input("> End date:\n> "))
            Drivers().download_rekap_harian(start_date, end_date)
        elif choice == '4':
            print('Month format: "mm/yyyy"')
            month = str(input("> Month:\n> "))
            Drivers().download_rekap_prestasi(month)
        else:
            print("> Invalid input!")
            input("> Press any key to continue. . .")
            self.menu_selection()


def main():
    Menu().menu_selection()


if __name__ == '__main__':
    main()
