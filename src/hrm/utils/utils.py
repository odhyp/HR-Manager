from pathlib import Path


def get_root_path():
    current_path = Path().absolute()
    root_path = Path(current_path).parents[2]
    return root_path


def get_password_path():
    root_path = get_root_path()
    password_path = Path(root_path, 'password.txt')
    return password_path


def get_admin_username():
    with open(get_password_path()) as f:
        username = f.readlines()[0].strip()
        return str(username)


def get_admin_password():
    with open(get_password_path()) as f:
        password = f.readlines()[1].strip()
        return str(password)


def get_download_path():
    return Path(Path.home(), "Downloads")
