def input_names_into_list(prompot, dist):
    try:
        while True:
            item = input(prompot).strip()
            if item:
                dist.append(item.capitalize())
    except EOFError:
        print()
        return      


def main():
    names = []
    input_names_into_list("Name: ", names)
    if len(names) == 1:
        print("Adieu, adieu, to " + names[0])
    elif len(names) == 2:
        print("Adieu, adieu, to " + " and ".join(names))
    else:
        print("Adieu, adieu, to " + ", ".join(names[:-1]) + ", and " + names[-1])

if __name__ == "__main__":
    main()
