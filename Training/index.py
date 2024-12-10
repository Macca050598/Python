import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug message.")
logging.error("This is an error message.")


def binary_search(lst, item):
    low = 0;
    high = len(lst) -1;

    while low <= high:
        mid = (low + high) //2
        guess = lst[mid]

        if guess == item:
            return mid;
        if guess < item:
            high = mid + 1;
        else:
            low = mid - 1;
    return -1;

my_list = [1,2,4,67,887]

print(binary_search(my_list, 4))