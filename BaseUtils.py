class BaseUtils:
    def sym2num(self, symIn: str) -> int:
        if len(symIn) > 1:
            raise Exception("Passed more than 1 symbol")
        tmp = [ord(symIn[0])]
        if tmp[0] == 95:  # ASCII code for '_'
            return 0
        if tmp[0] > 1066:
            return tmp[0] - 1039 - 1
        return tmp[0] - 1039

    def num2sym(self, numIn: int) -> str:
        if numIn == 0:
            return "_"
        if numIn > 26:
            return chr(numIn + 1039 + 1)
        return chr(numIn + 1039)

    def text2array(self, txtIn: str) -> list[int]:
        return [self.sym2num(element) for element in txtIn]

    def array2text(self, arrIn: list[int]) -> str:
        return ''.join(self.num2sym(i) for i in arrIn)

    def addS(self, s1In: str, s2In: str) -> str:
        temp = self.sym2num(s1In) + self.sym2num(s2In)
        return self.num2sym(temp % 32)

    def subS(self, s1In: str, s2In: str) -> str:
        temp = self.sym2num(s1In) - self.sym2num(s2In) + 32
        return self.num2sym(temp % 32)

    def addTxt(self, t1In: str, t2In: str) -> str:
        out = ""
        m = min(len(t1In), len(t2In))
        tIn = t1In if len(t1In) > len(t2In) else t2In
        M = len(tIn)

        for i in range(m):
            out += self.addS(t1In[i], t2In[i])

        if M > m:
            out += tIn[m:]  # Add remaining characters from the longer text

        return out

    def subTxt(self, t1In: str, t2In: str) -> str:
        out = ""
        m = min(len(t1In), len(t2In))
        tIn = t1In if len(t1In) > len(t2In) else t2In
        flag = 0 if len(t1In) > len(t2In) else 1
        M = len(tIn)

        for i in range(m):
            out += self.subS(t1In[i], t2In[i])

        if M > m:
            for i in range(m, M):
                t = tIn[i]
                if flag == 1:
                    out += self.subS("_", t)
                else:
                    out += self.subS(t, "_")

        return out

    def frwImproveBlock(self, blockIn: str, keyIn: str, jIn: int) -> str:
        t = keyIn

        while jIn > len(t) - 4:
            t += t

        key = t[t.index(t[jIn]):t.index(t[jIn]) + 4]
        k = self.text2array(key)
        b = self.text2array(blockIn)
        q = (k[0] + k[1] + k[2] + k[3]) % 4

        for i in range(3):
            j = (q + i + 1) % 4
            l = (q + i) % 4
            b[j] = (b[j] + b[l]) % 32

        return self.array2text(b)

    def invImproveBloc(self, blockIn: str, keyIn: str, jIn: int) -> str:
        t = keyIn

        while jIn > len(t) - 4:
            t += t

        key = t[t.index(t[jIn]):t.index(t[jIn]) + 4]
        k = self.text2array(key)
        b = self.text2array(blockIn)
        q = (k[0] + k[1] + k[2] + k[3]) % 4

        for i in range(2, -1, -1):
            j = (q + i + 1) % 4
            l = (q + i) % 4
            b[j] = (b[j] - b[l] + 32) % 32

        return self.array2text(b)
