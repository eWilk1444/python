"""
    Logical Operators
"""

a = 10
b = 20
c = 30
# and operator
if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c:
    print("b is the largest number")
else:
    print("c is the largest number")
# or operator
if a > b or a > c:
    print("a is the largest number")
elif b > a or b > c:
    print("b is the largest number")
else:
    print("c is the largest number")
# not operator
if not a > b:
    print("a is not greater than b")
else:
    print("a is greater than b")
