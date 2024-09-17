import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from ops import is_pure

from examples.form_blocks import form_blocks

def should_keep(blocks):
    new_blocks = []
    for block in blocks:
        while True:
            last_used = {}
            step = block.copy()
            # print(step)
            for instr in block:
                # print(last_used)
                if "args" in instr:
                    for arg in instr["args"]:
                        if arg in last_used:
                            del last_used[arg]
                if "dest" in instr:
                    if instr["dest"] in last_used:
                        # print("Identified dead")
                        # print(block)
                        block.remove(last_used[instr["dest"]])
                        # print(block)
                    last_used[instr["dest"]] = instr    
            # print(block)
            if step == block:
                new_blocks += block
                break
    return new_blocks

if __name__ == "__main__":
    prog = json.load(sys.stdin)
    for fn in prog["functions"]:
        fn["instrs"] = sum([], should_keep(form_blocks(fn["instrs"])))
    json.dump(prog, sys.stdout, indent=2)
