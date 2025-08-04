# #remove dupicate from array

# def dup(arr):
#     seen = set()
#     result = []

#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
#     return result


# arr = [5,8,8,1,2,3,3,4,5]
# print(dup(arr))


'''========================'''


#print only duplicate values from an array

def d(arr):
    seen =set()
    duplicates = set()    #use set here so that same number will not append multiple times.

    for num in arr :
        if num in seen : 
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates
arr=[4,5,2,3,4,5,5,5,5,6,1,2]
print(d(arr))