class LFSR:
    @staticmethod
    def push_reg(bin_in, bool_in):
        """
        Сдвигает регистр вправо и добавляет новый бит в конец.
        :param bin_in: Двоичное состояние (строка из 0 и 1).
        :param bool_in: Новый бит (0 или 1).
        :return: Новое состояние регистра.
        """
        n = len(bin_in) - 2
        output = ""

        for i in range(n, -1, -1):
            output = bin_in[i + 1] + output

        output += str(bool_in)
        return output

    @staticmethod
    def taps2bin(taps_in):
        """
        Преобразует массив позиций включения обратной связи в двоичную строку.
        :param taps_in: Массив позиций (целые числа).
        :return: Двоичная строка длиной 20 символов.
        """
        taps_in.sort(reverse=True)
        taps = taps_in

        last = taps[0]
        y = 20 - last
        output = ""

        if y > 0:
            output += "0" * y

        j = 0
        for i in range(last):
            if (last - i) == taps[j]:
                output += "1"
                j += 1
            else:
                output += "0"

            if j > len(taps) - 1:
                break

        q = len(output)
        if q < 20:
            output += "0" * (20 - q)

        return output

    @staticmethod
    def LFSR_push(state_in, taps_in):
        """
        Выполняет одну итерацию сдвига LFSR.
        :param state_in: Текущее состояние регистра.
        :param taps_in: Двоичная строка для обратной связи.
        :return: Новое состояние регистра.
        """
        n = min(len(state_in), len(taps_in))
        tmp = sum(int(state_in[i]) * int(taps_in[i]) for i in range(n) if state_in[i].isdigit() and taps_in[i].isdigit())

        return LFSR.push_reg(state_in, tmp % 2)

    @staticmethod
    def LFSR_next(state_in, taps_in):
        """
        Выполняет 20 итераций LFSR и возвращает поток и новое состояние регистра.
        :param state_in: Текущее состояние регистра.
        :param taps_in: Двоичная строка для обратной связи.
        :return: Итоговый поток и новое состояние регистра.
        """
        state = state_in
        stream = ""

        for _ in range(20):
            state = LFSR.LFSR_push(state, taps_in)
            stream += state[-1]

        output = stream + state
        return output
