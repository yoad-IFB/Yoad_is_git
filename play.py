

def multi():
    with open('RandomThing.txt') as file:
        content = file.readlines()
        return int(content[3]) * int(content[4])


def print_file():
    with open('RandomThing.txt') as file:
        print(file.read())


def main():
    print("hello world2")
    print_file()
    print("-----")
    # print(file.readline())
    print(multi())


if __name__ == '__main__':
    main()
