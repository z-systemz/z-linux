import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.match(r"^(\d\d?)(:\d\d)? (AM|PM) to (\d\d?)(:\d\d)? (AM|PM)$", s)
    try:
        if matches:
            start = {
                "hour": convert_hour(matches.group(1), matches.group(3)),
                "min": convert_minute(matches.group(2))
            }
    
            end = {
                "hour": convert_hour(matches.group(4), matches.group(6)),
                "min": convert_minute(matches.group(5))
            }
            return f"{start['hour']}{start['min']} to {end['hour']}{end['min']}"
    except ValueError:
        raise ValueError
def convert_hour(hour, time):
    hour = int(hour)
    if hour > 12:
        raise valueerror
    if time == 'AM':
        if hour == 12:
            return "00"
        return f"{hour:0>2}"
    else:
        if hour == 12:
            return "12"
        return f"{(hour + 12):0>2}"

def convert_minute(min):
    if min:
        min = min.removeprefix(":")
        if int(min) < 60:
            return f":{min}" 
        else:
            raise ValueError
    else:
        return f":00"


if __name__ == "__main__":
    main()