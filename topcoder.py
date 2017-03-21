from llist import dllist

def people_circle(male, female, k):
    circle = dllist()

    for i in range(male):
        circle.appendright('M')

    size = male + female
    index = k % size
    print(index)
    for i in range(female):
        index = (index + k) % size
        print(index)
        size -= 1

    print(size)


def main():
    people_circle(5, 3, 2)


if __name__ == '__main__':
    main()
