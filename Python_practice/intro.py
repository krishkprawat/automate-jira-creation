#Here are the some important points of the python before we start the coding..


#string methods --

name = "krishnapal singh rawat"
print(name)

print(name[0:6])   #including 0 but not 6
print(name[::-1])
print(len(name))   #include spaces

print(name[0:2])

print(name[:4])


string = "ishika"
print(string[::-2])
print(string[-3:-1]) #this will become [6-3 : 6-1] means 3:5 which is i and k


'''strings ae immutable means if we change anyhtng in string then we return a new string. old will be
 still same.'''

girl= "ishika"
print(girl.upper())

print(girl) #actual string will be same

'''replace() = replace will all the occurance with given string'''

print(girl.replace("ishika","KRISHna"))

'''split()= splits the given string and returns the seperated string as list item'''

boy = "krishnapal singh rawatboy"
print(boy.split())

'''capitalize = turns first character into uppercase and rest of them in small case. if rest are in upper then it turns in lower case
'''
boy1= "KrISHNapal"
print(boy1.capitalize())


'''count= count  the given word occurance
endswith()-- if string ends with a givenword then return true otherwise false


'''
