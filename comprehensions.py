results = []
numbers = [1,2,3,4,5]

results = [number for number in numbers]
print results

results = []
results = [number*2 for number in numbers]
print results

results = []
results = [number for number in numbers if number % 2 == 0]
# for every number that meets a condition, do this
print results
# This is same as
results = []
for number in numbers:
    if number % 2 == 0:
        results.append(number)
print results

# adding on a string conversion
evens = []
evens = [str(number) for number in numbers if number % 2 == 0]
print evens

evens = []
evens = [number**2 for number in numbers if number % 2 == 0]
print "Evens to the power of 2: " + str(evens)

d = {k: v for k, v in zip(range(1,11), range(1,11))}
# creates a dictionary of key,values from two lists
# Good for creating a large test data set
# range(1,11) returns a list of number from 1 to 10
# zip(range(1,11), range(1,11)) returns creates a list of tuples of the first element in each list
for key, value in zip(range(1,11),range(1,11)):
    print key, value

def favorite_number(n):
    if n in (2,3,5,7,11,13,17):
        return str(n) + " is a favorite"

favorites = [favorite_number(i) for i in range(1,21) if i % 3 == 0]
print favorites
