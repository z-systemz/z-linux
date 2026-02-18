import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.match(r"^(\d\d?)(:\d\d)? (AM|PM) to (\d\d?)(:\d\d)? (AM|PM)$", s)
    if matches:
        hour = cconvert_hour(matches.group(1), matches.group(3))
        hour += convert_hour(matches.group(4), matches.group(6))
        m1, m2 = int(matches.group(2).removeprefix(":")), int(matches.group(5).removeprefix(":"))
        if m1 >= 60 or m2 >= 60:
            raise ValueError
        else:
            minute = m1 + m2
            if minute >= 60:
                hour +=1
        hour %= 24
        minute %= 60
        return f"{}"

def convert_hour(hour, time)
    hour = int(hour)
    if hour > 12:
        raise ValueError
    if time == 'AM':
        return hour
    else:
        return hour + 12
...


if __name__ == "__main__":
    main()