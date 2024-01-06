from openpyxl import load_workbook
from win32com.client import Dispatch


class ExcelManager:
    def convert_xls_to_xlsx(self, file_path: str, file_format: int = 51):
        """Convert an Excel file from '.xls' to '.xlsx' format.

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

    def format_xlsx(self, file_type: str, file_path: str):
        """Format the specified 'xlsx' file

        Args:
        - file_type (str): The type of the specified 'xlsx' file. Example: 'nominatif'
        - file_path (str): Path to the specified 'xlsx' file
        """
        wb = load_workbook(filename=file_path)
        ws = wb.active

        if file_type == 'nominatif':
            ws.delete_cols(1, 1)
            ws.delete_rows(1, 4)
        elif file_type == 'duk':
            ws.delete_rows(1, 4)
        else:
            print('Invalid file type.')

        wb.save(filename=file_path)
