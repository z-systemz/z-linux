import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.match(r"^.+src=\"https?://(?:www\.)?(youtube\.com)/embed/(.+)\".+$", s)
    return f"{matches}"




if __name__ == "__main__":
    main()