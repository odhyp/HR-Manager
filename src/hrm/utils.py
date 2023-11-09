from pathlib import Path


path_current = Path().absolute()
path_root = Path(path_current).parents[1]
path_pass = Path(path_root).joinpath('password.txt')

with open(path_pass) as f:
    username = f.readlines(1)[0].strip()
    password = f.readlines(2)[0].strip()

print(username)
print(password)
