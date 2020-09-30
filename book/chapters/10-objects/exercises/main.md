---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. Use the class created in {ref}`objects_tutorial` to find the roots of the
   following quadratics:
   1. $f(x) = -4x ^ 2 + x + 6$
   2. $g(x) = 3x - 6$
   3. $h(x) = f(x) + g(x)$
2. Write a class for a Linear expression and use it to find the roots of the
   following expressions:
   1. $f(x) = 2x + 6$
   2. $g(x) = 3x - 6$
   3. $h(x) = f(x) + g(x)$
3. If rain drops were to fall randomly on a square of side length $2r$ the
   probability of the drops landing in an inscribed circle of radius $r$ would
   be given by:

   $$
       P = \frac{\text{Area of circle}}{\text{Area of square}}=\frac{\pi r ^2}{4r^2}=\frac{\pi}{4}
   $$

   Thus, if we can approximate $P$ then we can approximate $\pi$ as $4P$. In this
   question we will write code to approximate $P$ using the random library.

   First create the following class:

   ```
   class Drop():
       """
       A class that to represent a random rain drop falling on a square of
       length r.
       """
       def __init__(self, r=1):
           self.x = (.5 - random.random()) * 2 * r
           self.y = (.5 - random.random()) * 2 * r
           self.incircle = (self.y) ** 2 + (self.x) ** 2 <= r ** 2
   ```

   Note that the above uses the following equation for a circle centred at
   $(0,0)$ of radius $r$:

   $$
       x^2+y^2≤r^2
   $$

   To approximate $P$ create $N=1000$ instances of Drops and count the
   number of those that are in the circle. Use this to approximate $\pi$.
4. In a similar fashion to question 3, approximate the integral
   $\int_{0}^11-x^2\;dx$. Recall that the integral corresponds to the area
   under a curve.
