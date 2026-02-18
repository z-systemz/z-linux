import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matchs = re.match(r"^.+src=\"(https?://)(?:www\.)?(youtube\.com)/embed(/[^\"]+)\".+$", s)
    if matchs:
        return f"{matchs.group(1)}{matchs.group(2)}{matchs.group(3)}"




if __name__ == "__main__":
    main()