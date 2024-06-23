"""Модуль для повторяющихся кодовых конструкций"""

# TODO: Разобраться с значениями этих чисел
CRITICAL_EXIT_CODE: int = 1 
def handle_critical(error: str = '> Неизвестная ошибка!', exitCode: int = CRITICAL_EXIT_CODE):
    print(error, "> Завершаем выполнение программы...", sep='\n')
    exit(exitCode)