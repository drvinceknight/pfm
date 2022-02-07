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

1. For each of the following functions calculate $\frac{df}{dx}$, $\frac{d^2f}{dx^2}$ and $\int f(x) dx$.
   1. $f(x) = x$
   2. $f(x) = x ^{\frac{1}{3}}$
   3. $f(x) = 2 x (x - 3) (\sin(x) - 5)$
   4. $f(x) = 3  x ^ 3 + 6 \sqrt{x} + 3$
2. Consider the function $f(x)=2x+1$. By differentiating _from first principles_ show that $f'(x)=2$.
3. Consider the second derivative $f''(x)=6x+4$ of some cubic function $f(x)$.
   1. Find $f'(x)$
   2. You are given that $f(0)=10$ and $f(1)=13$, find $f(x)$.
   3. Find all the stationary points of $f(x)$ and determine their nature.
4. Consider the function $f(x)=\frac{2}{3}x ^ 3 + b x ^ 2 + 2 x + 3$, where $b$ is some undetermined coefficient.
   1. Find $f'(x)$ and $f''(x)$
   2. You are given that $f(x)$ has a stationary point at $x=2$. Use this information to find $b$.
   3. Find the coordinates of the other stationary point.
   4. Determine the nature of all stationary points.
5. Consider the functions $f(x)=-x^2+4x+4$ and $g(x)=3x^2-2x-2$.
   1. Create a variable `turning_points` which has value the turning points of $f(x)$.
   2. Create variable `intersection_points` which has value of the points where $f(x)$ and $g(x)$ intersect.
   3. Using your answers to parts 2., calculate the area of the region between $f$ and $g$. Assign this value to a variable `area_between`.
