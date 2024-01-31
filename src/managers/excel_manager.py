from openpyxl import load_workbook
from win32com.client import Dispatch
from xls2xlsx import XLS2XLSX


class ExcelManager:
    def convert_xls(self, file_path: str, file_format: int = 51):
        """Convert an Excel file from '.xls' to '.xlsx' format using pywin32

        Args:
        - file_path (str): The path to the input '.xls' file.
        - file_format (int, optional): The file format code for '.xlsx'.
        Default is 51.
        """
        excel_app = Dispatch("Excel.Application")
        excel_app.Visible = False
        output_path = str(file_path) + 'x'
        workbook = excel_app.Workbooks.Open(file_path)
        workbook.SaveAs(output_path, FileFormat=file_format)
        workbook.Close()
        excel_app.Quit()

    def convert_xls2(self, file_path: str):
        """Convert an Excel file from '.xls' to '.xlsx' format using xls2xlsx.

        Args:
        - file_path (str): The path to the input '.xls' file.
        """
        output_path = str(file_path) + 'x'
        x2x = XLS2XLSX(file_path)
        x2x.to_xlsx(output_path)

    def format_nominatif(self, file_path: str):
        """Format 'Nominatif.xlsx'

        Args:
        - file_path (str): Path to the 'Nominatif.xlsx'
        """
        wb = load_workbook(filename=file_path)
        ws = wb.active
        ws.delete_cols(1, 1)
        ws.delete_rows(1, 4)
