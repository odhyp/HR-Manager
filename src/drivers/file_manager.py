import time

from src.drivers.utils import get_download_path


class FileManager:
    def get_name_format(self, type):
        name_format = {
            "presensi": "Laporan Rekap Presensi",
            "prestasi": "Laporan Rekap Prestasi",
            "nominatif": "DAFTAR_PEGAWAI_NOMINATIF_",
            "duk": "DAFTAR_URUT_KEPANGKATAN_",
        }
        return name_format[type]

    def is_xls(self, file_name):
        return file_name.endswith('.xls')

    def is_xlsx(self, file_name):
        return file_name.endswith('.xlsx')

    def is_target_file(self, type, file_name):
        name_format = self.get_name_format(type)
        if file_name.find(name_format) == 0:
            return True
        else:
            return False

    def is_downloaded(self, type):
        for file in get_download_path().iterdir():
            is_target_file = self.is_target_file(type, file.name)
            is_xls = self.is_xls(file.name)
            if is_target_file and is_xls:
                return True
            else:
                continue
        return False

    def wait_for_download(self, type, timeout=20):
        while not self.is_downloaded(type) and timeout != 0:
            time.sleep(1)
            timeout -= 1
        return True

    def get_file_path(self, type):
        for file in get_download_path().iterdir():
            is_target_file = self.is_target_file(type, file.name)
            if is_target_file:
                return file
            else:
                continue
        return f"File not found."
