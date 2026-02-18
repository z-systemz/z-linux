import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    matches = re.search(r"\Wum\W", s)
    return matches


...


if __name__ == "__main__":
    main()