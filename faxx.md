# Understanding `and` and `or`

`and` and `or` are logical operators in Python that are used to combine boolean values.

`and` is a logical operator that will return `True` if both the conditions are `True`, else it will return `False`.

Example:

# Understanding `set`

`set` is a built-in data structure in Python that contains a collection of unordered elements. The elements must be unique, i.e., they cannot be repeated.

Example:

s = {1, 2, 3, 1}
print(s) # {1, 2, 3}
# Difference between `==` and `is`

`==` and `is` are operators in Python used for comparison, but they serve different purposes.

- `==` is the equality operator. It checks whether the values of two objects are equal. It is used to compare the contents of objects, meaning it checks if the data or information contained in the objects is the same.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, because the contents of both lists are the same
```

- `is` is the identity operator. It checks whether two references point to the same object in memory. It is used to compare the memory addresses of the objects, meaning it checks if both variables refer to the exact same object.

Example:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, because both a and b refer to the same object in memory
print(a is c)  # False, because a and c refer to different objects, even though they have the same content
```

In summary, use `==` to compare values for equality and `is` to check if two variables point to the same object.

