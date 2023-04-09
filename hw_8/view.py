# Группа функций для получения полей записи от пользователя
# С учётом возможного default_value для переиспользования в update логике
def ask_surname(default_value: str = ""):
    return input(f"Введите фамилию {f'({default_value})' if default_value else ''} > ") or default_value
def ask_name(default_value: str = ""):
    return input(f"Введите имя {f'({default_value})' if default_value else ''} > ") or default_value
def ask_phone(default_value: str = ""):
    return input(f"Введите номер телефона {f'({default_value})' if default_value else ''} > ") or default_value
def ask_comment(default_value: str = ""):
    return input(f"Введите комментарий {f'({default_value})' if default_value else ''} > ") or default_value
# И список этих функций для удобной их итерации
data_field_ask_funcs = [ask_surname, ask_name, ask_phone, ask_comment]

# Группа функций для сообщения incorrect input для полей записи
def incorrect_surname() -> None:
    print("Неправильно введена фамилия")
def incorrect_name() -> None:
    print("Неправильно введено имя")
def incorrect_phone() -> None:
    print("Неправильно введен номер телефона")
def incorrect_comment() -> None:
    print("Неправильно введена комментарий")
# И список этих функций для удобной их итерации
data_field_incorrect_funcs = [incorrect_surname, incorrect_name, incorrect_phone, incorrect_comment]


def menu() -> str:
    """
    Print menu and wait user input
    """
    # Заменил числовые обозначения на буквенные чтобы не переделывать каждый раз нумерацию списка
    print("="*10)
    print("Выберите действия")
    print("(n)ew record: Создать запись")
    print("(s)earch record: Найти контакт по начальной части фамилии")
    print("(d)elete record: Удалить запись по начальной части фамилии")
    print("(u)pdate record: Изменить запись")
    print("(p)rint all: Вывести имеющиеся данные")
    print("(e)xport data: Экспортировать данные в файл")
    print("(i)mport data: Импортировать данные из файла")
    print("(q)uit: Выход")
    user_input = input("Введите действие > ")
    print("=" * 10)
    return user_input

def ask_file_path():
    return input("Введите имя файла > ")

def ask_filter_string():
    return input("Введите первую часть фамилии для поиска записи > ")

def records_not_found(filter: str) -> None:
    print(f"Записей начинающихся с {filter} не найдено")

def record_deleted(record: dict, record_id: int, elements_separator: str = ' ') -> None:
    print("Удалена запись:")
    print_record(record_id, record, elements_separator)

def print_record(record_id, record_data: dict, elements_separator: str = ' ') -> None:
    print(f"{record_id}:", *(f"{key}: '{val}'" for key, val in record_data.items()), sep=elements_separator)

def no_data() -> None:
    print("Записей нет")

def incorrect_menu_choice() -> None:
    print("Недопустимый пункт меню, попробуйте ещё раз")

def file_not_exist(path: str) -> None:
    print(f"Файла по пути '{path}' нет")

def file_allow_replace(path: str) -> str:
    return input(f"Файл {path} уже существует, перезаписать? (y/N) > ") or 'n'

def file_unable_to_create(path) -> None:
    print(f"Невозможно создать файл по пути '{path}'")

def file_import_success(path: str, imported_count:int = 0) -> None:
    print(f"Успешно получено {imported_count} строк из файла '{path}'")

def file_import_failed(path: str, imported_count:int = 0) -> None:
    print(f"Файл '{path}' содержит несовместимую структуру, импортировано только первые {imported_count} строк")

def file_export_success(path: str) -> None:
    print(f"Данные успешно экспортированы в файл '{path}'")

def file_read(path: str, csv_delimiter) -> iter:
    """
    iterator for parsed file lines created from example on
    https://www.askpython.com/python/python-yield-examples
    :param path: file path
    :param csv_delimiter: custom delimiter for data in each file line
    """
    text_file = open(path, 'r')
    while True:
        line_data = text_file.readline()
        if not line_data:
            text_file.close()
            break
        yield line_data.strip().split(csv_delimiter)


def exit_message() -> None:
    print("Завершение работы...")


if __name__ == "__main__":
    exit("launch main.py, not this file")
