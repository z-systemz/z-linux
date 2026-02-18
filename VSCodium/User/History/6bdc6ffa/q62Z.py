import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check the ip format
    matchss = re.match(r'^(\d{1, 3})\.(\d{1, 3})\.(\d{1, 3})\.(\d{1, 3})$', ip)
    if matches:
        return true

...


if __name__ == "__main__":
    main()
