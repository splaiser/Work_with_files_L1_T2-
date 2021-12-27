from pathlib import Path
import sys, os

source_dir = Path('D:/Python/Netology/work_with_files/lesson_1_task_2/')
files = source_dir.glob('*.txt')
file_list = []


def get_files(files):
    for file in files:
        with file.open('r', encoding='UTF-8') as file_handle:
            lenght_file = sum(1 for line in open(file, 'r', encoding='UTF-8'))
            filename = os.path.basename(file)
            file_list.append({'filename': filename, 'lenght': lenght_file, 'text': file_handle.read()})


def get_result():
    get_files(files)
    with open('result', 'w', encoding='UTF-8') as res:
        file_list.sort(key=lambda file_list: file_list['lenght'])
        for dict in file_list:
            res.write(str(dict.get('filename') + '\n'))
            res.write(str(dict.get('lenght')) + '\n')
            res.write(str(dict.get('text') + '\n'))


get_result()
