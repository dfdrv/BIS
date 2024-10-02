from BaseUtils import BaseUtils
from Cezar import Cesar
from SBlockImpl import SBlockImpl

def main():
    util = BaseUtils()
    cesar = Cesar(util)
    s_block = SBlockImpl(util, cesar)

    while True:
        print("Для выхода из приложения напишите q")
        print("Для работы с шифром Цезаря напишите c")
        print("Для работы с S-блоком напишите s")
        input_text = input().lower()

        if input_text == "q":
            return
        elif input_text == "c":
            c(cesar)
        elif input_text == "s":
            s(s_block)

        print("--------------------------------")

def c(c: Cesar):
    print("Введите слово:")
    word = input()
    print("Введите ключ:")
    offset = input()

    frw = c.frw_Cesar(word, offset)
    inv = c.inv_Cesar(frw, offset)
    print(f"Зашифрованное слово: {frw} | Обратно расшифрованное слово: {inv}\n")

def s(s: SBlockImpl):
    print("Введите блок не более 4 символов:")
    txt = input()
    print("Введите ключ:")
    key = input()
    print("Введите смещение:")
    offset = int(input())

    frw = s.frw_S(txt, key, offset)
    inv = s.inv_S(frw, key, offset)
    print(f"Зашифрованное слово: {frw} | Обратно расшифрованное слово: {inv}\n")

if __name__ == "__main__":
    main()
