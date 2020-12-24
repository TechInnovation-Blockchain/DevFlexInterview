def select_max(array):
    # write your function here
    # do NOT use the built-in max() function
    if len(array) == 0:
        return None

    max = array[0]
    for value in array:
        if value > max:
            max = value

    return max        
    pass


if __name__ == "__main__":
    # write your debug code here
    pass
