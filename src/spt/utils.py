from pathlib import Path


def get_root_path():
    current_path = Path().absolute()
    root_path = Path(current_path)
    return root_path


def get_data_path():
    root_path = get_root_path()
    data_path = Path(root_path, 'data')
    return data_path


def get_golongan_path():
    data_path = get_data_path()
    golongan_path = Path(data_path, 'golongan.txt')
    return golongan_path
