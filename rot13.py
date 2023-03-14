#!/usr/bin/env python3

# ROT13  Русская Версия (cyrillic)

import sys

# Отступ не убирать
chars_normal = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
chars_rot13 = "лмнопрстуфхцчшщъыьэюяабвгдеёжзийкЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙК "

action  = ""
index = []

_help = f'''При запуске, пишите аргумент "-en" чтобы зашивровать след. текст, или "-de"
чтобы разшивровать след. текст в ROT-13

Пример: python3 {sys.argv[0]} -en "Текст тут"
'''

# Encode
def encode_single(char:str):
    try:
        index = chars_normal.index(char)
        print(chars_rot13[index], end="")
    except ValueError:
#        Если написать число а не букву, то вот так получается, тоесть плюсуем 2
#       1234567890
#       3456789012
        if char.isnumeric() == True:
            print(int(char) + 2, end="")
        else:
            sys.exit("Эй, что вы пишите!")
# Decode
def decode_single(char:str):
    try:
        index = chars_rot13.index(char)
        print(chars_normal[index], end="")
    except ValueError:
#        А сдесь минусуем 2
        if char.isnumeric() == True:
            print(int(char) - 2, end="")
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
