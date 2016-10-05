---
layout: post
title:  "Lab sheet 01: Variables, Conditional Statements and Loops"
comments: true
---

This first lab sheet will introduce you to programming. You are expected to work
through all the exercises marked as **Tickable**. There are other exercises that
aim to push your understanding further. Finally at the end of the sheet there
are links to other resources and tutorials that you might find
helpful and/or interesting.

There are videos throughout the sheets describing the concepts as well as
showing demos.

[Here is an overview of the course.](https://youtu.be/IB1wc1qgb7Q)

# Installing and running Python

Python is a programming language. There are various other programming languages:

- Java
- C
- C++
- Ruby
- VBA
- and many more.

A programming language allows you to write a program which is a sequence of
instructions that specifies how to perform a computation.

When writing a program you need two things:

- Something to save the code (a text editor for example)
- Something to run the code

We will be using a combination of these 2 things called **notebooks**.

# Install Python

There are various distributions of Python, we will use
[Anaconda](https://www.continuum.io/why-anaconda) which comes packaged with a
variety of other useful tools (including the notebooks I mentioned above).

To install it on your personal machine follow these steps:

1. Go to this webpage:
   [www.continuum.io/downloads](https://www.continuum.io/downloads).
2. Identify and download the version of Python 3 for your operating system
   (Windows, Mac OSX, Linux).
3. Run the installer.

We will use a Jupyter notebook which runs in your browser. To open a local
server find the Continuum navigator and click on Jupyter. You do not need to be
connected to the internet to use this.

[This video is a demo of using a notebook.](https://youtu.be/Zk0RhwCiiNA)

These lab sheets will include code snippets. They show what code you should
write but also the output you should see. Try the following:

```python
>>> print("Hello world")  # Code you should write and below is the output
Hello world

```

**Building blocks**

These questions aim to show you the basic building blocks of programming

1. **TICKABLE** Creating numeric variables.

   [A video describing the concept.](https://youtu.be/KtDrCIauto0)

   [A video demo.](https://youtu.be/Esp-5f0kmpE)

   One of the building block of any
   programming language is variables. This is how we store a particular variable
   that we can reuse:

   ```python
   >>> age = 20  # Pointing the variable age at the numeric value 20
   >>> print(age)  # Recalling the value of the variable
   20

   ```

   It is possible to carry out a variety of numeric operations and reassigning the value of the variable:

   ```python
   >>> age = age + 1  # Adding 1 to age
   >>> print(age)
   21

   ```

   Python has some **short hand** for the above:

   ```python
   >>> age += 1  # Adding 1 to age
   >>> print(age)
   22

   ```

   We can do more than just addition (experiment with these as you might need
   them later on):

   - Subtraction: `-`
   - Multiplication: `*`
   - Division: `/`
   - Exponentiation: `**`
   - Modulo division: `%`

   We can check the type of our variables:

   ```python
   >>> type(5)  # An integer
   <class 'int'>
   >>> type(5.4)  # A 'float'
   <class 'float'>

   ```

   **Experiment with manipulating numeric variables.**

2. **TICKABLE** Creating character variables.

   [A video describing the concept.](https://youtu.be/8-lY3TepDKc)

   [A video demo.](https://youtu.be/v3HBPbf0I3s)

   Another type of variable used is called a character variable. **In
   programming these are called strings**.

   ```python
   >>> firstname = "Vince"
   >>> print(firstname)
   Vince
   >>> print(type(firstname))  # Checking the type
   <class 'str'>

   ```

   We can also create new strings from other ones:

   ```python
   >>> lastname = "Knight"
   >>> fullname = firstname + " " + lastname
   >>> fullname
   'Vince Knight'

   ```

   **Experiment by creating your own strings variables.**

3. **TICKABLE** Boolean variables and if statements.

   [A video describing the concept.](https://youtu.be/IxU67BAFtHI)

   [A video demo.](https://youtu.be/EVAbSgT2Fvk)

   Programming languages can be used to check if statements are true or not. A
   variable that can either be `True` or `False` is called a boolean variable.
   Here is a simple example:

   ```python
   >>> a = 4
   >>> b = 8 / 2
   >>> a == b  # Check if a is equal to b
   True
   >>> a != b  # Check if a is NOT equal to b
   False
   >>> a >= b  # Check if a is bigger or equal to b
   True
   >>> a < b + 1  # Check if a is stricly small than b + 1
   True

   ```

   Note that we can set the statement to be a variable itself:

   ```python
   >>> statement = a == b
   >>> statement
   True
   >>> type(statement)  # This variable is a boolean
   <class 'bool'>

   ```

   We can use this to carry out different operations depending on whether or not
   a boolean is True or False.

   ```python
   >>> n = 11  # Experiment by changing the value of n
   >>> if n <= 5:
   ...    value = 1
   ... elif n % 2 == 0:  # Otherwise if (else if)
   ...    value = 2
   ... else:  # Otherwise
   ...    value = 3
   >>> value
   3

   ```

   **The indentation is important: everything indented after the `if`, `elif`,
   `else` statements is what will be evaluated in that specific case.**

   The above is in essence producing:

   $$f(n)=\begin{cases}
   1&\text{ if } n\leq 5\\
   2&\text{ if } n> 5\text{ and } n \text{ even}\\
   3&\text{ otherwise }\\
   \end{cases}$$

   **Experiment by changing the function \\(f\\) and modifying the code.**

4. **TICKABLE** While loops.

   [A video describing the concept.](https://youtu.be/MnKlyszfa7g)

   [A video demo.](https://youtu.be/orAnw7ZiFV4)

   It is possible to use code to repeat various actions. Here is a `while` loop
   that repeats whatever is indented until the boolean condition is no longer
   true:

   ```python
   >>> count = 0  # A variable to count
   >>> total = 0  # We will sum the first ten numbers
   >>> while count < 10:  # Keep repeating until count if >= 10
   ...     count += 1  # Adding 1 to count
   ...     total += count  # Adding the count to the total
   >>> total
   55

   ```

   **Experiment by summing (or perhaps multiplying?) over a different list of
   items.**

5. **Worked example**

   [A video describing the concept.](https://youtu.be/cPfHwhJgeik)

   [A video demo.](https://www.youtube.com/watch?v=im6yVzlFrys)

   This is a slightly more complex example that brings together the various
   concepts above.

   Let us aim to verify (**this is not a proof!**) that the following statement is
   true:

   $$
   \sum_{i=0}^n i ^ 2 = \frac{n(n+1)(2n+1)}{6}
   $$

   We will do this by computing the left hand side and the right hand side:

   ```python
   >>> n = 20
   >>> rhs = n * (n +  1) * (2 * n + 1) / 6
   >>> lhs = 0
   >>> i = 0
   >>> while i < n:
   ...     i += 1
   ...     lhs += i ** 2
   >>> lhs == rhs
   True

   ```

   We can put all of the above in a `while` loop that will check it for a large
   number of values of n:

   ```python
   >>> max_n = 2000
   >>> n = 0
   >>> while n < max_n:
   ...     n += 1
   ...     rhs = n * (n +  1) * (2 * n + 1) / 6
   ...     lhs = 0
   ...     i = 0
   ...     while i < n:
   ...         i += 1
   ...         lhs += i ** 2
   ...     if lhs != rhs:
   ...         print(False)

   ```

   **Further work**

   These questions aim to push a bit further.

6. **Debugging exercise**

   [A video demo.](https://youtu.be/NvAEDqMRSEw)

   Below is code that attempts to verify the following identity for all values
   less than 2000.

   $$
   \sum_{i=0}^ni ^ 3 = \frac{\left(n ^ 2 + n\right)^{2}}{4}
   $$

   **There is at least one error (also called a bug) in the
   code**. Find and fix all the bugs.

   ```python
   max_n = 2000
   n = 0
   while n > max_n:
       n += 2
       rhs = ((n ** 2 + 2 * n) ** 2) / 4
       lhs = 0
       i = 0
       while i < n:
           i += 1
           lhs += i ** 2
       if lhs != rhs:
           print(False)

   ```

7. Use code to check the following identity:

   $$\sum_{i=0}^{n}i=\frac{n(n+1)}{2}$$

   for \(n=20\).

8. **TICKABLE** Modify **the above** (Q7) to check it for all values less than
   2000.

9. Calculates the sum of the first natural numbers less than 1000 that are not
   divisible by 3.

10. Calculates the sum of the first 1000 natural numbers that are not
   divisible by 3.

11. It can be shown (you are not required to check this) that the following
    sequence:

    $$x_{n+1}=\frac{x_n + K / x_{n}}{2}$$

    approaches \\(\sqrt{K}\\) as \\(n\\) increases. Write some code to
    verify this to any given level of precision.

# Further resources

- [The official Python introduction
  tutorial](https://docs.python.org/3/tutorial/introduction.html)
- [A non programmers tutorial for
  Python](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3):
    - [Variables](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Hello,_World).
    - [Debugging](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Debugging).
    - [Boolean
      variables](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions).
    - [If
      statements](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Decisions).
    - [For](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/For_Loops)
      and
      [while](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Count_to_10)
      loops.
- [Learn X in Y minutes for Python3](https://learnxinyminutes.com/docs/python3/)
- [A good youtube
  playlist](https://www.youtube.com/watch?v=HBxCHonP6Ro&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_)
- [Automating the boring stuff: a nice
  book](https://automatetheboringstuff.com/)
