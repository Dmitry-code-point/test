from random import randint

n = 10
numbers = [randint(1, 100) \
           for i in range(n)]

def insert_sort(numbers):
    for i in range(1, len(numbers)):
        num = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > num:
            numbers[j + 1] = numbers[j]
            j -= 1
            numbers[j + 1]= num
    return numbers
print(insert_sort(numbers))