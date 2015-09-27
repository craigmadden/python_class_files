import function_test
#from function_test import average, get_letter_grade
print "Imported average",function_test.average([1,2,3,4,5])

def average(x):
    return float(sum(x))/len(x)

print "Local average",average([1,2,3,4,5])