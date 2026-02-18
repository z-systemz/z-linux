import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matchs = re.match(r"^.+src\=\"(.+)\".+$")    
    print(matchs)




if __name__ == "__main__":
    main()