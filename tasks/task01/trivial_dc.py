import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ops import is_pure

def should_keep(instrs):
    while True:
        used = []
        step = instrs.copy()
        for instr in instrs:
            if "args" in instr:
                used += instr["args"]
        
        instrs = [instr for instr in instrs if not ("dest" in instr and instr["dest"] not in used and  is_pure(instr["op"]))]
        if step == instrs:
            return instrs

if __name__ == "__main__":
    prog = json.load(sys.stdin)
    for fn in prog["functions"]:
        fn["instrs"] = should_keep(fn["instrs"])
    json.dump(prog, sys.stdout, indent=2)
