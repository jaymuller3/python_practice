# Python Practice 1: 
#   Variables & Basic Data Types, Boolean Exp, Conditionals, Math Ops


# Variables & Basic Data Types
# Integers
x = 2
y = 3
z = x + y
print("Ex 1: " + str(x) + " + " + str(y) + " = " + str(z))

# Floats
u = 3.3
v = 4.5
w = u + v
print("Ex 2: " + str(u) + " + " + str(v) + " = " + str(w))

# Composite
t = x + u
print("Ex 3: " + str(x) + " + " + str(u) + " = " + str(t))


# Boolean Expressions
# u = 3.3, t = 5.3, Expected: valCheck = False
valCheck = u == t
print("Ex 4: ", valCheck)

# u = 3.3, t = 5.3, x = 2, Expected: valCheck = True
valCheck = u == (t - x)
print("Ex 5: ", valCheck)


#Conditionals
# Not Equal - !=
# u = 3.3, t = 5.3, Expected: valCheck = True
valCheck = u != t
print("Ex 6: ", valCheck)

# and
# If either statement is false, the entire statement is false
# u != t, Expected: True; u == t - x, Expected: True; Expected: True
valCheck = u != t and u == t - x
print("Ex 7: ", valCheck)

# u == t, Expected: False; u == t - x, Expected: True; Expected: False
valCheck = u == t and u == t - x
print("Ex 8: ", valCheck)

# or
# If either statement is true, the entire statement is true
# u == t, Expected: False; u == t - x, Expected: True; Expected: True
val1 = u == t
val2 = u == t - x
valCheck = val1 or val2
print("Ex 9: ", valCheck)

# If both statements are false, the entire statement is false
# u == t, Expected: False; u == v, Expected: False; Expected: False
val1 = u == t
val2 = u == v
valCheck = val1 or val2
print("Ex 10: ", valCheck)


#Mathematical Operations
# Multiplication
r = x * y
print("Ex 11: " + str(x) + " * " + str(y) + " = " + str(r))

# Division
s = x / y
print("Ex 12: " + str(x) + " / " + str(y) + " = " + str(s))

# Integer Division - returns the floor value of a division equation
s = x // y
print("Ex 13: " + str(x) + " // " + str(y) + " = " + str(s))

s = v // y
print("Ex 14: " + str(v) + " // " + str(y) + " = " + str(s))

# Modulo Division - calculates the remainder of a division equation
s = x % y
print("Ex 15: " + str(x) + " % " + str(y) + " = " + str(s))

s = r % y
print("Ex 16: " + str(z) + " % " + str(y) + " = " + str(s))

s = (r + 1) % y
print("Ex 17: " + "(" + str(z) + " + 1)" + " % " + str(y) + " = " + str(s))

# Exponents
s = x ** y
print("Ex 18: " + str(x) + " ^ " + str(y) + " = " + str(s))

# P1: Calculate 5% sales tax on item costing $9.99

# P2: Find maximum value that a 32-bit number can have

# P3: Find the remainder of 23 divided by 7