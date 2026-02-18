import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"[^a-zA-Z](um)[^a-zA-Z]", s, re.IGNORECASE)
    return len(matches)


...


if __name__ == "__main__":
    main()