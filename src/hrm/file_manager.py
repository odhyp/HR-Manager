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
