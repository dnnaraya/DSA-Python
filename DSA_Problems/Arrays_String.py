# Problem 1: Given an Integer array return the sum of even numbers
def even_sum(nums: list[int]) -> int:
    total: int = 0
    for i in nums:
        if i % 2 == 0:
            total += i

    return total

#Problem 2: Given a string, return if the str is Valid IP address
def is_valid_ip(strIp: str) -> bool:
    arr_str = strIp.split(':')
    print(arr_str)

    if len(arr_str) != 4:
        return False

    for i in range(0,4):
        try:
            cur_str = int(arr_str[i])
            if (cur_str < 0) or (cur_str > 255):
                return False
        except ValueError:
            return False

    return True



arr: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_sum(arr))


