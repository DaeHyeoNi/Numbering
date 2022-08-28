import re


class FileControl:
    def __init__(self, file_path):
        self.file_path = file_path
        self.list_num = 0

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = ''
            for i in f.readlines():
                # empty line pass
                if i == '\n':
                    data += '\n'
                    continue

                # if line already has numbering replace it.
                if re.search(r'^\d+\.', i):
                    self.list_num += 1
                    i = re.sub(r'^\d+\.', '', i).strip() + '\n'
                    data += f'{self.list_num}. {i}'
                else:
                    self.list_num += 1
                    data += f'{self.list_num}. {i}'
            return data

    def write_file(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(data)
