given = ['Dog','xerox','Python','x','depend']
count = 0
for string in given:
    if len(string) > 1:
        if string[:1] == string[-1:]:
            count += 1

#print count

lst = ['mix','xyz','apple','Xanadu','aardvark']
#output a sorted list with items beginning with x go first
x_list = []
for item in lst:
    if item.startswith('x'):
    # Could also pass a tuple of values to startswith
    # if item.startswith(('x','X')):
        x_list.append(item)
        lst.remove(item)

x_list.sort()
lst.sort()
x_list.extend(lst)
print x_list

# Sort a list of tuples by the last element in the tuple
tuples = [(1,7),(1,3),(3,4,5),(2,2)]

# Utility function/Helper function
# Create funtion that returns the last element of a tuple
def last(t):
    return t[-1]

# Sort the tuples by using a utility function to return the last element to the sort
# Do not put the parens or value when used as the key function
print sorted(tuples, key=last)

