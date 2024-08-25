
# Mutable vs Immutable in Python

# Immutable Objects
# Immutable objects cannot be changed after their creation.
# Examples include int, float, bool, string, tuple, and frozenset.

# Integer (int) is immutable
num = 10
print(f"Initial value of num: {num}")  # Output: 10
print(f"Memory address of num: {id(num)}")

# Modifying the value of num creates a new object
num = 20
print(f"New value of num: {num}")  # Output: 20
print(f"Memory address of num after change: {id(num)}")

# String (str) is immutable
name = "Alice"
print(f"Initial value of name: {name}")  # Output: Alice
print(f"Memory address of name: {id(name)}")

# Modifying the string creates a new object
name = "Bob"
print(f"New value of name: {name}")  # Output: Bob
print(f"Memory address of name after change: {id(name)}")

# Tuple is immutable
my_tuple = (1, 2, 3)
print(f"Initial value of my_tuple: {my_tuple}")  # Output: (1, 2, 3)
print(f"Memory address of my_tuple: {id(my_tuple)}")

# Modifying the tuple creates a new object
my_tuple = (4, 5, 6)
print(f"New value of my_tuple: {my_tuple}")  # Output: (4, 5, 6)
print(f"Memory address of my_tuple after change: {id(my_tuple)}")

# Mutable Objects
# Mutable objects can be changed after their creation.
# Examples include list, dict, set, and most class instances.

# List is mutable
my_list = [1, 2, 3]
print(f"Initial value of my_list: {my_list}")  # Output: [1, 2, 3]
print(f"Memory address of my_list: {id(my_list)}")

# Modifying the list does not create a new object
my_list.append(4)
print(f"New value of my_list: {my_list}")  # Output: [1, 2, 3, 4]
print(f"Memory address of my_list after change: {id(my_list)}")

# Dictionary (dict) is mutable
my_dict = {'a': 1, 'b': 2}
print(f"Initial value of my_dict: {my_dict}")  # Output: {'a': 1, 'b': 2}
print(f"Memory address of my_dict: {id(my_dict)}")

# Modifying the dictionary does not create a new object
my_dict['c'] = 3
print(f"New value of my_dict: {my_dict}")  # Output: {'a': 1, 'b': 2, 'c': 3}
print(f"Memory address of my_dict after change: {id(my_dict)}")

# Set is mutable
my_set = {1, 2, 3}
print(f"Initial value of my_set: {my_set}")  # Output: {1, 2, 3}
print(f"Memory address of my_set: {id(my_set)}")

# Modifying the set does not create a new object
my_set.add(4)
print(f"New value of my_set: {my_set}")  # Output: {1, 2, 3, 4}
print(f"Memory address of my_set after change: {id(my_set)}")

"""
Additional Notes for Interview Preparation:

1. Understanding Immutability:
    - Immutable objects cannot be altered after creation. Any change creates a new object.
    - This can lead to performance benefits and predictable behavior, especially in multi-threaded environments.
    - Examples: int, float, bool, str, tuple, frozenset.

2. Understanding Mutability:
    - Mutable objects can be changed after creation. They allow modifications without creating new objects.
    - This can be useful for efficient data manipulation, but requires careful handling to avoid unintended side-effects.
    - Examples: list, dict, set, custom class instances.

3. Practical Implications:
    - Immutability can prevent bugs related to unintended changes and can be safer in concurrent programming.
    - Mutability can lead to performance improvements by avoiding the creation of new objects for modifications.

4. Memory Management:
    - Use the `id()` function to check the memory address of an object. If the address changes after a modification, a new object was created.
    - This is useful for understanding and debugging code behavior related to object mutability.

5. Best Practices:
    - Use immutable types for data that should not change to ensure integrity.
    - Use mutable types for collections of data that will be modified frequently.
    - Be mindful of the choice between mutable and immutable types based on the specific needs of your application.

6. Example Questions:
    - Explain the difference between mutable and immutable types in Python.
    - How does immutability affect the behavior of variables when passed to functions?
    - Discuss scenarios where you would prefer immutable types over mutable types and vice versa.
"""
