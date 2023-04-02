# 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
#
# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False
#
# 	Примеры/Тесты:
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True
#
# **Примечание.**
#
# - Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
# - Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.
#
# ```(*)``` **Усложнение.**
#
# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах.
# Эта информация возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.
#
# 	Примеры/Тесты:
# 		<function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

# Список гласных
vowels = "аиеёоуыэюя"

# Решение без усложнения
# def has_rhythm(poem: str) -> bool:
#     last_phrase_vowel_count = None
#     for phrase in poem.split():
#         current_phrase_vowel_count = 0
#         for symbol in phrase:
#             if symbol in vowels:
#                 current_phrase_vowel_count += 1
#         if last_phrase_vowel_count is not None and current_phrase_vowel_count != last_phrase_vowel_count:
#             return False
#         last_phrase_vowel_count = current_phrase_vowel_count
#     return True


# Решение с учётом усложнения
def has_rhythm(poem: str, debug: bool = True):
    vowels_info = list()
    last_phrase_vowel_count = None
    for phrase in poem.split():
        vowels_in_phrase = dict()
        current_phrase_vowel_count = 0
        for symbol in phrase:
            if symbol in vowels:
                current_phrase_vowel_count += 1
                if symbol in vowels_in_phrase:
                    vowels_in_phrase[symbol] += 1
                else:
                    vowels_in_phrase[symbol] = 1
        vowels_info.append(vowels_in_phrase)
        if last_phrase_vowel_count is not None and current_phrase_vowel_count != last_phrase_vowel_count:
            return (False, vowels_info) if debug else False
        last_phrase_vowel_count = current_phrase_vowel_count
    return (True, vowels_info) if debug else True


print(has_rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", False))
print(has_rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", True))
print(has_rhythm("пара-ра-рам рам-пум-пупам па-ре-по-дам"))
print(has_rhythm("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))
print(has_rhythm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))
print(has_rhythm("Пам-парам-пурум Пум-пурум-карам"))
