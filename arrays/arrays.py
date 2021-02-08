# Arrays in Python
def array_print(ar):
    print("The current array is:", end = '')
    for i in ar:
        print(i, end = "")
    print("\n")

def array_test():
    # create an array
    ar = [3, 6, 6, 2, 9]

    array_print(ar)

    # add an element to the array
    ar.append(7)

    array_print(ar)

    # count num of a specific value in the array
    print(ar.count(6))

    print(ar.count(8))

    # return index of a specific value
    print(ar.index(6))

    # insert value at specified index
    ar.insert(0, 7)

    array_print(ar)

    # remove element at specified index
    ar.pop(3)

    array_print(ar)

    # remove the first element with specified value
    ar.remove(7)

    array_print(ar)

    # reverse the array
    ar.reverse()

    array_print(ar)

    # sort the array
    ar.sort()

    array_print(ar)


def main():
    array_test()

if __name__ == "__main__":
    main()

