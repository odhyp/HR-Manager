from src.spt.pdf import PDF
from src.spt import constants
from src.spt.text_generator import TextGenerator
from src.hrm.driver_presensi import DriverPresensi
from src.hrm.driver_simpeg import DriverSimpeg
from src.hrm.file_manager import FileManager
from src.hrm.utils import get_username, get_password


def create_pdf():
    pdf = PDF(orientation='P',
              unit='mm',
              format=constants.PAPER_SIZE)
    pdf.print_sections()


def run_drivers():
    username = get_username()
    password = get_password()

    file_manager = FileManager()

    presensi = DriverPresensi(username, password)
    presensi.login()
    presensi.rekap_presensi("2023-11-01", "2023-11-20")
    file_manager.wait_for_download('presensi')
    presensi.rekap_prestasi("11/2023")
    file_manager.wait_for_download('prestasi')
    presensi.quit()

    simpeg = DriverSimpeg(username, password)
    simpeg.login()
    simpeg.nominatif()
    file_manager.wait_for_download('nominatif')
    simpeg.duk()
    file_manager.wait_for_download('duk')
    simpeg.quit()


def main():
    create_pdf()
    run_drivers()


if __name__ == '__main__':
    main()
