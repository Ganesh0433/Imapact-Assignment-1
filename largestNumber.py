def largestNumber(nums):
    nums = sorted(map(str, nums), key=lambda x: x*10, reverse=True)
    return str(int(''.join(nums)))
