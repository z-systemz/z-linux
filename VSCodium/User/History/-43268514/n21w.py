import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    matches = re.findall(r"\W?(um)\W?", s)
    return len(matches)


...


if __name__ == "__main__":
    main()