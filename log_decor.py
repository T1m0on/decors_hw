import datetime


def logger(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'''\nДата вызова функции {old_function.__name__} - {datetime.datetime.now().strftime('%d-%m-%Y время %H:%M:%S')}, 
            аргументы {args, kwargs}, 
            значение {result}\n''')
        return result
    return new_function

def params_logger(path):
    def __loger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'''\nДата вызова функции {old_function.__name__} - {datetime.datetime.now().strftime('%d-%m-%Y время %H:%M:%S')}, 
                аргументы {args, kwargs}, 
                значение {result}\n''')
            return result
        return new_function
    return __loger
