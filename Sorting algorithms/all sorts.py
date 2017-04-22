from random import *

def insertion_sort(A):
    for i in range(1, len(A)):
        while i > 0 and A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1                



def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]

def selection_sort(x):
    for i in range(len(x)):
        min_ind = i
        for j in range(i, len(x)):
            if x[min_ind] > x[j]:
                min_ind = j
        x[i], x[min_ind] = x[min_ind], x[i]

def bubble_sort(a):
     for i in range (len(A)):
        for j in range (len(A)-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]

def cocktail_sort(A):
    up = range(len(A)-1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                print(A)
                if A[i] > A[i+1]:  
                    A[i], A[i+1] =  A[i+1], A[i]
                    swapped = True
            if not swapped:
                return


def shacker(array):
    length = len(array)
    left = 0
    right = length - 1
    while left <= right:
        for i in range(left, right):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        right -= 1
        
        for i in range(right, left, -1):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
        left += 1

def shell(x):
    gap_prev = 1
    gap = 1
    sorte = True
    while True:
        if gap == len(x):
            break
        elif gap > len(x):
            gap = gap_prev
            break
        gap_prev = gap
        gap = gap_prev*3+1

    while gap >= 1:
        i = gap
        while i <= len(x)-1:
            if x[i] < x[i-gap]:
                x[i], x[i-gap] = x[i-gap], x[i]
                sorte = True
            i = i+1
        if sorte == False:
            gap = (gap - 1) // 3
        sorte = False

def qSort(x):
    if len(x) <= 1:
        return(x)
    else:   
        q = x[len(x) // 2]
        l = []
        m = []
        r = []
        for i in range(len(x)):
            if x[i] < q:
                l.append(x[i])
            elif x[i] == q:
                m.append(x[i])
            else:
                r.append(x[i])

        return(qSort(l) + m + qSort(r))

def quickSort(a):
    if len(a) <= 1:
        return a
    else:
        less = []
        more = []
        pivot = choice(a)
        for i in a:
            if i < pivot:
                less.append(i)
            if i > pivot:
                more.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + [pivot] * a.count(pivot) + more

def insort_bar(x):
    for i in range(2, len(x)):
        print(x)
        if x[i-1] > x[i]:
            x[0] = x[i]
            j = i - 1
            while x[j] > x[0]:
                x[j + 1] = x[j]
                j -= 1
            x[j+1] = x[0]
    
l = [x for x in range(5, 0, -1)]

insertion_sort(l)
##insertion_sort_bin(l)
##selection_sort(l)
# bubble_sort(l)
#cocktail_sort(l)
##shell(l)
#qSort(l)
#quickSort(l) # да хранит Селестия того,
# кому попадется этот любимец хаоса и беспорядка
insort_bar(l)
print(l)
