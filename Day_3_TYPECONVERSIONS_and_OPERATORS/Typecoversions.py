'''Type Conversion: converting one datatype into another datatype is called type conversion.
casting in python is done by constructor functions.
'''
# Examples:Int
print(int(3))
print(int(124e-2))
print(int(True))
# print(int("Ganesh")) string cannot be converted into integer.
# print(int(8+9j))     complex cannot be converted into integer.

# Float
print(float(3))
print(float(4.55))
print(float(True))
# print(float("Ganesh"))  string cannot be converted into float.
# print(float(9+4j))      complex cannot be converted into float.

# Bool: any datatype can be converted to boolean.
print(bool(24))
print(bool())
print(bool(0))
print(bool("string"))
print(bool(3.45))
print(bool(3+9j))

# String: any datatype can be converted to string.
print(str(1))
print(str(3.43))
print(str("Ganesh"))
print(str(True))
print(type(str(9+7j)))

# complex
print(complex(1))
print(complex(3.45))
print(complex(True))
print(complex(8+4j))
# print(complex("Ganesh"))  string cannot be converted into complex.