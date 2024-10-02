from SBlock import SBlock

class SBlockImpl(SBlock):
    def __init__(self, utils, cesar):
        self.utils = utils
        self.cesar = cesar

    def frw_S(self, blockIn: str, keyIn: str, jIn: int) -> str:
        out = "input error"
        if len(blockIn) != 4:
            return out
        out = self.cesar.frw_poly_Cesar(blockIn, keyIn, jIn)
        return self.utils.frwImproveBlock(out, keyIn, jIn)

    def inv_S(self, blockIn: str, keyIn: str, jIn: int) -> str:
        out = "input error"
        if len(blockIn) != 4:
            return out
        impBlock = self.utils.invImproveBloc(blockIn, keyIn, jIn)
        out = self.cesar.inv_poly_Cesar(impBlock, keyIn, jIn)
        return out
