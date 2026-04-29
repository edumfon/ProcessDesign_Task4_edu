
from dataclasses import dataclass

@dataclass
class Instruction:
    opcode: str      # e.g., "AND", "OR"
    rd: str          # destination register name, e.g., "t4"
    rs: str          # source register 1
    rt: str          # source register 2

    @staticmethod
    def from_asm(line: str) -> "Instruction":
        # Example: "and t4, t0, t1"
        line = line.split(";")[0].strip().lower()
        if not line:
            return None
        parts = line.replace(",", " ").split()
        opcode = parts[0].upper()
        rd, rs, rt = parts[1], parts[2], parts[3]
        return Instruction(opcode=opcode, rd=rd, rs=rs, rt=rt)
