def generate_filled_list(List, nums, asc=True, with_ref=True, as_str=False):
    """
    generate linked list and optionally reference list
    :param nums: number of nodes to generate and their data
    :param asc: ascending order flag
    :param with_ref: generate reference list flag
    :param as_str: convert data to string flag
    :return: generated linked list with reference list optionally
    """
    if asc:
        if as_str:
            list_data = [str(n) for n in range(nums)]
        else:
            list_data = [n for n in range(nums)]
    else:
        if as_str:
            list_data = [str(n - 1) for n in range(nums, 0, -1)]
        else:
            list_data = [n - 1 for n in range(nums, 0, -1)]

    list1 = List(list_data)
    if with_ref:
        return list1, list_data
    return list1