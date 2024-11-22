class TextConverter:
    # Храним русский телеграфный алфавит в виде строки
    alphabet = "_АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ"

    @staticmethod
    def num2sym(n):
        """
        Возвращает символ из строки алфавита по индексу n.
        """
        return TextConverter.alphabet[n]

    @staticmethod
    def sym2num(symbol):
        """
        Возвращает индекс символа symbol в строке телеграфного алфавита.
        """
        symbol_upper = symbol.upper()
        return TextConverter.alphabet.find(symbol_upper)

    @staticmethod
    def text2array(text):
        """
        Преобразует текст в массив индексов символов из алфавита.
        """
        return [TextConverter.sym2num(char) for char in text]

    @staticmethod
    def array2text(arr):
        """
        Преобразует массив индексов символов обратно в текст.
        """
        return ''.join(TextConverter.num2sym(num) for num in arr)
