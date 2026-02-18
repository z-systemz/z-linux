import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    matches = re.search(r"\W?(um)\W?", s)
    return matches.groups()


...


if __name__ == "__main__":
    main()