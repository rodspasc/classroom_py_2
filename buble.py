def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if (l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]



l = [4,7,4,9,6,4,8,0,3,4,6]
print(l)
bubble_sort(l)
print(l)