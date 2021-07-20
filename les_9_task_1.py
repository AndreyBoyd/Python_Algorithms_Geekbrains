# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1()
# или любой другой из модуля hashlib задача считается не решённой.

import hashlib


def rabin_karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) >= len(subs), 'Подстрока длиннее строки'

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == subs:
                return i
    return -1


def main():
    s_1 = input('Введите строку: ')
    s_2 = input('Введите подстроку для поиска: ')
    print(rabin_karp(s_1, s_2))


def task(s: str):
    len_subs = 1
    result_set = set()
    for z in range(1, len(s)):
        for j in range(0, len(s)-len_subs+1):
            subs = s[j:j+len_subs]
            pass
            len_sub = len(subs)
            h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

            for i in range(len(s) - len_sub + 1):
                if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

                    if s[i:i + len_sub] == subs:
                        result_set.add(subs)
                        # print(subs)
        len_subs += 1
    print(f'Кол-во уникальных подстрок: {len(result_set)}')
    print(result_set)


if __name__ == "__main__":
    string = input("Введите текст: ")
    task(string.replace("", ""))
