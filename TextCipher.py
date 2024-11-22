class TextCipher:
    @staticmethod
    def caesar_cipher_char(text, key):
        return TextCipher.add_s(text, key)

    @staticmethod
    def inv_caesar_cipher_char(text, key):
        return TextCipher.sub_s(text, key)

    @staticmethod
    def caesar_cipher_text(text, key):
        result = ""
        for char in text:
            result += TextCipher.caesar_cipher_char(char, key[0])
        return result

    @staticmethod
    def inv_caesar_cipher_text(text, key):
        result = ""
        for char in text:
            result += TextCipher.inv_caesar_cipher_char(char, key[0])
        return result

    @staticmethod
    def vigenere_cipher(text, key, shift):
        result = ""
        poly_key = "_"
        for i, char in enumerate(text):
            poly_key = TextCipher.caesar_cipher_char(poly_key, key[(i + shift) % len(key)])
            result += TextCipher.caesar_cipher_char(char, poly_key)
        return result

    @staticmethod
    def inv_vigenere_cipher(text, key, shift):
        result = ""
        poly_key = "_"
        for i, char in enumerate(text):
            poly_key = TextCipher.caesar_cipher_char(poly_key, key[(i + shift) % len(key)])
            result += TextCipher.inv_caesar_cipher_char(char, poly_key)
        return result

    @staticmethod
    def s_block_cipher(text, key, shift):
        if len(text) == 4:
            return TextCipher.vigenere_cipher(text, key, shift)
        else:
            return "input_error"

    @staticmethod
    def inv_s_block_cipher(text, key, shift):
        if len(text) == 4:
            return TextCipher.inv_vigenere_cipher(text, key, shift)
        else:
            return "input_error"

    @staticmethod
    def improve_s_block_cipher(text, key, shift):
        t = key
        while shift > len(t) - 4:
            t += t
        new_key = t[shift:shift + 4]
        key_arr = TextCipher.text2array(new_key)
        text_arr = TextCipher.text2array(text)
        q = sum(key_arr) % 4

        for i in range(3):
            j = (q + i + 1) % 4
            l = (q + i) % 4
            text_arr[j] = (text_arr[j] + text_arr[l]) % 32

        return TextCipher.array2text(text_arr)

    @staticmethod
    def inv_improve_s_block_cipher(text, key, shift):
        t = key
        while shift > len(t) - 4:
            t += t
        new_key = t[shift:shift + 4]
        key_arr = TextCipher.text2array(new_key)
        text_arr = TextCipher.text2array(text)
        q = sum(key_arr) % 4

        for i in range(2, -1, -1):
            j = (q + i + 1) % 4
            l = (q + i) % 4
            text_arr[j] = (32 + text_arr[j] - text_arr[l]) % 32

        return TextCipher.array2text(text_arr)

    @staticmethod
    def enhance_s_block(text, key, shift):
        if len(text) == 4:
            new_text = TextCipher.s_block_cipher(text, key, shift)
            return TextCipher.improve_s_block_cipher(new_text, key, shift)
        else:
            return "input_error"

    @staticmethod
    def inv_enhance_s_block(text, key, shift):
        if len(text) == 4:
            new_text = TextCipher.inv_improve_s_block_cipher(text, key, shift)
            return TextCipher.inv_s_block_cipher(new_text, key, shift)
        else:
            return "input_error"

    # Дополнительные методы, используемые в коде
    @staticmethod
    def add_s(text, key):
        # Реализация логики добавления (заменить примером)
        return chr((ord(text) + ord(key)) % 256)

    @staticmethod
    def sub_s(text, key):
        # Реализация логики вычитания (заменить примером)
        return chr((ord(text) - ord(key)) % 256)

    @staticmethod
    def text2array(text):
        return [ord(c) for c in text]

    @staticmethod
    def array2text(array):
        return ''.join(chr(c) for c in array)
