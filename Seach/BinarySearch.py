def binarySearch(a, n):
    beginning = 0
    end = len(a) - 1

    while beginning <= end:
        middle = (end + beginning) / 2
        if a[middle] == n:
            return middle
        elif a[middle] > n:
            end = middle - 1
        else:
            beginning = middle + 1

    return -1


print binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19], 11)

