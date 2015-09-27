num1 = raw_input("Give me a number: ")
num2 = raw_input("Give me another number: ")

num1 = int(num1)
num2 = int(num2)

print "%d plus %d = %d " % (num1, num2, (num1 + num2))
print "%d minus %d = %d " % (num1, num2, (num1 - num2))
print "%d times %d = %d " % (num1, num2, (num1 * num2))
print "%d divided by %d = %.2f " % (num1, num2, (float(num1) / float(num2)))

name = raw_input("Enter your name")
name = name.capitalize()
print name
print name[1:4]
# String functions
#str.lower()
#str.upper()
#str.strip() - This strips away any whitespace at the beginning or end of a string
