#merge two arays without duplicates..

list1=[3,4,5,6,7]
list2=[2,3,4,5,6,7,8]

def merge(list1,list2):
    merged= list1+list2
    result =[]

    for i in merged:
        if i not in result:
            result.append(i)
    return result

print(merge(list1,list2))
            