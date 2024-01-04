import os
import time


class Menu:
    def __init__(self):
        pass

    def clear(self):
        os.system("cls")

    def display_menu_screen(self):
        self.clear()

        print("")
        print("[1] Download Nominatif")
        print("[2] Download DUK")
        print("[3] Download Rekap Harian")
        print("[4] Download Rekap Prestasi")
        print("[0] Exit")
        print("")

    def menu_screen_selection(self):
        while True:
            self.display_menu_screen()

            choice = str(input("> "))

            if choice == '0':
                print("Good bye...")
                time.sleep(1)
                quit()
                time.sleep(5)
            elif choice == '1':
                quit()
            elif choice == '2':
                print("Option 2")
            elif choice == '3':
                print("Option 3")
            elif choice == '4':
                print("Option 4")
            else:
                self.menu_screen_selection()
                print("Invalid choice")

    def start(self):
        self.menu_screen_selection()
