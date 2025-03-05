from random import randint

n = 10
numbers = [randint(0,100) \
           for i in range(n)]

def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers[:]
    else:
        median = int(len(numbers) / 2)
        left = merge_sort(numbers[:median])
        right = merge_sort(numbers[median:])
        return merge(left, right)

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res
print(merge_sort(numbers))

