![Under Development](https://img.shields.io/badge/under-development-yellow?style=for-the-badge)
[![Version - FPDF2](https://img.shields.io/badge/FPDF2-2.7.6-teal?style=for-the-badge&logo=python)](https://pypi.org/project/fpdf2/)
[![Version - openpyxl](https://img.shields.io/badge/openpyxl-3.1.2-teal?style=for-the-badge&logo=python)](https://pypi.org/project/openpyxl/)
[![Version - pandas](https://img.shields.io/badge/pandas-2.1.4-teal?style=for-the-badge&logo=python)](https://pypi.org/project/pandas/)
[![Version - pywin32](https://img.shields.io/badge/pywin32-306-teal?style=for-the-badge&logo=python)](https://pypi.org/project/pywin32/)
[![Version - selenium](https://img.shields.io/badge/selenium-4.16.0-teal?style=for-the-badge&logo=python)](https://pypi.org/project/selenium/)
[![Version - xls2xlsx](https://img.shields.io/badge/xls2xlsx-0.2.0-teal?style=for-the-badge&logo=python)](https://pypi.org/project/xls2xlsx/)

<div align="center">
    <a href="https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Yogyakarta.svg">
        <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/Coat_of_arms_of_Yogyakarta.svg" width=25% height=25%>
    </a>
</div>

# Human Resource Manager

HR-Manager is a Python project to automate human resource-related tasks such as downloading reports, cleaning data, and formatting data into print-out ready reports.


## Project Progress

This is a simple to-do list to track the progress of the HR Manager.

### Todo

- [ ] Add Indonesian for README.md
- [ ] Add sample data/examples
- [ ] Add setup
- [ ] Add command-line menu
- [ ] Add file_handling.py or file_operations.py to store file checker method
- [ ] Fix error-handling while using convert_xls_to_xlsx

### In Progress

- [ ] Add excel format for nominatif, duk, presensi, and prestasi
- [ ] Add CLI menu

### Done ✓

- [x] Add requirements.txt
- [x] More research about MS Word and PDFs packages
- [x] Add PDF creator class
- [x] Fix text using import from texts.py
- [x] Fix PDF generation
- [x] Add WebDriverWait for login()
- [x] Wrap utils function in getters and setters
- [x] Replace parameters using getters and setters
- [x] Project Restructure
- [x] Add WebDriverWait for rekap_presensi() and rekap_prestasi()
- [x] Add download method for rekap_presensi, rekap_prestasi, nominatif, and duk
- [x] Fix webdriver for being to fast before webpage fully load certain element like dropdown
- [x] Fix webdriver to wait until file has finished downloading
- [x] Add file manager (rename, move, etc)
- [x] Fix text import from base_text.txt and user_text.txt
- [x] Fix method parameter in PDF class
- [x] Do more testing for driver class
- [x] Add alternative for converting 'xls' to 'xlsx'
- [x] Add badges in README.md
