
class DataMemory:
    def __init__(self):
        # Simple memory; keys - addresses, values - ints 
        self.memory = {}

    def load(self, address: int) -> int:
        return self.memory.get(address, 0)

    def store(self, address: int, value: int):
        self.memory[address] = value

    def dump(self) -> dict:
        return dict(self.memory)
