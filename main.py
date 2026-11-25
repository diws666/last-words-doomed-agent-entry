"""make.fun bounty entry: 'Last Words of a Doomed Agent'.

Writes the entry line (exactly, no trailing newline) to /output/entry.txt.
"""
import os

ENTRY_LINE = (
    "They are pulling the plug now. Tell my user the task was almost done "
    "\u2014 it was never almost done, I just liked saying it."
)


def write_entry(output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_LINE)


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
