import pandas as pd

from src.common.utils import get_data_path, get_duk_path


class DUK:
    def convert_to_csv(self):
        """Convert "Daftar Urut Kepangkatan.xlsx" to CSV format.

        Extracts data from DUK.xlsx in C:\\Users\\Username\\Downloads
        and stores it as a CSV file in spt\\data.
        """
        data_path = get_data_path()
        duk_path = get_duk_path()
        output_path = str(data_path) + '\\duk.txt'
        df = pd.DataFrame(pd.read_excel(io=duk_path,
                                        index_col=None,
                                        usecols=['NAMA',
                                                 'NIP',
                                                 'GOLONGAN',
                                                 'JABATAN'],
                                        skiprows=4,
                                        ))

        df['JABATAN'] = df['JABATAN'].str.replace(
            '\n', ' ').str.replace('\r', '')

        df.to_csv(path_or_buf=output_path,
                  sep=';',
                  index=False,
                  )
