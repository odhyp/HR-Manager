import pandas as pd


def convert_to_csv():
    df = pd.DataFrame(pd.read_excel(io='duk.xlsx',
                                    index_col=None,
                                    usecols=['JABATAN'],
                                    # usecols=['NIP', 'NAMA', 'GOLONGAN', 'JABATAN'],
                                    skiprows=4,
                                    ))

    df['JABATAN'] = df['JABATAN'].str.replace('\n', ' ').str.replace('\r', '')

    df.to_csv(path_or_buf='duk.txt',
              sep=';',
              index=False,
              )
