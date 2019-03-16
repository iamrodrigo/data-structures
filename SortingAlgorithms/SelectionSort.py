#a = [234,62,25, 674,1 ,3, 5, 67, 7, 21, 564, 76,4,8,43,85,34,85,32,86,32,57,43,47,97,123]
a  = [64, 25, 12, 22, 11]
print a
for i in xrange(len(a) - 1):
    min = i
    for j in xrange(i + 1, len(a)):
        if a[j] < a[min]:
            min = j
    if min > i:
        a[i], a[min] = a[min], a[i]
    print a
