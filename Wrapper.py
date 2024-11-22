from ASLFSR import ASLFSR
from SeedGenerator import SeedGenerator
from Converter import Converter

class Wrapper(ASLFSR):
    @staticmethod
    def wrap_CASLFSR_next(init_flag, state_in, seed_in, set_in):
        output = []
        stream = ""
        check = 0
        tmp = [0] * 20

        state = [[] for _ in range(4)]

        if init_flag == "up":
            for i in range(4):
                state[i] = SeedGenerator.seed2bins(SeedGenerator.make_seed(seed_in[i * 4:(i + 1) * 4]))
                check = 1
        elif init_flag == "down":
            state = state_in
            check = 1

        if check == 1:
            for j in range(4):
                for k in range(4):
                    result = ASLFSR.ASLFSR_next(state[k], set_in)
                    state[k] = result[1]
                    if k == 0:
                        tmp = [int(x) for x in result[0]]
                    else:
                        tmp = [(tmp[i] + int(result[0][i])) % 2 for i in range(20)]

                tmp_string = ''.join(str(x) for x in tmp)
                stream += Converter.bin2block(tmp_string)

            output = [stream, state]

        return output

    @staticmethod
    def wrap_CASLFSRM_next(init_flag, state_in, seed_in, set_in):
        output = []
        stream = ""
        check = 0
        tmp = [0] * 20

        state = [[] for _ in range(4)]

        if init_flag == "up":
            seed = SeedGenerator.check_seed(seed_in)
            for i in range(4):
                state[i] = SeedGenerator.seed2bins(SeedGenerator.make_seed(seed[i * 4:(i + 1) * 4]))
                if i > 0:
                    for q in range(i + 1):
                        state[i] = ASLFSR.ASLFSR_next(state[i], set_in)[1]
                check = 1
        elif init_flag == "down":
            state = state_in
            check = 1

        if check == 1:
            for j in range(4):
                for k in range(4):
                    result = ASLFSR.ASLFSR_next(state[k], set_in)
                    state[k] = result[1]
                    if k == 0:
                        tmp = [int(x) for x in result[0]]
                    else:
                        tmp = [(tmp[i] + int(result[0][i])) % 2 for i in range(20)]

                tmp_string = ''.join(str(x) for x in tmp)
                stream += Converter.bin2block(tmp_string)

            output = [stream, state]

        return output

