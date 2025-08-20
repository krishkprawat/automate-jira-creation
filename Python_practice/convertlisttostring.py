#if we have list then convert into string

'''if list elements are stirng'''

list1= ["1","2","3"]
result = "".join(list1)
print(result)


'''OR if list elements are not stirng
The join() method only works with strings.
If your list has numbers, you must convert them to strings before joining.

What map() does

map(function, iterable) applies a function to each element of an iterable (list, tuple, etc.).

It returns a map object (like a generator) which can be directly used in loops or functions like join().'''

list2= [1,2,3]
result2 = "".join(map(str,list2))
print(result2)