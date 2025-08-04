nums = [1,2,3,4,7,7,3,2]
freq_map ={}
n = len(nums)
for i in range (0,n):
    if nums[i] in freq_map:
        freq_map[nums[i]] +=1
    else:
        freq_map[nums[i]]=1

print (freq_map)
print(freq_map[7]) #if we want to see a frequecny of specific number 