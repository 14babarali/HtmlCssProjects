
# Data Types in Python

# Numeric Types
# 1. Integer (int)
a = 10
print(f"Value: {a}, Type: {type(a)}")  # Output: Value: 10, Type: <class 'int'>

# 2. Float (float)
b = 10.5
print(f"Value: {b}, Type: {type(b)}")  # Output: Value: 10.5, Type: <class 'float'>

# 3. Complex (complex)
c = 1 + 2j
print(f"Value: {c}, Type: {type(c)}")  # Output: Value: (1+2j), Type: <class 'complex'>

# Sequence Types
# 1. String (str)
str_var = "Hello, Python!"
print(f"Value: '{str_var}', Type: {type(str_var)}")  # Output: Value: 'Hello, Python!', Type: <class 'str'>

# 2. List (list)
list_var = [1, 2, 3, 4]
print(f"Value: {list_var}, Type: {type(list_var)}")  # Output: Value: [1, 2, 3, 4], Type: <class 'list'>

# 3. Tuple (tuple)
tuple_var = (1, 2, 3, 4)
print(f"Value: {tuple_var}, Type: {type(tuple_var)}")  # Output: Value: (1, 2, 3, 4), Type: <class 'tuple'>

# 4. Range (range)
range_var = range(5)
print(f"Value: {list(range_var)}, Type: {type(range_var)}")  # Output: Value: [0, 1, 2, 3, 4], Type: <class 'range'>

# Mapping Type
# 1. Dictionary (dict)
dict_var = {'a': 1, 'b': 2}
print(f"Value: {dict_var}, Type: {type(dict_var)}")  # Output: Value: {'a': 1, 'b': 2}, Type: <class 'dict'>

# Set Types
# 1. Set (set)
set_var = {1, 2, 3, 4}
print(f"Value: {set_var}, Type: {type(set_var)}")  # Output: Value: {1, 2, 3, 4}, Type: <class 'set'>

# 2. Frozenset (frozenset)
frozenset_var = frozenset([1, 2, 3, 4])
print(f"Value: {frozenset_var}, Type: {type(frozenset_var)}")  # Output: Value: frozenset({1, 2, 3, 4}), Type: <class 'frozenset'>

# Boolean Type
# 1. Boolean (bool)
bool_var = True
print(f"Value: {bool_var}, Type: {type(bool_var)}")  # Output: Value: True, Type: <class 'bool'>

# Binary Types
# 1. Bytes (bytes)
bytes_var = b"Hello"
print(f"Value: {bytes_var}, Type: {type(bytes_var)}")  # Output: Value: b'Hello', Type: <class 'bytes'>

# 2. Bytearray (bytearray)
bytearray_var = bytearray([1, 2, 3])
print(f"Value: {bytearray_var}, Type: {type(bytearray_var)}")  # Output: Value: bytearray(b'\x01\x02\x03'), Type: <class 'bytearray'>

# 3. Memoryview (memoryview)
memoryview_var = memoryview(bytearray_var)
print(f"Value: {memoryview_var}, Type: {type(memoryview_var)}")  # Output: Value: <memory at 0x7feca944c1c0>, Type: <class 'memoryview'>

"""
Additional Notes for Interview Preparation:

1. Numeric Types:
    - Integers (int) are whole numbers without a fractional part.
    - Floats (float) are numbers with a decimal point.
    - Complex numbers (complex) have a real part and an imaginary part, denoted as a + bj.

2. Sequence Types:
    - Strings (str) are sequences of characters enclosed in quotes. They are immutable.
    - Lists (list) are ordered collections of items enclosed in square brackets. They are mutable.
    - Tuples (tuple) are ordered collections of items enclosed in parentheses. They are immutable.
    - Ranges (range) represent sequences of numbers, commonly used in for-loops.

3. Mapping Type:
    - Dictionaries (dict) are collections of key-value pairs. Keys must be unique and immutable, while values can be of any type.

4. Set Types:
    - Sets (set) are unordered collections of unique items.
    - Frozensets (frozenset) are immutable sets.

5. Boolean Type:
    - Booleans (bool) represent truth values: True or False.

6. Binary Types:
    - Bytes (bytes) represent sequences of byte values.
    - Bytearrays (bytearray) are mutable sequences of byte values.
    - Memoryviews (memoryview) allow efficient manipulation of large data buffers.

7. Type Checking:
    - Use the `type()` function to check the data type of a variable.
    - Example: `type(variable)` returns the type of `variable`.

8. Common Operations:
    - Most types support common operations like concatenation, repetition, and membership testing.
    - Example: `'a' in 'apple'` returns `True`.

9. Immutability:
    - Immutable types (e.g., int, float, str, tuple) cannot be changed after their creation. Any modification creates a new object.
    - Mutable types (e.g., list, dict, set) can be changed after their creation without creating new objects.

10. Practical Implications:
    - Understanding data types is crucial for writing efficient and error-free code.
    - Use appropriate data types based on the specific needs of your application (e.g., lists for ordered collections, sets for unique items).

"""
