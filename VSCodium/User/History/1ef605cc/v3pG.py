import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matchs = re.match(r"^.+src=\"https?://(?:www\.)?(youtube\.com|youtu\.be)/embed(/[^\"]+)\".+$", s)
    if matchs:
        return f"https://youtu.be{matchs.group(2)}"




if __name__ == "__main__":
    main()