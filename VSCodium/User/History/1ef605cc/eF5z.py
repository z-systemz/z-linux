import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matchs = re.match(r"^.+src=\"https?://(?:www\.)?(youtube\.com)/embed/(.+)\".+$", s)
    return f"{matchs.groups(1)} {matchs.groups(2)}"




if __name__ == "__main__":
    main()