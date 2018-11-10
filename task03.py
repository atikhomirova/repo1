# Вкратце: функция process должна обработать значения в словаре как указано в config'e.

# Убрать пробелы по краям строки 
def trim_whitespaces(dct, name):
    dct[name] = dct[name].strip() if dct.get(name) else ''
    return dct


# Заменить несколько пробелов подряд на один пробел
def remove_extra_whitespaces(dct, name):
    dct[name] = ' '.join(dct[name].split()) if dct.get(name) else ''
    return dct


# Функция process должна вернуть None, если если строка в поле name содержит подстроку arg
def skip_row_with_value(dct, name, arg):
    dct = None if arg in dct.get(name) else dct
    return dct


cleansing_functions = {'trim_whitespaces': trim_whitespaces,
                       'remove_extra_whitespaces': remove_extra_whitespaces,
                       'skip_row_with_value': skip_row_with_value
                   }


# Вызвать функцию в зависимости от того, указан ли в конфиге рядом с
# именем функции через запятую входной аргумент
def call_function_from_str(str_function, dct, name):

    arg = None

    if ':' in str_function:
        function_name, arg = str_function.split(':') #How an argument should be put in config?
        arg = arg.strip()
    else:
        function_name = str_function

    try:
        function = cleansing_functions[function_name]
    except KeyError:
        print("Specified Function Not Found")

    if arg:
        dct = function(dct, name, arg)
    else:
        dct = function(dct, name)

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
              'Address': ('skip_row_with_value: 42', 'trim_whitespaces', 'remove_extra_whitespaces')}

    # Словарь, который надо преобразовать. То есть:
    # к значению в полях "FirstName", "LastName", "Address" надо применить функцию trim_whitespaces,
    # а к значению в "Address" - еще и функции remove_extra_whitespaces и skip_row_by_value(со входным параметром 42)
    dct = {"ID" : 1 , 
           "FirstName": "  testName  ",
           "LastName": "  testLastName  ",
           "Address": "       _P    s       3       2     44_                "}
    d = process(dct)
    print(d)