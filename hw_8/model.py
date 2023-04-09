data_fields = ['surname', 'name', 'phone', 'comment']


def assemble_record(record_fields: list):
    record = {}
    for idx in range(len(data_fields)):
        record[data_fields[idx]] = record_fields[idx]
    return record


def add(phonebook: list, record: dict) -> None:
    phonebook.append(record)


# Функция подсчёта размера словаря. Но в данном случае достаточно просто обычной len
records_count = len


def iter_records(phonebook):
    for idx, record in enumerate(phonebook):
        yield idx, record


def get_record(data: list, rec_id: int) -> dict:
    return data[rec_id]


def search_by_surname(data: list, filter_str: str):
    """
    Search record when field 'surname' starts on filter
    :param data: phonebook records
    :param filter_str: string for search
    :return: index of record or None
    """
    for idx, record in enumerate(data):
        if record['surname'].lower().startswith(filter_str.lower()):
            return idx
    return None


def delete_record(data: list, record_num: int):
    return data.pop(record_num)


def export_data_to_file(phonebook: list, file_path: str, csv_delimiter: str):
    with open(file_path, 'w', encoding='utf-8') as file:
        for record_id, record in iter_records(phonebook):
            line = csv_delimiter.join(record[key] for key in data_fields)
            file.write(f"{line}\n")


if __name__ == "__main__":
    exit("launch main.py, not this file")
