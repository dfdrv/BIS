from Converter import Converter
from TextCipher import TextCipher
from CipherOperations import CipherOperations

class CaesarCipher(Converter):
    @staticmethod
    def oneside_caesar(block_in, const_in, n_in):
        """
        Выполняет односторонний шифр Цезаря для блока символов.
        :param block_in: Входной блок (строка длиной 4 символа).
        :param const_in: Константа для формирования ключей.
        :param n_in: Количество итераций шифрования.
        :return: Зашифрованный блок.
        """
        data = block_in
        c = len(const_in)

        # Формируем строку C
        C = "ТПУ" + const_in + const_in[:4]

        # Извлекаем первоначальный ключ
        key = C[3:7]

        tmp = "error"

        for i in range(n_in):
            q = ((i * 4) % c) + 3
            tmp = TextCipher.enhance_s_block(data, key, 0)
            s = Converter.block2num(tmp) % 4
            key = CipherOperations.add_txt(tmp, C[q - s : q - s + 4])

        return tmp
