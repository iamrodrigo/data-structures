#a = [234,62,25, 674,1 ,3, 5, 67, 7, 21, 564, 76,4,8,43,85,34,85,32,86,32,57,43,47,97,123]
#a=[5, 7, 2, 1, 6]
a = [1, 2, 7, 4, 5]
for i in xrange(len(a) - 1):
    swap = False
    for j in xrange(len(a) - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swap = True
    if not swap:
        break
    print a

print a
