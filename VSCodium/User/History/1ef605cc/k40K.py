import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matchs = re.match(r"^.+src=\"https?://(?:www\.)?(.+)\".+$", s)
    print(matchs.group(1))




if __name__ == "__main__":
    main()