constant = ["const"]
arithmetic = ["add", "mul", "sub", "div"]
comparison = ["eq", "lt", "gt", "le", "ge"]
logic = ["not", "and", "or"]
control = ["jmp", "br", "call", "ret"]
misc = ["id", "print", "nop"]

def is_arith(op):
    return op in arithmetic
def is_comp(op):
    return op in comparison
def is_logic(op):
    return op in logic
def is_control(op):
    return op in control
def is_pure(op):
    return op in constant or is_arith(op) or is_comp(op) or is_logic(op)