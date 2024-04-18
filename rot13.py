#!/usr/bin/env python3

# ROT13 Кириллическая Версия. С поддержкой латинского (английского) алфавита
# Автор: github.com/1RaY-1
# Дата последнего изменения: Четверг, 11 Апреля, 2024

import sys

cir_chars_normal = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
cir_chars_rot13 = "мнопрстуфхцчшщъыьэюяабвгдеёжзийклМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛ "

# Можно еще работать с Латиницей (Англ. алфавит)
latin_chars_normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
latin_chars_rot13 = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM "

# всякие симболы которые не шивруются
other_chars = "'\"!@#$%^&*()_+-/.><?|\\}{`~,[]=:;0123456789"
action  = ""
index = []
_help = f'''
ROT13 Русскоязычная Версия

При запуске, пишите аргумент "-en" чтобы зашифровать текст, или "-de" чтобы разшифровать текст используя ROT-13

Шифрование: python3 {sys.argv[0]} -en "Текст тут"
Расшифровка: python3 {sys.argv[0]} -de "Ясчюя яая"
'''

def encode_single(char:str):
    try:
        index = cir_chars_normal.index(char)
        print(cir_chars_rot13[index], end="")

    except ValueError:
#       see if characters aren't cyrrilic
        if char in latin_chars_normal:
            index = latin_chars_normal.index(char)
            print(latin_chars_rot13[index], end="")
#       detect some symbols
        elif char in other_chars:
            print(char, end="")
#       detect new line
        elif "\n" in char:
            print("\n", end="")
        else:
            sys.exit("Эй, что вы пишите!")

def decode_single(char:str):
    try:
        index = cir_chars_rot13.index(char)
        print(cir_chars_normal[index], end="")

    except ValueError:
        if char in latin_chars_rot13:
            index = latin_chars_rot13.index(char)
            print(latin_chars_normal[index], end="")
        elif char in other_chars:
            print(char, end="")
        elif "\n" in char:
            print("\n", end="")
        else:
            sys.exit("Эй, что вы пишите!")
def main():
    if action == "encode":
        for i in sys.argv[2]:
            encode_single(i)
    elif action == "decode":
        for i in sys.argv[2]:
            decode_single(i)
    print()
if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit(_help)

    else:
        if sys.argv[1] == "-en" or sys.argv[1] == "--encode": action = "encode"

        elif sys.argv[1] == "-de" or sys.argv[1] == "--decode": action = "decode"

        else: sys.exit("Что-то не так!\n" + _help)

        main()
        
