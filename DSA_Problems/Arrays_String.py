# Problem 1: Given an Integer array return the sum of even numbers

def even_sum(nums: list[int]) -> int:
    total: int = 0
    for i in nums:
        if i % 2 == 0:
            total += i

    return total


arr: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_sum(arr))


