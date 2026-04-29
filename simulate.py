
from instruction import Instruction
from datapath import Datapath

PROGRAM_ASM = [
    "and t4, t0, t1",   # t4 = A & B
    "andn t6, t2, t3",   # t6 = (~C) & D   
    "or  t0, t4, t6",   # t0 = t4 | t6
]

def build_program():
    program = []
    for line in PROGRAM_ASM:
        instr = Instruction.from_asm(line)
        if instr is not None:
            program.append(instr)
    return program

def run_simulation(A: int, B: int, C: int, D: int):
    dp = Datapath()
    dp.load_inputs(A, B, C, D)

    program = build_program()
    for instr in program:
        dp.execute_instruction(instr)

    Y = dp.get_output()
    trace = dp.get_trace()
    return Y, trace

if __name__ == "__main__":
    # Example test
    A, B, C, D = 1, 0, 1, 1
    Y, trace = run_simulation(A, B, C, D)

    print("Inputs: A B C D =", A, B, C, D)
    print("Final Y (t0)   =", Y)
    print("\nExecution trace:")
    for step, info in enumerate(trace, start=1):
        instr = info["instr"]
        print(f"Step {step}: {instr.opcode} {instr.rd}, {instr.rs}, {instr.rt}")
        print("  ALU op   :", info["alu_op"], "invert_a:", info["invert_a"])
        print("  rs, rt   :", info["rs_val"], info["rt_val"])
        print("  result   :", info["result"])
        print("  regs_after:", info["regs_after"])
        print()
