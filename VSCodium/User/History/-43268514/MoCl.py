import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = f" {s} "
    matches = re.findall(r"[^A-Z](um)[^A-Z]", s, re.IGNORECASE)
    return len(matches)


...


if __name__ == "__main__":
    main()