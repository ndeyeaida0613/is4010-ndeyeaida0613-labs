# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> **Context**: I am working on a Python function `sum_of_evens(numbers)` that is supposed to calculate the sum of all even numbers in a list. However, it currently seems to be summing the odd numbers instead.
>
> **Persona**: You are a senior Python developer with expertise in debugging.
>
> **Task**: Identify the logical error in the provided code and provide the corrected version.
>
> **Format**: Provide the corrected code in a Python code block and a brief explanation of the fix.
>
> **Code**:
> ```python
> def sum_of_evens(numbers):
>     """Calculate the sum of all even numbers in a list.
>
>     Parameters
>     ----------
>     numbers : list of int
>         A list of integers.
>
>     Returns
>     -------
>     int
>         The sum of all even numbers in the list.
>     """
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Changed from == 1 to == 0 to check for even numbers
            total += num
    return total
```

**What I Learned:**
I learned that using the CPTF framework helps the AI understand the exact context and the specific goal, leading to a more accurate fix. In this case, the logical error was in the modulo operation, where `num % 2 == 1` checks for odd numbers instead of even numbers.

---

## Problem 2: Refactoring

**My Prompt:**
> **Context**: I have a function `get_names_of_adults(users)` that correctly returns a list of names for users aged 18 or older. While functional, the code is not very "Pythonic" as it uses an indexed loop.
>
> **Persona**: You are a senior Python developer who values clean, concise, and idiomatic code.
>
> **Task**: Refactor the provided function to be more readable and idiomatic, preferably using a list comprehension.
>
> **Format**: Provide the refactored code in a Python code block and explain why the new version is better.
>
> **Code**:
> ```python
> def get_names_of_adults(users):
>     """Given a list of user dictionaries, returns a list of names of users
>     who are 18 or older.
>
>     Parameters
>     ----------
>     users : list of dict
>         List of user dictionaries with 'name' and 'age' keys.
>
>     Returns
>     -------
>     list of str
>         Names of users who are 18 or older.
>     """
>     results = []
>     for i in range(len(users)):
>         if users[i]['age'] >= 18:
>             results.append(users[i]['name'])
>     return results
> ```

**AI's Corrected Code:**
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user['name'] for user in users if user['age'] >= 18]
```

**What I Learned:**
Refactoring code to be more "Pythonic" often involves replacing manual loops and indexing with more expressive constructs like list comprehensions. This makes the code shorter, more readable, and often more efficient.

---

## Problem 3: Documenting

**My Prompt:**
> **Context**: I have a simple function `calculate_area(length, width)` that calculates the area of a rectangle. It works correctly and handles invalid inputs by raising a ValueError, but it lacks documentation.
>
> **Persona**: You are a technical lead who insists on high-quality documentation for all code.
>
> **Task**: Write a professional NumPy-style docstring for the provided function. Ensure you include sections for Parameters, Returns, and Raises.
>
> **Format**: Provide the function with the new docstring in a Python code block.
>
> **Code**:
> ```python
> def calculate_area(length, width):
>     if length <= 0 or width <= 0:
>         raise ValueError("Length and width must be positive numbers.")
>     return length * width
> ```

**AI's Corrected Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle.
    width : float or int
        The width of the rectangle.

    Returns
    -------
    float or int
        The area of the rectangle.

    Raises
    ------
    ValueError
        If either length or width is non-positive.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**
I learned the importance of structured docstrings, such as the NumPy style, for communicating the intent, parameters, return types, and potential errors of a function. This is especially useful for both human developers and AI coding assistants.
