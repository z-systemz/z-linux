import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check the ip format
    re.search(r'^(\D\.)$', ip)


...


if __name__ == "__main__":
    main()
