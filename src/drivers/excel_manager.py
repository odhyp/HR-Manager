import win32com.client as win32


class ExcelManager:
    def convert_xls_to_xlsx(self, file_path: str, file_format: int = 51):
        """Convert an Excel file from '.xls' to '.xlsx' format.

        Args:
        - file_path (str): The path to the input '.xls' file.
        - file_format (int, optional): The file format code for '.xlsx'. Default is 51.
        """
        excel_app = win32.Dispatch("Excel.Application")
        excel_app.Visible = False
        output_path = str(file_path) + 'x'
        workbook = excel_app.Workbooks.Open(file_path)
        workbook.SaveAs(output_path, FileFormat=file_format)
        workbook.Close()
        excel_app.Quit()
