def traverse(arr, n):
    for i in range(n):
        print('Arr[{0}] = {1}'.format(i, arr[i]))


def insert(arr, n, k, item):
    arr.append(0)
    for i in range(n, k, -1):
        arr[i] = arr[i-1]
    arr[k] = item
    n += 1

    return n


def delete(arr, n, k):
    for i in range(k, n):
        arr[i-1] = arr[i]
    arr.pop()
    n -= 1

    return n


def search(arr, n, item):
    for i in range(n):
        if arr[i] == item:
            return i
    return None


def update(arr, k, item):
    arr[k] = item


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 8]
    item = 10
    n = 5
    k = 3

    print('Original arr')
    traverse(arr, n)

    print('Insert')
    n = insert(arr, n, k, item)
    traverse(arr, n)

    print('Delete')
    n = delete(arr, n, k)
    traverse(arr, n)

    print('Search')
    print(search(arr, n, item))

    print('Update')
    update(arr, k, item)
    traverse(arr, n)
