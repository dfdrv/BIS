from LFSR import LFSR

class ASLFSR(LFSR):
    @staticmethod
    def ASLFSR_push(state_in, taps_in):
        """
        Выполняет один шаг асинхронного LFSR.
        :param state_in: Список строк, представляющих состояния трех LFSR.
        :param taps_in: Список строк, представляющих тэпы трех LFSR.
        :return: Кортеж, содержащий потоковый бит и новые состояния LFSR.
        """
        lfsr0 = LFSR.LFSR_push(state_in[0], taps_in[0])
        lfsr1 = LFSR.LFSR_push(state_in[1], taps_in[1])
        lfsr2 = LFSR.LFSR_push(state_in[2], taps_in[2])

        # Выбор бита потока на основе 19-го бита LFSR0
        stream = lfsr1[-1] if lfsr0[-1] == '0' else lfsr2[-1]

        output_state = [lfsr0, lfsr1, lfsr2]

        return stream, output_state

    @staticmethod
    def ASLFSR_next(state_in, taps_in):
        """
        Выполняет 20 шагов асинхронного LFSR.
        :param state_in: Список строк, представляющих начальные состояния трех LFSR.
        :param taps_in: Список строк, представляющих тэпы трех LFSR.
        :return: Кортеж, содержащий итоговый поток и новые состояния LFSR.
        """
        state_set = state_in
        stream = ""

        for _ in range(20):
            stream_bit, state_set = ASLFSR.ASLFSR_push(state_set, taps_in)
            stream += stream_bit

        return stream, state_set
