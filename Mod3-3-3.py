from functools import cmp_to_key
def large_number(nums):
    nums = list(map(str, nums))
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    nums.sort(cmp_to_key(compare))
    result = ''.join(nums)
    return result
nums = [56, 9, 11, 2]
print(large_number(nums))