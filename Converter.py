from TextConverter import TextConverter
class Converter(TextConverter):
    @staticmethod
    def block2num(block_in):
        """
        Преобразует блок из 4 символов в целое число.
        """
        if len(block_in) == 4:
            output = 0
            pos = 1
            tmp = TextConverter.text2array(block_in)

            for i in range(3, -1, -1):
                output += pos * tmp[i]
                pos *= 32
            return output
        else:
            return -1

    @staticmethod
    def num2block(num_in):
        """
        Преобразует число в блок из 4 символов.
        """
        rem = num_in
        tmp = [0] * 4

        for i in range(4):
            tmp[3 - i] = rem % 32
            rem //= 32

        return TextConverter.array2text(tmp)

    @staticmethod
    def dec2bin(num_in):
        """
        Преобразует десятичное число в строку двоичного представления длиной 20 бит.
        """
        rem = num_in
        output = ""

        for _ in range(20):
            output = str(rem % 2) + output
            rem //= 2

        return output

    @staticmethod
    def bin2dec(bin_in):
        """
        Преобразует строку двоичного представления в десятичное число.
        """
        output = 0

        for char in bin_in:
            output = 2 * output + int(char)

        return output

    @staticmethod
    def block2bin(block_in):
        """
        Преобразует блок из 4 символов в двоичное представление длиной 20 бит.
        """
        tmp = Converter.block2num(block_in)
        return Converter.dec2bin(tmp)

    @staticmethod
    def bin2block(bin_in):
        """
        Преобразует строку двоичного представления в блок из 4 символов.
        """
        tmp = Converter.bin2dec(bin_in)
        return Converter.num2block(tmp)
