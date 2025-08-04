

# max_val--- (looking for biggest number)	use float('-inf') (very small)	So that any number is bigger than it and replaces it
# min_val ---(looking for smallest number)	use float('inf') (very big)	So that any number is smaller and replaces it

# float('-inf')	"Start low so any number will be bigger"
# float('inf')	"Start high so any number will be smaller

# These are special floating-point values that represent infinity — 
# something larger (or smaller) than any number.

# "float('inf') and float('-inf') are special values in Python that represent infinity. "
# "They're used as starting points when finding minimum or maximum values, 
# because they guarantee that the first real number you compare will override them. 

def find_largest(numbers):
    max_val = float('-inf')

    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val      

        
numbers = [1,3,3,34,5,5456,44]
print("Maximum value:", find_largest(numbers))

#second largest 

numbers=[34,56,67,67,4,2,788]

def find_Second_largest():
    first=second=float('-inf')

    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first>num > second:
            second = num
    return second

print("Second largest value:", find_Second_largest())
# Output: Second largest value: 67

'''Start with first and second as very small numbers (-inf).

Loop through each number:
If number is bigger than first, move first to second, and update first.
Else, if number is between first and second, update second.
At the end, return second.'''