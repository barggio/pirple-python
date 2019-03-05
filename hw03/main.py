"""
Python class HW # 3
Create function that test equality between three integers/string-integer
If at least two inputs are equal, return True else False
"""

"""
Compare three numbers are integer or string equivalent of integer.
"None" is considered comparable and used for comparison.
e.g.  None, 2, None => True
Parameters
Number1: first number to be compared
Number2: second number to be compared
Number3: third number to be compared
"""
def compareEquality(Number1, Number2, Number3):
    # After conversion, the result is either integer or None
    value1 = int(Number1) if Number1 is not None else None
    value2 = int(Number2) if Number2 is not None else None
    value3 = int(Number3) if Number3 is not None else None

    # Check 3 conditions and if either one of the condition is true, then it is true.
    chk1 = (value1 == value2)
    chk2 = (value1 == value3)
    chk3 = (value2 == value3)
    return chk1 or chk2 or chk3


# Test(s)
print(compareEquality("1", 1, 2)) # Expect True
print(compareEquality("1", 3, 1)) # Expect True
print(compareEquality("2", 3, 3)) # Expect True
print(compareEquality("1", "1", 1)) # Expect True
print(compareEquality(1, 2, 3)) # Expect False
print(compareEquality("1", "2", "3")) # Expect False
print(compareEquality(None, "1", 1)) # Expect True
print(compareEquality(None, "1", None)) # Expect True
