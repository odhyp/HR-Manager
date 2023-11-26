from pathlib import Path


def get_root_path():
    current_path = Path().absolute()
    root_path = Path(current_path)
    return root_path


def get_data_path():
    root_path = get_root_path()
    data_path = Path(root_path, 'data')
    return data_path


def get_duk_path():
    data_path = get_data_path()
    duk_path = Path(data_path, 'duk.xlsx')
    return duk_path
