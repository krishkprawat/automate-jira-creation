#return a index of comiaitons in the list where sum of two numbers is target number.

'''1,2,3,4,5 , target is - 5
then return 2,1 --- 0,3'''

def check(nums):
    n = len(nums)
    target = 5
    result = {}
    pairs = []  # ← To store all valid pairs of indices

    for i in range(n):
        remaining = target - nums[i]
        if remaining in result:
            pairs.append([result[remaining], i])  # ← Store the index pair
        result[nums[i]] = i  # ← Add current element to result map

    return pairs  # ← Return the list of pairs

# Example
list1 = [1, 2, 3, 4, 5]
print(check(list1))
