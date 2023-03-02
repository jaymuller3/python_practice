# Python Practice 1: 
#   Variables & Basic Data Types, Boolean Exp, Conditionals, Math Ops


# Variables & Basic Data Types
# Integers
x = 2
y = 3
z = x + y
print(str(x) + " + " + str(y) + " = " + str(z))

# Floats
u = 3.3
v = 4.5
w = u + v
print(str(u) + " + " + str(v) + " = " + str(w))

# Composite
t = x + u
print(str(x) + " + " + str(u) + " = " + str(t))


# Boolean Expressions
# u = 3.3, t = 5.3, Expected: valCheck = False
valCheck = u == t
print(valCheck)

# u = 3.3, t = 5.3, x = 2, Expected: valCheck = True
valCheck = u == (t - x)
print(valCheck)


#Conditionals
# Not Equal - !=
# u = 3.3, t = 5.3, Expected: valCheck = True
valCheck = u != t
print(valCheck)

# and
# If either statement is false, the entire statement is false
# u != t, Expected: True; u == t - x, Expected: True; Expected: True
valCheck = u != t and u == t - x
print(valCheck)

# u == t, Expected: False; u == t - x, Expected: True; Expected: False
valCheck = u == t and u == t - x
print(valCheck)

# or
# If either statement is true, the entire statement is true
# u == t, Expected: False; u == t - x, Expected: True; Expected: True
val1 = u == t
val2 = u == t - x
valCheck = val1 or val2
print(valCheck)

# If both statements are false, the entire statement is false
# u == t, Expected: False; u == v, Expected: False; Expected: False
val1 = u == t
val2 = u == v
valCheck = val1 or val2
print(valCheck)


#Mathematical Operations
# Multiplication
r = x * y
print(str(x) + " * " + str(y) + " = " + str(r))

# Division
s = x / y
print(str(x) + " / " + str(y) + " = " + str(s))

# Integer Division
s = x // y
print(str(x) + " // " + str(y) + " = " + str(s))

s = v // y
print(str(v) + " // " + str(y) + " = " + str(s))

# Modulo Division
s = x % y
print(str(x) + " % " + str(y) + " = " + str(s))

s = r % y
print(str(z) + " % " + str(y) + " = " + str(s))

s = (r + 1) % y
print("(" + str(z) + " + 1)" + " % " + str(y) + " = " + str(s))

# Exponents
s = x ** y
print(str(x) + " ^ " + str(y) + " = " + str(s))