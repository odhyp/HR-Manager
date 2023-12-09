from src.spt.utils import get_base_text_path, get_user_text_path


class TextGenerator:
    base_text_path = get_base_text_path()
    
    def __init__(self):
        self.text_list = []
        self.read_txt_file()


    def read_txt_file(self, file_path=base_text_path):
        with open(file_path, 'r') as f:
            for line in f:
                self.text_list.append(line.rstrip('\n'))

    def get_text(self):
        return self.text_list
