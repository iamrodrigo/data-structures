a = [234,62,25, 674,1 ,3, 5, 67, 7, 21, 564, 76,4,8,43,85,34,85,32,86,32,57,43,47,97,123]
#a=[12, 11, 13, 5, 6]
#a = [4, 6, 1, 2, 3,  7, 8, 5]
#a = [3,2,1,3,2,1,3,2,1]

print a

for i in xrange(1, len(a)):
    j = i - 1
    swap = a[i]
    if a[i] < a[j]:
        beginning = 0
        end = i - 1
        middle = (beginning + end) / 2
        while beginning <= end:
            if a[middle] <= a[i] and a[middle+1] >= a[i]:
                break
            else:
                if  a[middle] > a[i]:
                    end = middle - 1
                else:
                    beginning = middle + 1
            middle = (beginning + end) / 2
        while j > middle:
            a[j+1] = a[j]
            j -= 1
        a[middle+1] = swap

    print a
