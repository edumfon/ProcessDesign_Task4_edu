
from instruction import Instruction

class ControlSignals:
    def __init__(self, alu_op: str, invert_a: bool, reg_write: bool):
        self.alu_op = alu_op
        self.invert_a = invert_a
        self.reg_write = reg_write

class ControlUnit:
    def decode(self, instr):
        if instr.opcode == "AND":
            return ControlSignals("AND", False, True)

        elif instr.opcode == "ANDN":   # NEW
            return ControlSignals("AND", True, True)

        elif instr.opcode == "OR":
            return ControlSignals("OR", False, True)

        else:
            raise ValueError("Unsupported opcode")


    
        return ControlSignals(alu_op=alu_op, invert_a=invert_a, reg_write=reg_write)
