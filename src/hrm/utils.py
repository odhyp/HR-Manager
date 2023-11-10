from pathlib import Path


def get_root_path():
    current_path = Path().absolute()
    root_path = Path(current_path).parents[1]
    return root_path


def get_password_path():
    root_path = get_root_path()
    password_path = Path(root_path).joinpath('password.txt')
    return password_path
