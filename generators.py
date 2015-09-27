def fibonnacci():
    a,b = 0,1
    while True:
        # yield is a key word that makes this a generator
        # When this function is called again with .next, it will start at the yield
        # and not reset the a,b values
        yield b
        a,b = b, a + b

# Generators keep track of where it left off. This can be a big performance boost.

fib = fibonnacci()

print fib.next()
print fib.next()
print fib.next()

fibs = []
for i in range(1,11):
    fibs.append(fib.next())

print fibs

# Same thing as above but in a comprehension form
[fib.next() for i in range(1,11)]
print fibs

# This is a list comprehension and generator combined
# Note the parens instead of brackets of a list comprehension
powers = (i**2 for i in range(100) if i % 2 == 0)

