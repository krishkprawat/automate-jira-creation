'''input = "ishika rawat
outut = tawar akihsi'''

girl= "ishika rawat"
newgirl=list(girl)
newgirl.reverse()
print("".join(newgirl))

#method 2--

'''input = "krish rawat
output = hsirk tawar '''

boy = "krish rawat"
reversed_word=[]
nboy= boy.split()
for word in nboy:
    reversed = word[::-1]
    reversed_word.append(reversed)


print(reversed_word)
result = " ".join(reversed_word) #"".join() in Python is used to combine a list of strings into a single string.
print(result)

