from TextConverter import TextConverter
class CipherOperations(TextConverter):
    @staticmethod
    def add_s(a, b):
        """
        Суммирует индексы символов a и b в алфавите и возвращает соответствующий символ.
        """
        index = (TextConverter.sym2num(a) + TextConverter.sym2num(b)) % 32
        return TextConverter.num2sym(index)

    @staticmethod
    def sub_s(a, b):
        """
        Вычитает индекс символа b из a в алфавите и возвращает соответствующий символ.
        """
        index = (32 + TextConverter.sym2num(a) - TextConverter.sym2num(b)) % 32
        return TextConverter.num2sym(index)

    @staticmethod
    def add_txt(T1_IN, T2_IN):
        """
        Выполняет побуквенную операцию сложения двух строк T1_IN и T2_IN.
        """
        output = ""
        m = min(len(T1_IN), len(T2_IN))

        # Определяем более длинную строку
        T_IN = T1_IN if len(T1_IN) > len(T2_IN) else T2_IN
        M = len(T_IN)

        # Сложение символов в пределах длины m
        for i in range(m):
            output += CipherOperations.add_s(T1_IN[i], T2_IN[i])

        # Добавляем оставшиеся символы из более длинной строки
        if M > m:
            output += T_IN[m:]

        return output

    @staticmethod
    def sub_txt(T1_IN, T2_IN):
        """
        Выполняет побуквенную операцию вычитания двух строк T1_IN и T2_IN.
        """
        output = ""
        m = min(len(T1_IN), len(T2_IN))
        flag = 0  # Указывает, какая строка длиннее

        # Определяем более длинную строку
        if len(T1_IN) > len(T2_IN):
            T_IN = T1_IN
        else:
            T_IN = T2_IN
            flag = 1

        M = len(T_IN)

        # Вычитание символов в пределах длины m
        for i in range(m):
            output += CipherOperations.sub_s(T1_IN[i], T2_IN[i])

        # Обработка оставшихся символов
        if M > m:
            for i in range(m, M):
                if flag == 1:
                    output += CipherOperations.sub_s('_', T_IN[i])
                else:
                    output += CipherOperations.sub_s(T_IN[i], '_')

        return output
