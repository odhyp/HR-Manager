import time
from pathlib import Path
from typing import Union

from src.common.utils import get_download_path


class FileManager:
    def get_name_format(self, type: str) -> str:
        """Get the name format based on the specified type.

        Args:
        - type (str): The type of the file.
        """
        name_format = {
            "presensi": "Laporan Rekap Presensi",
            "prestasi": "Laporan Rekap Prestasi",
            "nominatif": "DAFTAR_PEGAWAI_NOMINATIF_",
            "duk": "DAFTAR_URUT_KEPANGKATAN_",
        }
        return name_format[type]

    def is_xls(self, file_name: str) -> bool:
        """Check if the file has a '.xls' extension.

        Args:
        - file_name (str): The name of the file.
        """
        return file_name.endswith('.xls')

    def is_xlsx(self, file_name: str) -> bool:
        """Check if the file has an '.xlsx' extension.

        Args:
        - file_name (str): The name of the file.
        """
        return file_name.endswith('.xlsx')

    def is_target_file(self, type: str, file_name: str) -> bool:
        """Check if the file matches the expected format for the
        specified type.

        Args:
        - type (str): The type of the file.
        - file_name (str): The name of the file.
        """
        name_format = self.get_name_format(type)
        if file_name.find(name_format) == 0:
            return True
        else:
            return False

    def is_downloaded(self, type: str) -> bool:
        """Check if a file of the specified type with '.xls' extension
        is downloaded.

        Args:
        - type (str): The type of the file.
        """
        for file in get_download_path().iterdir():
            is_target_file = self.is_target_file(type, file.name)
            is_xls = self.is_xls(file.name)
            if is_target_file and is_xls:
                return True
            else:
                continue
        return False

    def wait_for_download(self, type: str, timeout: int = 20) -> bool:
        """Wait for a file of the specified type with '.xls' extension
        to be downloaded.

        Args:
        - type (str): The type of the file.
        - timeout (int): The maximum time to wait in seconds.
        Default is 20 seconds.
        """
        while not self.is_downloaded(type) and timeout != 0:
            time.sleep(1)
            timeout -= 1
        return True

    def get_file_path(self, type: str) -> Union[Path, str]:
        """Get the path of the downloaded file for the specified type.

        Args:
        - type (str): The type of the file.
        """
        for file in get_download_path().iterdir():
            is_target_file = self.is_target_file(type, file.name)
            if is_target_file:
                return file
            else:
                continue
        return f"File not found."
