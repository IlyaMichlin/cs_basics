"------------------Linear------------------"


def search_linear(array, val):
    """
    linear search
    :param array: array to search
    :param val: value to search
    :return: value index in array
    """
    for n, arr in enumerate(array):
        if val == arr:
            return n
    return None


"------------------Binary------------------"


def search_binary(array, val):
    """
    binary search
    :param array: array to search
    :param val: value to search
    :return: value index in array
    """
    low = 0
    high = len(array) - 1
    index = low + (high - low) // 2
    return divide_conquer(array, val, index, low, high)


def divide_conquer(array, val, index, low, high):
    """
    divide and conquer for binary search
    :param array: array to search
    :param val: value to search
    :param index: index to probe
    :param low: low index to probe
    :param high: high index to probe
    :return: value index in array
    """
    if array[index] == val:
        return index

    if low == high:
        return None

    if val < array[index]:
        high = index - 1
        index = low + (high - low) // 2
        index = divide_conquer(array, val, index, low, high)
    else:
        low = index + 1
        index = low + (high - low) // 2
        index = divide_conquer(array, val, index, low, high)
    return index


"------------------Interpolation------------------"


def interpolation_search(array, val):
    """
    interpolation search
    :param array: array to search
    :param val: value to search
    :return: value index in array
    """
    low = 0
    high = len(array) - 1
    index = round(low + ((high - low) / (array[high] - array[low])) * (val - array[low]))
    if index < low or index > high:
        return None

    while val != array[index]:
        if low == high or array[low] == array[high]:
            return None

        if index < low or index > high:
            return None
        elif array[index] == val:
            return index
        else:
            if array[index] < val:
                low = index + 1
            else:
                high = index - 1

        index = round(low + ((high - low) / (array[high] - array[low])) * (val - array[low]))

    return index
