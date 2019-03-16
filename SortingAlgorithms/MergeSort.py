def merge(a):
    if len(a) == 1:
        return a
    middle = len(a) / 2
    left = merge(a[0:middle])
    right = merge(a[middle:])
    ileft = 0
    iright = 0
    ia = 0
    lleft = len(left)
    lright = len(right)

    while(ileft < lleft and iright < lright):
        if left[ileft] < right[iright]:
            a[ia] = left[ileft]
            ileft += 1
        else:
            a[ia] = right[iright]
            iright += 1

        ia += 1

    while iright != lright:
        a[ia] = right[iright]
        iright += 1
        ia += 1
    while ileft != lleft:
        a[ia] = left[ileft]
        ileft += 1
        ia += 1

    return a

#print merge([234,62,25, 674,1 ,3, 5, 67, 7, 21, 564, 76,4,8,43,85,34,85,32,86,32,57,43,47,97,123])
print merge([5, 4, 3, 2, 1, 6])
