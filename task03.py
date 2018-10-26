# Вкратце: функция process должна обработать значения в словаре как указано в config'e.

# Убрать пробелы по краям строки 
def trim_whitespaces(dct, name):
    line = dct[name]
    dct[name] = line.strip()
    return dct

# Заменить несколько пробелов подряд на один пробел
def remove_extra_whitespaces(dct, name):
    line = dct[name]
    dct[name] = ' '.join(line.split())
    return dct

# Функция process должна вернуть None, если если строка в поле name содержит подстроку arg
def skip_row_by_value(dct, name, arg):
    if arg in dct[name]:
        return None
    else:
        return dct


# Выполнить eval в зависимости от того, указан ли в конфиге рядом с
# именем функции через запятую входной аргумент
def call_function_from_str(str_function, dct, name):
    if ',' in str_function:
        function, arg = str_function.split(',') #№№
        dct = eval(function)(dct, name, arg)
    else:
        dct = eval(str_function)(dct, name)
    return dct


# Функция, которая обрабатывает значения в словаре в соотв. с конфигом.
def process(dct):
    for name in config.keys():
        functions = config[name]
        for function in functions:
            dct = call_function_from_str(function, dct, name)
            if dct is None:
                return None

    return [dct] # Почему функция возвращает словарь в списке? Ни по чему, просто по тз так надо)


if __name__ == '__main__':

    # Это конфиг вида "имя поля в словаре: функция, которую надо применить к значению"
    config = {'FirstName': ('trim_whitespaces',),
              'LastName': ('trim_whitespaces',),
              'Address': ('skip_row_by_value,42', 'trim_whitespaces', 'remove_extra_whitespaces')}

    # Словарь, который надо преобразовать. То есть:
    # к значению в полях "FirstName", "LastName", "Address" надо применить функцию trim_whitespaces,
    # а к значению в "Address" - еще и функции remove_extra_whitespaces и skip_row_by_value(со входным параметром 42)
    dct = {"ID" : 1 , 
           "FirstName": "  testName  ",
           "LastName": "  testLastName  ",
           "Address": "       _P    s       3       2     44_                "}
    d = process(dct)
    print(d)