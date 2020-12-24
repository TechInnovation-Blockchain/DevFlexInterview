from math import floor


def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2
    array_length = len(array)

    if array_length == 0:
        return []

    zero_start_point = floor(array_length / 2) - 1
    new_array = []

    for value in array:
        if value != 0:
            new_array.append(value)

    zero_count = array_length - len(new_array)

    for index in range(zero_count):
        new_array.insert(zero_start_point + index, 0)

    return new_array

    pass


if __name__ == "__main__":
    # write your debug code here
    pass