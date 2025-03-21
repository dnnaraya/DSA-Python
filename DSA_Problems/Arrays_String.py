# Problem 1: Given an Integer array return the sum of even numbers
def even_sum(nums: list[int]) -> int:
    total: int = 0
    for i in nums:
        if i % 2 == 0:
            total += i

    return total


# Problem 2: Given a string, return if the str is Valid IP address

def is_valid_ip(str_ip: str) -> bool:
    arr_str = str_ip.split('.')
    if len(arr_str) != 4:
        return False

    for i in range(0, 4):
        try:
            cur_str = int(arr_str[i])
            if (cur_str < 0) or (cur_str > 255):
                return False
        except ValueError:
            return False

    return True

def validate_ip_address(self, queryIP: str) -> str:
    result = ['IPv4', 'IPv6', 'Neither']

    if '.' in queryIP and len(queryIP.split('.')) == 4:

        arr_IP = queryIP.split('.')
        for i in arr_IP:
            try:
                cur = int(i)
                if cur != 0 and len(i) - len(i.lstrip('0')) != 0:
                    return 'Neither'
                elif (cur < 0) or (cur > 255):
                    return 'Neither'

            except ValueError:
                return 'Neither'

        return 'IPv4'

    elif ':' in queryIP and len(queryIP.split(':')) == 8:

        arr_IP6 = queryIP.split(":")
        valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B',
                       'C', 'D', 'E', 'F']
        for i in arr_IP6:
            if len(i) >= 1 and len(i) <= 4:
                for x in i:
                    if x not in valid_chars:
                        return 'Neither'
            else:
                return 'Neither'

        return 'IPv6'

    else:
        return 'Neither'

# problem 3: Reverse Words in a String - Solution 1
def reverseWords1(self, s: str) -> str:
    s_arr = s.strip().split(" ")
    reverse_word = ""
    s_arr_len = len(s_arr)
    for i in range(0, s_arr_len):
        word = s_arr[s_arr_len - 1 - i]
        if word != "":
            reverse_word += s_arr[s_arr_len - 1 - i].strip()
            if i != s_arr_len - 1:
                reverse_word += " "
    return reverse_word

# Solution 2
def reverseWords2(self, s: str) -> str:
    words = s.split()

    left = 0
    right = len(words)-1

    while left < right :
        words[left], words[right] = words[right], words[left]
        right -= 1
        left += 1

    return " ".join(words)


# Problem 4 : Determine if string has all unique characters
def has_unique_chars(s: str) -> bool:

    for i in s:
        if s.count(i) > 1:
            return False

    return True


# Problem 5: Is Subsequence

def isSubsequence(s: str, t: str) -> bool:
    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    return i == len(s)



arr: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_sum(arr))

queryIP1 = "172.16.254.1"
queryIP2 = "172.16.@4.256"
print("Is this IP ", queryIP1, "valid? : ", is_valid_ip(queryIP1))
print("Is this IP ", queryIP2, "valid? : ", is_valid_ip(queryIP2))

str1 = "abcdefgh"
str2 = "aabbjhjgfg"
print("Is the string ", str1, "has unique characters? :", has_unique_chars(str1))
print("Is the string ", str2, "has unique characters? :", has_unique_chars(str2))

s1 = "abc"
s2 = "axc"
t = "ahbgdc"
print("Is the string s ", s1 , "is subsequence of string t ", t , " :: ", isSubsequence(s1,t))
print("Is the string s ", s2 , "is subsequence of string t ", t , " :: ", isSubsequence(s2,t))