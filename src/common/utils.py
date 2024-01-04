from pathlib import Path


def get_root_path():
    """Get project root path
    """
    current_path = Path().absolute()
    root_path = Path(current_path)
    return root_path


def get_data_path():
    """Get data directory path
    """
    root_path = get_root_path()
    data_path = Path(root_path, 'data')
    return data_path


def get_password_path():
    """Get 'password.txt' path
    """
    root_path = get_root_path()
    password_path = Path(root_path, 'password.txt')
    return password_path


def get_download_path():
    """Get User/Downloads path
    """
    return Path(Path.home(), "Downloads")


def get_username():
    """Get username from p'assword.txt'
    """
    with open(get_password_path()) as f:
        username = f.readlines()[0].strip()
    return str(username)


def get_password():
    """Get password from 'password.txt'
    """
    with open(get_password_path()) as f:
        password = f.readlines()[1].strip()
    return str(password)


def get_base_text_path():
    """Get 'base_text.txt' path
    """
    data_path = get_data_path()
    base_text_path = Path(data_path, 'base_text.txt')
    return base_text_path


def get_user_text_path():
    """Get 'user_text.txt' path
    """
    data_path = get_data_path()
    user_text_path = Path(data_path, 'user_text.txt')
    return user_text_path
