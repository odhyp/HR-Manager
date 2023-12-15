from src.spt.utils import get_base_text_path, get_user_text_path


class TextGenerator:
    def __init__(self):
        self.base_text = []
        self.user_text = []
        self.populate_list('base_text')
        self.populate_list('user_text')


    def populate_list(self, list_type):
        if list_type == 'base_text':
            with open(get_base_text_path(), 'r') as f:
                for line in f:
                    self.base_text.append(line.rstrip('\n'))
        elif list_type == 'user_text':
            with open(get_user_text_path(), 'r') as f:
                for line in f:
                    self.user_text.append(line.rstrip('\n'))
        else:
            return None
