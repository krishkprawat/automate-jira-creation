#pritn vowels count in the string

name = "krishnpalt"
count = 0
vowels=["a","e","i","o","u"]
for i in name:
    if i in vowels:
        count = count +1
print(count)