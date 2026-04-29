
class RegisterFile:
    def __init__(self):
        # Initializing all needed registers
        self.registers = {
            "t0": 0,
            "t1": 0,
            "t2": 0,
            "t3": 0,
            "t4": 0,
            "t5": 0,
            "t6": 0,
        }

    def read(self, reg_name: str) -> int:
        return self.registers.get(reg_name, 0)

    def write(self, reg_name: str, value: int, write_enable: bool):
        if write_enable and reg_name in self.registers:
            self.registers[reg_name] = value

    def dump(self) -> dict:
        return dict(self.registers)
