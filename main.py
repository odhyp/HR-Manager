from src.hrm.driver_presensi import DriverPresensi
from src.hrm.driver_simpeg import DriverSimpeg
from src.hrm.utils import get_username, get_password

import time


def main():
    username = get_username()
    password = get_password()

    presensi = DriverPresensi(username, password)
    presensi.login()
    time.sleep(2)
    presensi.quit()

    time.sleep(2)

    simpeg = DriverSimpeg(username, password)
    simpeg.login()
    time.sleep(2)
    simpeg.quit()


if __name__ == '__main__':
    main()
