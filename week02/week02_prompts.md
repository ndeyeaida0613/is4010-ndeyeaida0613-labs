# Lab 02: Prompt Engineering Solutions
## Problem 1: Debugging

**My Prompt:**
   **Context:**   I have a Python function `sum_of_evens` that is supposed to calculate the sum of all even numbers in a list. However, it is currently summing the odd numbers instead. Here is the code:
> ```python
> def sum_of_evens(numbers):
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```
   **Persona:** You are a senior Python developer.
   **Task:** Identify the logical error and provide the corrected version of the function.
   **Format:** Provide the corrected code in a Python code block and briefly explain the fix.

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
        if num% 2 == 0:  # Fixed changed 1 to 0 to check for even number
            total += num
        return total




## Problem 2: Refactoring

**My Prompt:**
 **Context:** I have a Python function get_names_of_adults that extracts the names of users who are 18 or older from a list of dictionaries. The current implementation uses an index-based for loop, which is not very Pythonic.

 def get_names_of_adults(users):
     results = []
     for i in range(len(users)):
         if users[i]['age'] >= 18:
             results.append(users[i]['name'])
     return results
```
 **Persona:** You are a senior Python developer.
 **Task:** Refactor this function to be more clear, concise, and idiomatic using modern Python practices.
 **Format:** Provide the refactored code in a Python code block and explain the improvements made.

**AI's Refactored Code:**
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



## Problem 3: Documenting

**My Prompt:**
> **Context:** I have a Python function `calculate_area` that computes the area of a rectangle and validates that dimensions are positive.
> ```python
> def calculate_area(length, width):
>     if length <= 0 or width <= 0:
>         raise ValueError("Length and width must be positive numbers.")
>     return length * width
> ```
> **Persona:** You are a senior Python developer.
> **Task:** Write a professional NumPy-style docstring for this function, including sections for Parameters, Returns, and Raises.
> **Format:** Provide the function with the new docstring in a Python code block.

**AI's Documented Code:**
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

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
        If either length or width is less than or equal to zero.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

