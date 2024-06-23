import json
FILE_TEMPLATE: dict[str] = {
    'token': 'insert your token here',
    'prefix': '$'
}
FILE_KEYS = {'token', 'prefix'}
FILE_PATH: str = 'info.json'
def file_read(path: str = FILE_PATH) -> dict:
    """> Функция для прочтения файла с информацией."""
    with open(path, 'r') as file:
        return json.load(file)
def file_create(path: str = FILE_PATH, template: dict = FILE_TEMPLATE):
    """> Функция для создания файла по шаблону"""
    with open(path, 'x') as file:
        file.write(json.dumps(template, indent=4))
def check_keys(values: dict) -> bool:
    return FILE_KEYS.issubset(values.keys())
