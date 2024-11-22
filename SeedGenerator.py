from CaesarCipher import CaesarCipher
from Converter import Converter

class SeedGenerator(CaesarCipher):
    @staticmethod
    def make_seed(block_in):
        """
        Генерирует три строки на основе входного блока.
        :param block_in: Входной блок текста.
        :return: Список из трех строк, представляющих seed'ы.
        """
        str1 = "ПЕРВЫЙ_ГЕНЕРАТОР"
        str2 = "ВТОРОЙ_ГЕНЕРАТОР"
        str3 = "ТРЕТИЙ_ГЕНЕРАТОР"

        out0 = CaesarCipher.oneside_caesar(block_in, str1, 10)
        out1 = CaesarCipher.oneside_caesar(block_in, str2, 10)
        out2 = CaesarCipher.oneside_caesar(block_in, str3, 10)

        return [out0, out1, out2]

    @staticmethod
    def check_seed(block_in):
        """
        Проверяет и корректирует seed-блок, чтобы избежать совпадений.
        :param block_in: Входной блок текста длиной 16 символов.
        :return: Корректированный блок текста.
        """
        C = "ОТВЕТСТВЕННЫЙ_ПОДХОД"
        T = [block_in[i * 4:(i + 1) * 4] for i in range(4)]

        for j in range(3):
            for i in range(j + 1, 4):
                if T[i] == T[j]:
                    T[i] = CaesarCipher.oneside_caesar(T[j], C, j + 2 * i)

        return "".join(T)

    @staticmethod
    def seed2bins(array_in):
        """
        Преобразует список seed'ов в их двоичные представления.
        :param array_in: Список seed'ов.
        :return: Список из трех строк, представляющих двоичные представления seed'ов.
        """
        out1 = Converter.block2bin(array_in[0])
        out2 = Converter.block2bin(array_in[1])
        out3 = Converter.block2bin(array_in[2])

        return [out1, out2, out3]


