from random import randint

n = 10
numbers = [randint(0,100) \
           for i in range(n)]

def half_division(numbers):
    if len(numbers) < 2:
        return numbers[:]
    else:
        median = int(len(numbers) / 2)
        left = half_division(numbers[:median])
        right = half_division(numbers[median:])
        return comparison(left, right)

def comparison(left, right):
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
print(half_division(numbers))

