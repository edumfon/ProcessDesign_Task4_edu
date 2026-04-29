# datapath.py

from register_file import RegisterFile
from alu import ALU
from data_memory import DataMemory
from control_unit import ControlUnit
from instruction import Instruction

class Datapath:
    def __init__(self):
        self.reg_file = RegisterFile()
        self.alu = ALU()
        self.data_mem = DataMemory()
        self.control = ControlUnit()

        # For tracing
        self.trace = []

    def load_inputs(self, A: int, B: int, C: int, D: int):
        self.reg_file.write("t0", A, True)  # A
        self.reg_file.write("t1", B, True)  # B
        self.reg_file.write("t2", C, True)  # C
        self.reg_file.write("t3", D, True)  # D

        # Optionally precompute ~C into t5 if you want
        inv_c = 0 if C == 1 else 1
        self.reg_file.write("t5", inv_c, True)

    def execute_instruction(self, instr: Instruction):
        # Decode
        ctrl = self.control.decode(instr)

        # Read registers
        rs_val = self.reg_file.read(instr.rs)
        rt_val = self.reg_file.read(instr.rt)

        # ALU
        result = self.alu.execute(ctrl.alu_op, rs_val, rt_val, invert_a=ctrl.invert_a)

        # Write-back
        self.reg_file.write(instr.rd, result, ctrl.reg_write)

        # Trace
        self.trace.append({
            "instr": instr,
            "alu_op": ctrl.alu_op,
            "invert_a": ctrl.invert_a,
            "reg_write": ctrl.reg_write,
            "rs_val": rs_val,
            "rt_val": rt_val,
            "result": result,
            "regs_after": self.reg_file.dump(),
        })

    def get_output(self) -> int:
        # Final Y is in t0 per assignment
        return self.reg_file.read("t0")

    def get_trace(self):
        return self.trace
