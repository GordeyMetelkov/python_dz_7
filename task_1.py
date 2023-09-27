# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import string
from random import randint, sample, randbytes
def create_file(
        extention,
        count_files = 42,
        min_len_name = 6,
        max_len_name = 30,
        min_bytes = 256,
        max_bytes = 4096
):
    for _ in range(count_files):
        name = "".join(sample(string.ascii_lowercase + string.ascii_lowercase, randint(min_len_name, max_len_name)))
        with open(f'{name}.{extention}', 'wb') as f:
            f.write(randbytes(randint(min_bytes, max_bytes)))

def create_file_extention(extentions: list, count_files: int):
    tmp_count = 0
    while tmp_count < count_files:
        extention_file = extentions[randint(0, len(extentions) - 1)]
        extention_count = randint(0, count_files - tmp_count)
        tmp_count += extention_count
        create_file(extention=extention_file, count_files=extention_count)

def sort_files():
    music_files = ['mp3', 'wav', 'midi']
    text_files = ['txt', 'md', 'docx']
    picture_files = ['jpeg', 'png']
    for i in os.listdir('.'):
        if i.split('.')[-1] in music_files:
            if not os.path.isdir('music'):
                os.mkdir('music')
            os.replace(i, os.path.join(os.getcwd(), "music", i))
        elif i.split('.')[-1] in text_files:
            if not os.path.isdir('text'):
                os.mkdir('text')
            os.replace(i, os.path.join(os.getcwd(), "text", i))
        elif i.split('.')[-1] in picture_files:
            if not os.path.isdir('pictures'):
                os.mkdir('pictures')
            os.replace(i, os.path.join(os.getcwd(), "pictures", i))

# all_extentions = ['txt', 'md', 'docx', 'mp3', 'wav', 'midi', 'jpeg', 'png']
# create_file_extention(all_extentions, 50)
# sort_files()

