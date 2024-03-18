from pathlib import Path
from pprint import pprint

def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
               dict_cats_info = {}
               dict_cats_info['id'], dict_cats_info['name'], dict_cats_info['age'] = line.strip().split(',')
               cats.append(dict_cats_info)
               
        return cats

    except Exception as e:
        pprint('There is a problem with the file: {e}')

cats_info = get_cats_info(Path('cats_info.txt'))
pprint (cats_info)