---
layout: post
title:  "Lab Sheet 03: Reading and writing to file, recursion and algorithms"
---

This lab sheet will allow us to read and write to text files (which lets us
store information even after we close down Python) and introduce recursion.

**Building blocks**

These questions aim to show you the basic building blocks of programming

1. **Tickable** Recursion.

   [A video describing the concept.](https://youtu.be/xFQGaPeaFxg)

   [A video demo.](https://youtu.be/VDXYEJcksPs)

   It is possible to define functions recursively. This is similar to inductive
   proofs in mathematics. To do this we need to consider two things:

   1. A recursive rule;
   2. A base case (that the recursive rule reduces to).

   As an example let us code the following function:

   $$f(n) = \sum_{i=0}^ni$$

   We can see the **'recursive rule'**:

   $$f(n) = f(n-1) + n$$

   We also know that the **'base case'** is:

   $$f(0) = 0$$

   Now let us program this function using recursion:

   ```python
   >>> def sum_of_integers(n):
   ...     """Sum of integers from 0 to n"""
   ...     if n == 0:  # Base case
   ...         return 0
   ...     return sum_of_integers(n - 1) + n  # Recursive rule
   >>> sum_of_integers(3)
   6

   ```

   Here is another example. The factorial function
   \\(n!=n\times(n-1)\times(n-2)...2\times 1\\) can be defined as:

   1. The base case: \\(0!=1\\)
   2. The recursive rule: \\(n!=n\times (n-1)!\\)

   Here is how to code this:

   ```python
   >>> def factorial(n):
   ...     """Returns n! using recursion"""
   ...     if n == 0:  # Base case
   ...         return 1
   ...     return n * factorial(n - 1)
   >>> for n in range(6):
   ...     print(factorial(n))
   1
   1
   2
   6
   24
   120

   ```

   Experiment with modifying the above code.

2. **Tickable** Writing to file.

   [A video describing the concept.](https://youtu.be/w-gEOEOLfiA)

   [A video demo.](https://youtu.be/jFS015bgRS0)

   All of the data we handle with variables, lists and dictionaries lives in
   the ‘memory’ of a computer when our python code is running. When the program
   stops running the data is lost. There will be occasions when we want to write
   our data to a file on the hard drive of a computer (so that it is always
   available even when we turn the computer off).

   To do this we need Python to
   open a file (usually a basic text file), write strings to the text file and
   then close the file. The following code opens (or creates a) text file in
   ‘write mode’ (that’s what the w is for) and writes the numbers 1 to 10 to it:

   ```python
   textfile = open('mytextfile.txt', 'w')  # Open the file in write mode
   for i in range(1, 11):
      textfile.write(str(i) + "\n")
   textfile.close()  # Close the file

   ```

   It is also possible to do it as below (so that we don't have to worry about
   closing the file.

   ```python
   with open('mytextfile.txt', 'w') as textfile:
       for i in range(1, 11):
          textfile.write(str(i) + "\n")

   ```

   Modify the above code to write something different to file.

3. **Tickable** Reading files.

   [A video describing the concept.](https://youtu.be/rn21nG6TZlg)

   [A video demo.](https://youtu.be/jtU3dML5mqw)

   To read data from a file, we need to open the file in ‘read mode’:

   ```python
   >>> with open('mytextfile.txt', 'r') as textfile:
   ...     string = textfile.read()
   >>> string
   '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'

   ```

   This string is not particularly helpful. To transform the string to a
   list we can use the split method which separates a string on a given
   character:

   ```python
   >>> data = string.split('\n')
   >>> data
   ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '']

   ```

   We see that we have a list of **strings** and also have a last empy item.
   Here we clean that up (converting the strings to integers and ignoring the
   last item):

   ```python
   >>> data = [int(e) for e in data[:-1]]
   >>> data
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   ```

   Use this code to verify that you can read in from the file you wrote.

4. **Worked example**

   [A video describing the concept.](https://youtu.be/WgmgK7K3WUM)

   [A video demo.](https://youtu.be/7245uwUjSkI)

   The Fibonacci sequence can be thought of as:

   1. The base case: \\(f(0)=f(1)=1\\)
   2. The recursive rule: \\(f(n)=f(n-1)+f(n-2)\\)

   Here is how to code this:

   ```python
   >>> def fibonacci(n):
   ...     """Returns the nth fibonacci number using recursion"""
   ...     if n in [0, 1]:  # Base case
   ...         return 1
   ...     return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive rule
   >>> for n in range(10):
   ...     print(fibonacci(n))
   1
   1
   2
   3
   5
   8
   13
   21
   34
   55

   ```

   It can be shown that the Fibonacci sequence can also be given by:

   $$f(n) = \frac{\phi^{(n + 1)} + (-\phi)^{-(n + 1)}}{\sqrt{5}}$$

   Where \\(\phi\\) is the golden ratio:

   $$\phi = \frac{1 - \sqrt{5}}{2}$$

   Let us use the recursive function to verify that this formula is correct for
   the first 200 values of \\(n\\):

   ```python
   >>> import math  # This is a library that has various helpful function
   >>> phi = (1 + math.sqrt(5)) / 2
   >>> def alt_fibonacci(n):
   ...     """Return the nth fibonacci number using the golden ratio formula"""
   ...     return (phi ** (n + 1) - (-phi) ** (-(n + 1))) / (math.sqrt(5))

   ```

   As we did in the previous sheet let us write a function to check the formula:

   ```python
   >>> def check_formula(K):
   ...     """Check the golden ratio formula"""
   ...     return fibonacci(K) == round(alt_fibonacci(K), 1)
   >>> check_formula(3)
   True

   ```

   Let us check this for the first 30 values:

   ```python
   >>> checks = [check_formula(K) for K in range(30)]
   >>> all(checks)  # `all` combines all booleans in a list
   True

   ```

   We can then use the alternative formula to write a large file with the
   first 500 Fibonacci numbers:

   ```python
   with open('fibonacci.txt', 'w') as textfile:
       for n in range(500):
           fib_number = int(round(alt_fibonacci(n), 0))  # Rounding the number
           textfile.write(str(fib_number) + "\n")  # Writing it
   ```

   **Further work**

   These questions aim to push a bit further.

5. **Debugging exercise**

   The following is an attempt to write \\(n!\\) as a recursive function. Find
   and fix all the bugs.

   ```python
   def factorial(n):
       """A function that returns factorial n"""
       return n * factoial(n)
   ```

6. Write a recursive function that returns the Catalan numbers \\(C(n)\\)
   defined by the following:

   1. Base case: \\(C(0)=1\\);
   2. Recursive rule: \\(C(n)=\sum_{i=0}^{n-1}C(i)C(n-1-i)\\);

7. **Tickable** Verify for the first 15 values of \\(n\\) that the following
   alternative formula also gives the Catalan numbers (this is in fact the more
   commonly used formula):

   $$C(n) = \frac{(2n)!}{(n+1)!n!}$$

   Write the first 500 catalan numbers to file.

   You can use the factorial function we defined in this lab sheet (question 1) or you   can use the `math` library: `math.factorial`.

8. The file [primes.csv]({{site.baseurl}}/assets/data/primes.csv) contains the
   first million prime numbers. Use it to attempt to verify
   [Goldbach's conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture).

9. Python has it's own functions to sort a list. This question investigates how
   one of those algorithms works.

   If we have a list of items that are not in the correct order, one algorithm
   to sort them is call 'insertion sort'. This illustrates how it works:

   ![Insertion sort]({{site.baseurl}}/assets/Images/W04-img02.png)

   Here is some 'pseudo code' that describes this algorithm:

   ```
   SET FIRSTUNSORTED TO 0
   WHILE NOT SORTED:
       FIND SMALLEST UNSORTED ITEM
       SWAP FIRST UNSORTED ITEM WITH EARLIEST UNSORTED ITEM
       SET FIRSTUNSORTED TO FIRSTUNSORTED + 1
   ```

   Attempt to write a function in python `insertion_sort` that takes a list of
   numbers and returns it sorted.

10. Similarly to sorting there are also various algorithms for searching
    (and finding) elements in a list. One of these is called 'binary search'
    illustrated below:

    ![Binary search]({{site.baseurl}}/assets/Images/W04-img03.png)

    Here is some 'pseudo code' that describes this algorithm:

    ```
    SORT THE LIST
    SET INDEX TO 0
    SET LAST TO LENGTH - 1
    SET FOUND TO FALSE
    WHILE FIRST <= LAST AND NOT FOUND:
        SET MIDDLE TO (FIRST + LAST) / 2
        IF DATA[MIDDLE] = ITEM:
            SET FOUND TO TRUE
        ELSE:
            IF DATA[MIDDLE] > ITEM:
                SET LAST TO MIDDLE - 1
            ELSE:
                SET FIRST TO MIDDLE + 1
    RETURN MIDDLE
    ```

    Attempt to write a function in python `binary_search` which takes a list and
    an item to search for in that list. It should return the position of the
    item.

11. Repeated calls of a recursive function can actually be quite slow
    (we have to recalculate the values each time). **Recursion is a tool that
    helps write nice code, often when we do not know an alternative formula**.
    There are ways to deal with this inefficiency:

    1. Use an alternative formula (if it's known)
    2. Use a technique called 'caching'. Python 3 has some nice inbuilt ways to
    do this but you can also easily build your own with dictionaries (see
    previous sheet).

    Investigate caching and see if you can implement it yourself and/or use
    the inbuilt functions to use it.

# Further resources

- [A non programmers tutorial for
  Python:
  Recursion](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Recursion):
- [A nice tutorial from The Python
  Course on recursion](http://www.python-course.eu/recursive_functions.php)
- [Reading and writing csv files with the csv library](https://pymotw.com/3/csv/)
- [Docuentation for the caching function available in Python
  3](https://docs.python.org/3/library/functools.html#functools.lru_cache)
- [Insertion sort in
  Python](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html)
- [Binary search in
  Python](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html)
