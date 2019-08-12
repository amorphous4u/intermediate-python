__authos__ = 'Amit Verma'

def my_big_sum(n):
    # num, nums = 0, []
    #
    # while num < n:
    #     nums.append(num)
    #     num += 1
    # return nums
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(my_big_sum(10000000)))