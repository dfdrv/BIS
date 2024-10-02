class Cesar:
    def __init__(self, util):
        self.util = util

    # to cesar
    def frw_Cesar(self, txtIn: str, keyIn: str) -> str:
        if len(keyIn) > 1:
            raise ValueError("Key length longer than 1")

        out = ""
        key = keyIn[0]

        for i in range(len(txtIn)):
            tmp = txtIn[i]
            out += self.util.addS(tmp, key)

        return out

    # from cesar
    def inv_Cesar(self, txtIn: str, keyIn: str) -> str:
        if len(keyIn) > 1:
            raise ValueError("Key length longer than 1")

        out = ""
        key = keyIn[0]

        for i in range(len(txtIn)):
            tmp = txtIn[i]
            out += self.util.subS(tmp, key)

        return out

    # Poly-alphabet
    def frw_poly_Cesar(self, txtIn: str, keyIn: str, jIn: int) -> str:
        out = ""
        tK = "_"
        k = len(keyIn)

        for i in range(len(txtIn)):
            tI = txtIn[i]
            q = (i + jIn) % k
            tK = self.util.addS(tK, keyIn[q])
            out += self.util.addS(tI, tK)

        return out

    def inv_poly_Cesar(self, txtIn: str, keyIn: str, jIn: int) -> str:
        out = ""
        tK = "_"
        k = len(keyIn)

        for i in range(len(txtIn)):
            tI = txtIn[i]
            q = (i + jIn) % k
            tK = self.util.addS(tK, keyIn[q])
            out += self.util.subS(tI, tK)

        return out
