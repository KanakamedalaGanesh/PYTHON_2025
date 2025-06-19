'''Datatypes: It is used to define the type of data that a variable can hold. For example, int, float, str, etc.
Datatypes in python:
4 types:
i.Numeric
ii.Sequential
iii.Sets
iv.Dictionary
1. Int: It is used to store integer values. For example, 10,20,30, etc.
2. Float: It is used to store floating point values. For example, 10.5, 20.7, etc.
3. complex: It is used to store complex numbers. For example, 3+4j , 5+6j, etc.
4. Boolean: It is used to store boolean values. For example, True, False , etc.
5. String: It is used to store string values. For example, "Hello", "World", etc.
6. List: It is used to store a collection of values. For example, [1,2,3] , [4,5,6], etc.
7. Array: It is used to store a collection of values. For example, [1,2,3] , [4,5,6], etc.
8. ByteArray: It is used to store a collection of bytes. For example, b'Hello', b'World', etc.
9. Tuple: It is used to store a collection of values. For example, (1,2,3),(4,5,6), etc.
10. Set: It is used to store a collection of unique values. For example, {1,2 ,3},{4,5,6}, etc.
11. Dictionary: It is used to store a collection of key-value pairs. For example, {" name": "John", "age": 25} , {"name": "Jane", "age": 30}, etc.

'''
# sys:It is a module in python which is used to interact with the operating system. It is used to perform system-specific tasks such as executing a system command, terminating a process, etc.
# sizeof: It is a function in python which is used to get the memory size of an object in bytes.
import sys
i = 10,30,"Ganesh"
print(i.__sizeof__())
print(sys.getsizeof(i))
print(type(i),i)

f=98.0
print(type(f),f)

c=complex(6,9)
print(type(c),c)

a=True
print(type(a),a)

b='Ganesh'
print(type(b),b)

c=[1,2,3,"Ganesh",True]
print(type(c),c)

d={1,3,4,6}
print(type(d),d)