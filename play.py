

def multi():
    with open('RandomThing.txt') as file:
        content = file.readlines()
        return int(content[3]) * int(content[4])


def print_file():
    with open('/Users/yoadhordan/PycharmProjects/Yoad_is_git/tryenv/cool.txt') as file:
        print(file.read())


def more_file():
    with open('/Users/yoadhordan/PycharmProjects/Yoad_is_git/tryenv/cool.txt') as file:
        lines = file.readlines()
        print(int(lines[0]) - int(lines[1]) + int(lines[2]))


def main():
    print("hello world2")
    print_file()
    print("-----")
    # print(file.readline())
    print(multi())
    more_file()


if __name__ == '__main__':
    main()
