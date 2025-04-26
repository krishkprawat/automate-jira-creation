#find a maximum number in the list

listi = [1,2,3,34,5,5456,44]
max=0
for num in listi:
    if num > max:
        max=num
print(max)


#second largerst number is the list

listi.sort()   #list is sorted in place returns none. so dont save it in variable.
largest= listi[-2]
print(largest)
