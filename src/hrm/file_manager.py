class FileManager:
    def is_xls(self, file_name):
        return file_name.endswith('.xls')

    def is_xlsx(self, file_name):
        return file_name.endswith('.xlsx')
