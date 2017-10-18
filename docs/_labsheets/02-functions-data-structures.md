---
layout: post
title:  "Lab Sheet 02: Data Structures and Functions"
comments: true
---

This lab sheet will move on to understanding how to write functions (very
similar to mathematical functions) and lists (a way of holding data).

**Building blocks**

1. Lists

   [A video describing the concept.](https://youtu.be/oLrrdPQzZas)

   [A video demo.](https://youtu.be/E3BNVFwLWkM)

   Another type of variable in Python (we have already seen numeric and
   character variables) is the list. This type acts as a container that can hold
   multiple other items in an ordered way.

   Here is a list of my favourite numbers:

   ```python
   >>> favourite_numbers = [9, 12, 13, 7]  # Defining a list
   >>> favourite_numbers
   [9, 12, 13, 7]
   >>> type(favourite_numbers)
   <class 'list'>

   ```

   We can do various things to the items in the list:

   ```python
   >>> sum(favourite_numbers)  # Adding all the elements of our list
   41

   >>> max(favourite_numbers)  # Getting the largest element of a list
   13

   >>> min(favourite_numbers)  # Getting the minimum element of a list
   7

   >>> favourite_numbers.append(-100)  # Add another element to a list
   >>> favourite_numbers
   [9, 12, 13, 7, -100]

   ```

   We can also go in to our lists and get specific items. This works just as it
   did with strings:

   ```python
   >>> favourite_numbers[0]  # Getting the first element of a list
   9
   >>> favourite_numbers[1]  # Getting the second element of a list
   12
   >>> favourite_numbers[-1]  # Getting the last element of a list
   -100
   >>> favourite_numbers[2:4]  # Getting the 3rd till the 4th element of a list
   [13, 7]

   ```

   Strings (see in in the previous lab sheet) and lists are similar in that they
   are 'containers' for items. A lot of the manipulation that works with lists
   also works with strings:

   ```python
   >>> firstname = "Vince"
   >>> len(firstname)  # How many characters are in the variable
   5
   >>> firstname[0]  # We can point at individual characters, 0 is the first
   'V'
   >>> firstname[4]
   'e'
   >>> firstname[-1]  # We can use negative number to start counting from the end
   'e'
   >>> firstname[0:4]  # We can 'slice' strings
   'Vinc'

   ```

   Experiment by creating lists and manipulating them.

2. For loops.

   [A video describing the concept.](https://youtu.be/icgb6I85pX8)

   [A video demo.](https://youtu.be/npJqdB1pqdQ)

   In the previous sheet, we saw that a `while` loop can be used to repeat a
   code chunk until a boolean condition is `False`. It is also possible to
   repeat an action for all elements of a list.

   ```python
   >>> items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Creating a list
   >>> total = 0
   >>> for item in items:
   ...     total += item
   >>> total
   55

   ```

   A quick way to get a list of integers is the `range` command:

   ```python
   >>> for k in range(10):
   ...     print(k)
   0
   1
   2
   3
   4
   5
   6
   7
   8
   9

   ```

   **Experiment by summing (or perhaps multiplying?) over a different list of
   items.**

3. List comprehension

   [A video describing the concept.](https://youtu.be/tEyxAfVWEGE)

   [A video demo.](https://youtu.be/893eu9F75gI)

   Here is a list of squares, done using the `append` method and a for loop.

   ```python
   >>> total = 0
   >>> square_of_favourite_numbers = []  # Create an empty list
   >>> for n in favourite_numbers:
   ...     square_of_favourite_numbers.append(n ** 2)
   >>> square_of_favourite_numbers
   [81, 144, 169, 49, 10000]

   ```

   We can however do this using some nice Python syntax called a list
   comprehension:

   ```python
   >>> square_of_favourite_numbers = [x ** 2 for x in favourite_numbers]
   >>> square_of_favourite_numbers
   [81, 144, 169, 49, 10000]

   ```

   This is familiar, as it replicates mathematical notation. For example here
   is how to get the sum of the elements in the following set:

   $$\{n \in S \;| \text{ if } n \text{ is divisible by  2}\}$$

   (This is mathematical notation for "the set of all things in \\(S\\) that are
   divisible by 2".)

   ```python
   >>> sum([n for n in favourite_numbers if n % 2 == 0])
   -88

   ```

   Experiment by modifying this code to create a different list.

4. Writing simple functions.

   [A video describing the concept.](https://youtu.be/_8gcT7_o84U)

   [A video demo.](https://youtu.be/FHXiY22e6NQ)

   Often we want to be able to use code more than once. The way to do this is to
   write a function. Here is a very simple example. This creates a function that
   returns a string saying "Hello world":

   ```python
   >>> def say_hi():
   ...     return "Hello world"

   ```

   Now, to **use** that function we need to call the function:

   ```python
   >>> say_hi()
   'Hello world'

   ```

   It is good practice to break down code in to smaller functions that make
   it easier to read.

   Experiment with changing what the `say_hi` function says.

5. Functions with variables.

   [A video describing the concept.](https://youtu.be/S-pzofb4Ok0)

   [A video demo.](https://youtu.be/X13uTM0GPjI)

   It is more useful to include variables in our functions (in the exact same
   way as for mathematical functions!).

   Let us revisit the mathematical function we described in the previous lab
   sheet:

   $$f(n)=\begin{cases}
   1&\text{ if } n\leq 5\\
   2&\text{ if } n> 5\text{ and } n \text{ even}\\
   3&\text{ otherwise }\\
   \end{cases}$$

   Here is the code that defines this function (compare it to the code we wrote
   in the previous lab sheet):

   ```python
   >>> def f(n):
   ...     """
   ...     This is text in between triple quoatation marks is a doc string.
   ...     We use it to describe what a function does. For example here we would
   ...     write: This function returns f(n) as described above.
   ...     """
   ...     if n <= 5:
   ...        return 1
   ...     elif n % 2 == 0:  # Otherwise if (else if)
   ...        return 2
   ...     else:  # Otherwise
   ...        return 3
   >>> f(11)
   3

   ```

   We can also have functions with more than 1 variable:

   ```python
   >>> def simple_sum(a, b):
   ...     """Returns the sum of a and b"""
   ...     return a + b
   >>> simple_sum(5, 7)
   12

   ```

   Finally, it is also possible to have default variables:

   ```python
   >>> def simple_sum(a=5, b=1):
   ...     """Returns the sum of a and b"""
   ...     return a + b
   >>> simple_sum()
   6
   >>> simple_sum(b=2)
   7
   >>> simple_sum(a=3)
   4

   ```

   Experiment by creating your own function.

6. **Worked example**

   [A video describing the concept.](https://youtu.be/Y1mdHL7OZiU)

   [A video demo.](https://youtu.be/h0_nnFmRwUQ)

   The Fibonacci numbers are defined by the following mathematical formula:

   $$
   f_n = \begin{cases}
   1,\text{ if } n \in \{0, 1\}\\
   f_{n - 1} + f_{n - 2}, \text{ otherwise}
   \end{cases}
   $$

   The goal of this question is to verify the following theorem about the sum
   of the first Fibonacci numbers:

   $$\sum_{i=0}^n f_i = f_{n + 2} - 1$$

   As an example with \\(n=3\\) we have: \\(f_0=f_1=1, f_2=2, f_3=3\\) and
   \\(f_5=8\\). We indeed have:

   $$
   \sum_{i=0}^nf_i = 1 + 1 + 2 + 3 = 7 = 8 - 1 = f_{3 + 2} - 1
   $$

   We are going to automate checking the formula using Python.
   Let us first write a function for the Fibonacci sequence itself:

   ```python
   >>> def fibonacci(n):
   ...     """Returns the n th fibonacci number"""
   ...     if n in [0, 1]:  # The special case of n being 0 or 1
   ...         return 1
   ...     a = 1  # Setting the starting values
   ...     b = 1
   ...     for i in range(n - 1):  # Going through the first n - 1 terms
   ...         temp = b  # A temporary variable to remember the value of b
   ...         b = a + b  # New value of b
   ...         a = temp  # New value of a (old value of b)
   ...     return b

   ```

   Let us now call this function to check that it is correct:

   ```python
   >>> for n in range(5):
   ...     print(fibonacci(n))
   1
   1
   2
   3
   5

   ```

   We can now obtain a list of the first \\(K\\) fibonacci numbers and check the
   theorem:

   ```python
   >>> K = 3
   >>> list_of_fib = [fibonacci(n) for n in range(K + 1)]
   >>> sum(list_of_fib) == fibonacci(K + 2) - 1
   True

   ```

   We can put this code that checks if a relationship is true in to a new
   function:

   ```python
   >>> def check_theorem(K):
   ...     """
   ...     Check the relationship for the sum of the first K fibonacci numbers
   ...     """
   ...     list_of_fib = [fibonacci(n) for n in range(K + 1)]
   ...     return  sum(list_of_fib) == fibonacci(K + 2) - 1

   ```


   Let us now check that our theorem can be checked for the first 200
   values of:

   ```python
   >>> checks = [check_theorem(K) for K in range(200)]
   >>> all(checks)  # `all` combines all booleans in a list
   True

   ```

   **Further work**

   These questions aim to push a bit further.

7. **Debugging exercise**

   The following is an attempt to write \\(n!\\) as a function. Find
   and fix all the bugs.

   ```python
   def factorial(n):
       """A function that returns factorial n"""
       for i in range(n)
           prod *= i
   ```

8. Write a function that returns the triangular numbers \\(T_n\\):

   $$T_n=\frac{n(n+1)}{2}$$

9. Use code to check that the following relationship is true:

   $$\sum_{i=0}^{n}T_i=\frac{n(n+1)(n+2)}{6}$$

10. Create a list with the first 1300 integers divisible by 3. What is the largest
   such number? What is the smallest such number? What is the mean of these
   numbers?

11. Investigate the use of the python `random` library. Use this to simulate the
    [Monty hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem):

    - Write a function that simulates the play of the game when you 'stick' with
      the initial choice.
    - Write a function that simulates the play of the game when you 'change' your
      choice.
    - Repeat the play of the game using both those functions and compare the
      probability of winning.

12. A data type that we have not considered are dictionaries. These are a
    specific type of what is generally called a 'hash table'. Find information
    about dictionaries and experiment with them.

# Further resources

- [A non programmers tutorial for
  Python:
  Functions](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Defining_Functions):
- [A nice tutorial from The Python
  Course](http://www.python-course.eu/python3_functions.php)

# Solutions

[Solutions available.](https://gist.github.com/drvinceknight/1c5e32180672fd0e1a189f68f0703b63)
