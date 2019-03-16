def quickSort(array, beginning, end):
    if end <= beginning:
        return

    pivot = end
    i = beginning
    while pivot > i:
        if array[i] > array[pivot]:
            array[i], array[pivot-1], array[pivot] = array[pivot-1], array[pivot], array[i]
            pivot -= 1
        else:
            i += 1

    quickSort(array, beginning, pivot-1)
    quickSort(array, pivot+1, end)

    return array


def quicksort(array, beginning, end):
    if beginning >= end:
        return

    pindex = beginning
    for i in xrange(beginning, end):
        if array[i] <= array[end]:
            array[i], array[pindex] = array[pindex], array[i]
            pindex += 1

    array[pindex], array[end] = array[end], array[pindex]
    quicksort(array, beginning, pindex-1)
    quicksort(array, pindex+1, end)

    return array


array = [234,62,25, 674,1 ,3, 5, 67, 7, 21, 564, 76,4,8,43,85,34,85,32,86,32,57,43,47,97,123]
#array = [4, 1, 6, 7, 9, 14, 3]
#array = [1, 2, 3, 4, 5]
#array = [5, 4, 3, 2, 1]
#print quickSort(array, 0, len(array)-1)
#print quicksort(array, 0, len(array)-1)
print quicksort(array, 0, len(array)-1)