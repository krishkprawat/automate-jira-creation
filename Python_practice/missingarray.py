# find the missing number in the array
def findd(nums):
    
    n = len(nums) + 1   #total elements
    original_sum = sum(nums)
    expected_sum = n * (n+1) //2 #sum of 1 to n
    return expected_sum - original_sum

nums = [1,2,3,4,6]
print(findd(nums))


#antoher way

nums =[1,2,4,5]


for i in range(1, len(nums)+1):
    if i not in nums:
        print (i)