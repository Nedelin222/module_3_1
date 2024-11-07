
calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string

def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    for i in range(len(list_to_search)):
        if string == list_to_search[i].upper():
            finish = True
            break
        else:
            finish = False
            continue
    return finish

print(string_info('Прикол'))
print(string_info('Аргумент'))
print(is_contains('Собака', ['1234', 'СОбаКА', 'ЗИЛ', 'тормозил']))
print(is_contains('Дерево', ['8645', 'ПРоГУлка', 'Чашка', 'СПАТЬ', 'хОчЕТСЯ']))

print(calls)
