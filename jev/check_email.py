import sys


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("error: no email supplied", file=sys.stderr)
        print("usage: uv run check_email.py EMAIL", file=sys.stderr)
        return 1

    email = argv[1]
    print(f"ok: {email}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))