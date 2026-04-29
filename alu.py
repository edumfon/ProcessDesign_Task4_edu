
class ALU:
    def execute(self, op: str, a: int, b: int, invert_a: bool = False) -> int:
        # Inputs are assumed to be 0 or 1 for this Boolean processor
        if invert_a:
            a = 0 if a == 1 else 1

        if op == "AND":
            return a & b
        elif op == "OR":
            return a | b
        else:
            raise ValueError(f"Unsupported ALU operation: {op}")
