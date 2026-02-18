import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check the ip format
    matches = re.match(r'^(\d\d?\d?)\.(\d\d?\d?)\.(\d\d?\d?)\.(\d\d?\d?)$', ip)
    if matches:
        for match in matches.groups():
            if int(match) > 255 or match:
                return False
        return True
    else:
        return False

...


if __name__ == "__main__":
    main()
