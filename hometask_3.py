# -*- coding: utf-8 -*-
import datetime
import hashlib
import os


def logger(func):
    def wrapper(*args, **kwargs):
        today = datetime.datetime.today()
        with open('log.txt', 'a', encoding='utf-8') as f:
            print(f'Имя функции: {func.__name__}', file=f)
            print(f'Дата и время вызова: {today.strftime("%Y-%m-%d %H:%M:%S")}', file=f)
            pos_args = [str(arg) for arg in args]
            kw_args = [':'.join((str(key), str(val))) for key, val in kwargs.items()]
            if args:
                print(f"Позиционные аргументы: {' '.join(pos_args)}", file=f)
            if kwargs:
                print(f"Именованные аргументы: {' '.join(kw_args)}", file=f)
            result = func(*args, **kwargs)
            print(f'Значение, возвращенное функцией: {result}', file=f)
        return func

    return wrapper


def add_log_path(log_path_and_name):
    def decor(func):
        def wrapper(*args, **kwargs):
            today = datetime.datetime.today()
            with open(log_path_and_name, 'a', encoding='utf-8') as f:
                print(f'Имя функции: {func.__name__}', file=f)
                print(f'Дата и время вызова: {today.strftime("%Y-%m-%d %H:%M:%S")}', file=f)
                pos_args = [str(arg) for arg in args]
                kw_args = [':'.join((str(key), str(val))) for key, val in kwargs.items()]
                if args:
                    print(f"Позиционные аргументы: {' '.join(pos_args)}", file=f)
                if kwargs:
                    print(f"Именованные аргументы: {' '.join(kw_args)}", file=f)
                result = func(*args, **kwargs)
                print(f'Значение, возвращенное функцией: {result}', file=f)
                print('*' * 78, file=f)
            return func

        return wrapper

    return decor


def main():
    log_path = input('Путь к каталогу логов:')
    log_name = input('Имя лога:')
    file_to_hash = input('Имя файла для расчета хеш-сумм:')
    # TODO: проверка путей  и имен файлов
    full_path = os.path.join(log_path, log_name)

    @add_log_path(full_path)
    def get_file_line_md5(file: str):
        hashes = set()
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                md5_hash = hashlib.md5()
                md5_hash.update(line.encode(encoding='utf-8'))
                hashes.add(md5_hash.hexdigest())
        return hashes

    get_file_line_md5(file_to_hash)


if __name__ == '__main__':
    main()
