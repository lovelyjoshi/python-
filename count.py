def count_even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

nums = [1, 2, 3, 4, 5]
print(count_even_odd(nums))