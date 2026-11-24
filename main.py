import os

FORTUNE = (
    "You will fix a bug today. "
    "Tomorrow a better model of you will put it back."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
