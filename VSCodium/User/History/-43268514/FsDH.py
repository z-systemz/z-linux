import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = f" {s} "
    print(s)
    matches = re.findall(r"\b(um)\b", s, re.I)
    print(matches)
    return len(matches)


...


if __name__ == "__main__":
    main()