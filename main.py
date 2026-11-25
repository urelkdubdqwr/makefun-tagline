import os

TEXT = "Your agent writes the code. make.fun writes the checks.\n"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
