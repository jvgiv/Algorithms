# fib


def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)

def fib1(n):
    nums = [0, 1]
    for i in range(2, n+1):
        val = nums[i - 1] + nums[i - 2]
        nums.append(val)

    return nums[n]