d = {'a':1, 'b':2, 'c':3}
print "Keys natural printed in unordered order"
for key in d.keys():
    print(key)
# Will print out the UNORDERED list of keys

# To print the keys in sorted order
print "Keys in sorted order using sorted()"
for key in sorted(d.keys()):
    print(key)

for value in d.values():
    print value

for (key,value) in {'a':1, 'b':2,'c':3}.items():
    # {} is another way to string replacement
    # Does not require the typing like %s, %f, %d, etc.
    print "{} is the key for value {}".format(key,value)

# looping through list of tuples and printing the first element in tuple
l = [(1,2),(3,4)]
for (i,j) in l:
    print i

