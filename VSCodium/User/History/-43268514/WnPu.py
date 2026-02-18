import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    matches = re.search("\Wum\W", s)
    return len(matches)


...


if __name__ == "__main__":
    main()