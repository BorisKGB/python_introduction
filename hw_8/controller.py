import model
import view
import os.path


def start(previous_data: list = None) -> None:
    if not previous_data:
        previous_data = list()
    # Опционально тут должен быть какой-то validate для previous_data, скорее всего model.validate_data(previous_data)
    # Опционально в меню/параметрах должны быть пункты для задания доп параметров, но я просто укажу их тут явно
    in_file_elements_delimiter = "#"
    print_elements_delimiter = " "
    user_menu(previous_data, in_file_elements_delimiter, print_elements_delimiter)


def user_menu(phonebook: list, csv_delimiter: str, print_delimiter: str) -> None:
    while True:
        user_input = view.menu()
        if user_input == "n":
            new_record(phonebook)
        elif user_input == "p":
            # первый вариант делал enumerate напрямую обращаясь к phonebook, но
            # мне показалось, что правильнее спрашивать данные у model
            if model.records_count(phonebook) > 0:
                for record_id, record in model.iter_records(phonebook):
                    view.print_record(record_id, model.get_record(phonebook, record_id), print_delimiter)
            else:
                view.no_data()
        elif user_input == "i":
            import_records(phonebook, csv_delimiter)
        elif user_input == "e":
            export_records(phonebook, csv_delimiter)
        elif user_input == "s":
            user_input, record_id = search_record(phonebook)
            if type(record_id) is int:
                view.print_record(record_id, model.get_record(phonebook, record_id), print_delimiter)
            else:
                view.records_not_found(user_input)
        elif user_input == "d":
            user_input, record_id = search_record(phonebook)
            if type(record_id) is int:
                view.record_deleted(model.delete_record(phonebook, record_id), record_id, print_delimiter)
            else:
                view.records_not_found(user_input)
        elif user_input == "u":
            update_record(phonebook)
        elif user_input == "q":
            view.exit_message()
            break
        else:
            view.incorrect_menu_choice()


def new_record(phonebook: list) -> None:
    """Ask user for data fields, validate them and if all of them is correct append record to phonebook"""
    # 'surname': "Иванов", 'name': "Иван", 'phone': "89234145", 'commentary': "работник"
    record_data = []
    # Считаю, что такая структура позволит мне абстрагироваться
    # от кол-ва полей и функций их получения/проверки/сообщений об ошибках
    for data_field, ask_func, validate_func, \
            incorrect_func in zip(model.data_fields, view.data_field_ask_funcs,
                                  data_field_validate_funcs, view.data_field_incorrect_funcs):
        user_input = ask_func()
        if validate_func(user_input):
            record_data.append(user_input)
        else:
            incorrect_func()
            return
    model.add(phonebook, model.assemble_record(record_data))


def search_record(phonebook: list) -> tuple:
    user_input = view.ask_filter_string()
    return user_input, model.search_by_surname(phonebook, user_input)


def update_record(phonebook: list) -> None:
    user_input, record_id = search_record(phonebook)
    if type(record_id) is int:
        record = model.get_record(phonebook, record_id)
        new_record_data = []
        for data_field, ask_func, validate_func, \
                incorrect_func, old_value in zip(model.data_fields, view.data_field_ask_funcs,
                                                 data_field_validate_funcs, view.data_field_incorrect_funcs,
                                                 record.values()):
            user_input = ask_func(old_value)
            if validate_func(user_input):
                new_record_data.append(user_input)
            else:
                incorrect_func()
                return None
        phonebook[record_id] = model.assemble_record(new_record_data)
        # view.print_record(record_id, model.get_record(phonebook, record_id))
    else:
        view.records_not_found(user_input)
    return None


def import_records(phonebook: list, csv_delimiter: str = ',') -> None:
    """Check file path and try to get records from it
    :param csv_delimiter: custom delimiter for data in each file line"""
    file_path = view.ask_file_path()
    if os.path.isfile(file_path):
        imported_count = 0
        # Силами view получаю из файла уже разбитые по delimiter строки и тут их валидирую и добавляю к данным
        for data in view.file_read(file_path, csv_delimiter):
            if len(data) != len(model.data_fields):
                view.file_import_failed(file_path, imported_count)
                return None
            record = list()
            for element, validate_func in zip(data, data_field_validate_funcs):
                if validate_func(element):
                    record.append(element)
                else:
                    view.file_import_failed(file_path, imported_count)
                    return None
            model.add(phonebook, model.assemble_record(record))
            imported_count += 1
        view.file_import_success(file_path, imported_count)
    else:
        view.file_not_exist(file_path)
        return None


def export_records(phonebook: list, csv_delimiter: str = ',') -> None:
    """
    request data export
    :param phonebook: data source
    :param csv_delimiter: delimiter for element fields in file
    """
    file_path = os.path.abspath(view.ask_file_path())
    parent_dir = os.path.dirname(file_path)
    # check if we can even create this file
    if not(os.path.isdir(parent_dir) and os.access(parent_dir, os.W_OK)):
        view.file_unable_to_create(file_path)
        return None
    # check if file already_exist
    if os.path.isfile(file_path):
        user_input = view.file_allow_replace(file_path).lower()
        if user_input != "y":
            return None
    model.export_data_to_file(phonebook, file_path, csv_delimiter)
    view.file_export_success(file_path)
    return None


# функции валидации введённых данных
# В данном случае ни каких требований к данным не представлено
def validate_surname(text: str) -> bool: return True
def validate_name(text: str) -> bool: return True
def validate_phone(text: str) -> bool: return True
def validate_comment(text: str) -> bool: return True
# список функций валидации в порядке следования в соответствии с model.data_fields, для удобства перебора данных записи
data_field_validate_funcs = [validate_surname, validate_name, validate_phone, validate_comment]


if __name__ == "__main__":
    exit("launch main.py, not this file")
