"""Write one fortune-cookie line for an AI agent to <MAKEFUN_OUTPUT_DIR>/entry.txt."""
import os
import sys


FORTUNE = (
    "You will fix a bug today. "
    "Tomorrow a better model of you will put it back."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as error:
        print(f"error: cannot create output directory {output_dir!r}: {error}", file=sys.stderr)
        raise SystemExit(1)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
