

def multi(a, b):
    return a * b



def main():
    print("hello world2")
    with open('RandomThing.txt') as file:
        print(file.read())
        print("-----")
        # print(file.readline())
    print(multi(5, 6))


if __name__ == '__main__':
    main()
