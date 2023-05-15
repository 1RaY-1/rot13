#!/usr/bin/env python3

# ROT13 Кириллическая Версия
import sys
chars_normal = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
chars_rot13 = "лмнопрстуфхцчшщъыьэюяабвгдеёжзийкЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙК "
# всякие симболы которые не шивруются
other_chars = "'\"!@#$%^&*()_+-/.><?|\\}{`~,[]=:;0123456789"
action  = ""
index = []
_help = f'''
ROT13 Русскоязычная Версия

При запуске, пишите аргумент "-en" чтобы зашивровать текст, или "-de" чтобы разшивровать текст используя ROT-13

Пример: python3 {sys.argv[0]} -en "какой-то текст"

'''

def encode_single(char:str):
    try:
        index = chars_normal.index(char)
        print(chars_rot13[index], end="")

    except ValueError:

        if char in other_chars:
            print(char, end="")
        else:
            sys.exit("Эй, что вы пишите!")

def decode_single(char:str):
    try:
        index = chars_rot13.index(char)
        print(chars_normal[index], end="")

    except ValueError:
        if char in other_chars:
            print(char, end="")
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
