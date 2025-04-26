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

#if list have a dulicate values then --

kplist= [1,1,12,2,234,45,45345,556,66,66]
newlist=sorted(set(kplist))
print(newlist[-2])


#set will give unique set result but it gives output in set so change this set to list i n last.
nomber= [1,76,67,67,2,3,4]
newdaru =list(set(nomber))
print(newdaru)
