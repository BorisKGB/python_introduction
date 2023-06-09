# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv.
# Доделать задание вебинара и реализовать  Update, Delete
#
# Информация о человеке: Фамилия, Имя, Телефон, Описание
#
# Корректность и уникальность данных не обязательны.
#
# ##### Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
#     Выберите наиболее удобную структуру данных для хранения справочника.
#
# 2) CRUD: Create, Read, Update, Delete
#
# - Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# - Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека.
#         Берем первое совпадение по фамилии.
# - Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# - Delete: Удаление записи из справочника. Выбор - как в Read.
#
# 3) экспорт данных в текстовый файл формата csv
#
# 4) импорт данных из текстового файла формата csv
#
#
# Используйте функции для реализации значимых действий в программе
#
# ```(*)``` **Усложнение.**
#
# - Сделать тесты для функций
# - Разделить на model-view-controller

# Подсмотрел структуру model-view-controller в эталонном решении и попытался её повторить.
# Пример структуры данных справочника
# data = [{'surname': "Иванов", 'name': "Иван", 'phone': "89234145", 'commentary': "работник"}]

# Усложнение "Сделать тесты для функций" пропущено,
# не смог адаптировать из эталонного решения и решил не переусложнять код

from controller import start as controller_start

if __name__ == "__main__":
    controller_start()
    # user_menu(phonebook)
