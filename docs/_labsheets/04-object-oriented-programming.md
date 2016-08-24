---
layout: post
title:  "Lab Sheet 04: Object Oriented Programming"
---

This lab sheet introduces object oriented programming. We have been using
object oriented programming throughout the previous lab sheets. Here we will
learn how to create our own objects (what this means become clear).

**Building blocks**

These questions aim to show you the basic building blocks of programming

1. **Tickable** Writing a class.

   The main idea behind object orientated programming (OOP) is to
   create abstract structures that allow us to not worry about data. Alan Kay
   came up with the concept and is quoted as saying: ‘I wanted to get rid of
   data’. Instead of keeping track of variables using lists and arrays and
   writing specific functions for each operation we could be trying to do we use
   a system similar to the cellular structure in biology:

   ![Biology]({{site.baseurl}}/assets/Images/W05-img01.png)

   Here is an image showing the various things we will consider in this lab
   sheet:

   ![Classes]({{site.baseurl}}/assets/Images/W05-img02.png)

   Creating a class in Python is similar to creating a function: we write down
   the rules:

   ```python
   >>> class Student:
   ...     pass  # This is just a dummy line (we will use real code later)

   ```

   We can then create 'instances' of this class:

   ```python
   >>> vince = Student()
   >>> zoe = Student()
   >>> vince
   <Student object at ...>
   >>> zoe
   <Student object at ...>

   ```

   The `at ...` is a pointer to the location of the instance in memory. If you
   re run the code that location will change.

   We have already seen examples of classes in Python:

   - Integers;
   - Strings;
   - Lists.

   There are many more and we are going to see how to build our own.

   **Experiment with building an instance of the Student class.**

2. **Tickable** Attributes

   The above student class is not very useful. We now see how to make our
   objects ‘hold’ information. The following code re-creates our previous
   student class but gives the class some 'attributes':

   ```python
   >>> class Student:
   ...     courses = ['Biology', 'Mathematics', 'English']
   ...     age = 12
   ...     gender = "Female"

   ```

   Now our class itself has some information:

   ```python
   >>> Student.age
   12

   ```

   This information is also passed on to any instances of the class:

   ```python
   >>> vince = Student()
   >>> vince.courses
   ['Biology', 'Mathematics', 'English']
   >>> vince.age
   12
   >>> vince.gender
   'Female'

   ```

   We can use and/or modify those attributes just like any other python
   variable:

   ```python
   >>> vince.age += 1
   >>> vince.age
   13
   >>> vince.gender = 'Male'
   >>> vince.gender
   'Male'
   >>> vince.courses.append('Chemistry')
   >>> vince.courses
   ['Biology', 'Mathematics', 'English', 'Chemistry']

   ```

   **Create instances with attributes and experiment with them.**

3. **Tickable** Methods

   We will now see how to make classes 'do' things. These are called 'methods'
   and they are just functions 'attached' to classes.

   ```python
   >>> class Student:
   ...     """A class to represent a student"""
   ...     courses = ['Biology', 'Mathematics', 'English']
   ...     age = 12
   ...     gender = "Female"
   ...     def have_a_birthday(self, years=1):
   ...         """Increment the age"""
   ...         self.age += years  # self corresponds to the instance
   >>> vince = Student()
   >>> vince.have_a_birthday()
   >>> vince.age
   13
   >>> vince.have_a_birthday(years=10)
   >>> vince.age
   23

   ```

   There are various 'special' methods names that act in particular ways.
   One of these is `__init__`, this method is called when an instance is
   created ('initialised'):

   ```python
   >>> class Student:
   ...     """A class to represent a student"""
   ...     def __init__(self, courses, age, gender):
   ...         self.courses = courses
   ...         self.age = age
   ...         self.gender = gender
   ...     def have_a_birthday(self, years=1):
   ...         """Increment the age"""
   ...         self.age += years  # self corresponds to the instance

   ```

   Now we can easily create instances with given attributes:

   ```python
   >>> vince = Student(["Maths"], 32, "Male")
   >>> zoe = Student(["Biology"], 31, "Female")
   >>> vince.courses, vince.age, vince.gender
   (['Maths'], 32, 'Male')
   >>> zoe.courses, zoe.age, zoe.gender
   (['Biology'], 31, 'Female')

   ```

   There are various other 'special' methods, we will see one of them in the
   worked example.

   **Create instances of the Student class with these new methods.**

4. **Inheritance**

   One final (very important) aspect of object oriented programming is the
   concept of inheritance. This allows us to create new classes from other ones.
   In practice this saves replicating code as we can change only certain methods
   as required.

   To do this we simply create the new class as usual but pass it the old class:

   ```python
   class NewClass(OldClass):
       ...
   ```

   For example, let us create a student who we know is born on the 29th of
   February (a date that only occurs once every 4 years):

   ```python
   >>> class LeapYearStudent(Student):
   ...     """A class for a student born on the 29th of February"""
   ...     # Note that we do not have to rewrite the init method
   ...     def have_a_birthday(self, years=1):
   ...         self.age += int(years / 4)
   ...     def complain(self):
   ...         """Return a string complaining about birthday"""
   ...         # This is a new method that the Student class does not have
   ...         return "I wish I was not born on the 29th of Feb"

   ```

   ```python
   >>> geraint = LeapYearStudent(["Maths"], 22, "Male")
   >>> geraint.have_a_birthday()
   >>> geraint.age  # Still  22
   22
   >>> geraint.have_a_birthday(8)
   >>> geraint.age
   24
   >>> geraint.complain()
   'I wish I was not born on the 29th of Feb'

   ```

   **Experiment with the above code: how would it work if leap year was every 3
   years?**

5. **Worked example**

   Let us assume we want to study linear expressions. These are expressions
   of the form:

   $$ax+b$$

   We are interested, for example, in what the value of \\(x\\) for which a
   linear expression is 0. This is called the 'root' and is the solution to the
   following equation:

   $$ax+b=0$$

   This is obviously an easy thing to study but we're going to assume it's not
   and build a class to represent and manipulate linear expressions.


   ```python
   >>> class LinearExpression:
   ...     """A class for a linear expression"""
   ...     def __init__(self, a, b):
   ...         self.a = a
   ...         self.b = b
   ...     def root(self):
   ...         """Return the root of the linear expression"""
   ...         return - self.b / self.a
   ...     def __add__(self, linexp):
   ...         """A special method: lets us have addition between expressions"""
   ...         return LinearExpression(self.a + linexp.a, self.b + linexp.b)
   ...     def __repr__(self):
   ...         """A special method: changes the way an instance is displayed"""
   ...         return "Linear expression: " + str(self.a) + "x + " + str(self.b)
   >>> exp = LinearExpression(2, 4)
   >>> exp  # This output is given by the `__repr__` method
   Linear expression: 2x + 4
   >>> exp.a
   2
   >>> exp.b
   4
   >>> exp.root()
   -2.0
   >>> exp2 = LinearExpression(5, -2)
   >>> exp + exp2  # This works because of the `__add__` method
   Linear expression: 7x + 2

   ```

   This class works just fine but we quickly arrive at a problem:

   ```python
   >>> exp1 = LinearExpression(2, 4)
   >>> exp2 = LinearExpression(-2, 4)
   >>> exp3 = exp1 + exp2
   >>> exp3
   Linear expression: 0x + 8
   >>> exp3.root()
   Traceback (most recent call last):
   ...
   ZeroDivisionError: division by zero

   ```

   We get an error because our `root` method is attempting to divide by 0.
   Let's fix that:

   ```python
   >>> class LinearExpression:
   ...     """A class for a linear expression"""
   ...     def __init__(self, a, b):
   ...         self.a = a
   ...         self.b = b
   ...     def root(self):
   ...         """Return the root of the linear expression"""
   ...         if self.a != 0:
   ...             return - self.b / self.a
   ...         return False
   ...     def __add__(self, linexp):
   ...         """A special method: let's us have addition between expressions"""
   ...         return LinearExpression(self.a + linexp.a, self.b + linexp.b)
   ...     def __repr__(self):
   ...         """A special method: changes the default way an instance is displayed"""
   ...         return "Linear expression: " + str(self.a) + "x + " + str(self.b)
   >>> exp3 = LinearExpression(0, 8)
   >>> exp3.root()
   False

   ```

   Let us now use this to verify the following simple fact. If \\(f(x) =
   a_1x+b_1\\) and \\(g(x) = a_2x+b_2\\), then the root of \\(f(x) + g(x)\\) is
   given by:

   $$\frac{a_1x_1 + a_2x_2}{a_1+a_2}$$

   where \\(x_1\\) is the root of \\(f\\) and \\(x_2\\) is the root of \\(g\\)
   (if they exist).

   First let's write a function that checks this for a given set of
   \\(a_1, a_2, b_1, b_2\\).

   ```python
   >>> def check_result(a1, a2, b1, b2):
   ...     """Check that the relationship holds"""
   ...     f = LinearExpression(a1, b1)
   ...     g = LinearExpression(a2, b2)
   ...     k = f + g
   ...     x1 = f.root()
   ...     x2 = g.root()
   ...     x3 = k.root()
   ...     if x1 and x2 and x3:  # Assuming our three expressions have a root
   ...         return (a1 * x1 + a2 * x2) / (a1 + a2) == x3
   ...     return True  # If f, g have no roots the relationship is still true
   >>> check_result(2, 3, 4, 5)
   True

   ```

   We will verify this by randomly sampling values for \\(a_1, a_2, b_1, b_2\\).

   ```python
   >>> import random  # Importing the random module
   >>> N = 1000  # THe number of samples
   >>> checks = []
   >>> for _ in range(N):
   ...     a1 = random.randint(-10, 10)
   ...     a2 = random.randint(-10, 10)
   ...     b1 = random.randint(-10, 10)
   ...     b2 = random.randint(-10, 10)
   ...     checks.append(check_result(a1, a2, b1, b2))
   >>> all(checks)
   True

   ```

   **Further work**

   These questions aim to push a bit further.

6. Build a class for a quadratic expression:

   $$ax^2+bx+c$$

   Include a method for adding two quadratic expressions together and also a
   method to calculate the roots of the expression.

7. **Tickable** The data file
   [W05_D01.csv]({{site.baseurl}}/assets/Data/W05_D01.csv) contains data
   corresponding to quadratic expression of the form:

   ```
   a,b,c
   1,4,7
   11,7,14
   16,2,8
   14,7,13
   2,20,5
   ...
   ```

   Read in the data file (you might find it helpful to read about the `csv`
   library) and identify how many quadratics have real roots.

8. If rain drops were to fall randomly on a square of side length \\(2r\\) the
   probability of the drops landing in an inscribed circle of radius \\(r\\)
   would be given by:

   $$P = \frac{\text{Area of circle}}{\text{Area of square}}=\frac{\pi r ^2}{4r^2}=\frac{\pi}{4}$$

   ![Circle]({{site.baseurl}}/assets/Images/W05-img03.png)

   Thus, if we can approximate \\(P\\) then we can approximate \\(\pi\\) as
   \\(4P\\). In this question we will write code to approximate \\(P\\) using
   the random python library.

   First of all, create a class for a rain drop (make sure you
   understand the code!):

   ```python
   >>> class Drop():
   ...     def __init__(self, r=1):
   ...         self.x = (.5 - random.random()) * 2 * r
   ...         self.y = (.5 - random.random()) * 2 * r
   ...         self.incircle = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2

   ```

    Note that the above uses the following equation for a circle centred at
    \\((0,0)\\) of radius \\(r\\):

    $$x^2+y^22≤r^2$$

    To approximate \\(P\\) simply create \\(N=1000\\) instances of Drops and
    count the number of those that are in the circle.  Use this to approximate
    \\(\pi\\).

    What happens if you increase \\(N\\)?

    What value of \\(N\\) seems to give \\(\pi\\P correct to 3
    decimal places?

    (This is an example of a technique called Monte Carlo Simulation.)

9. In a similar fashion to question 8, approximate the integral
   \\(\int_{0}^11-x^2\;dx\\).

   Recall that the integral corresponds to the area under a curve.
   Furthermore this diagram might be helpful:

   ![Grid]({{site.baseurl}}/assets/Images/gridwithplot.png)

10. Re create the linear expression class using **inheritance** and the
    quadratic quadratic expression class from question 6.

# Further resources

- [A non programmers tutorial for
  Python:
  Object Oriented
  Programming](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Intro_to_Object_Oriented_Programming_in_Python_3)
- [A nice tutorial: a role playing
  example](http://inventwithpython.com/blog/2014/12/02/why-is-object-oriented-programming-useful-with-an-role-playing-game-example)
- [A video about classed suggested by a student
  tutor](https://www.youtube.com/watch?v=trOZBgZ8F_c)
