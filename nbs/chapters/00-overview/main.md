---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Computing for mathematics

## Overview

This course aims to introduce students to programming for mathematics.

It is assumed that students are used to solving problems of the form:

---

> Given the function \\(f:\mathbb{R}\to\mathbb{R}\\) defined by \\(f(x) = x ^ 2 - 3 x + 1\\) obtain the global minima of the function.

To solve this we need to apply our **mathematical knowledge** which tells us to:

1. Differentiate \\(f(x)\\) to get \\(\frac{df}{dx}\\);
2. Equate \\(\frac{df}{dx}=0\\);
3. Use the second derivative test on the solution to the previous equation.

For each of those 3 steps we will usually make use of our **mathematical techniques**:

1. Differentiate \\(f(x)\\):

   \\[\frac{df}{dx} = 2 x - 3\\]

2. Equate \\(\frac{df}{dx}=0\\):

   \\[2x-3 =0 \Rightarrow x = 3/2\\]

3. Use the second derivate test on the solution:

   \\[\frac{d^2f}{dx^2} = 2 > 0\text{ for all values of }x\\]

   Thus \\(x=2/3\\) is the global minima of the function.

---

As we progress as mathematicians **mathematical knowledge** is more prominant than **mathematical technique**: often knowing what to do is the real problem as opposed to having the technical ability to do it.

This is what this course will cover: **programming** allows us to instruct a computer to carry out mathematical techniques.

We will for example learn how to solve the above problem by instructing a computer which **mathematical technique** to carry out.

**This course will teach us how to give the correct instructions to a computer.**

The following is an example, do not worry too much about the specific code used for now:

1. Differentiate \\(f(x)\\) to get \\(\frac{df}{dx}\\);

```python
import sympy as sym

x = sym.Symbol("x")
sym.diff(x ** 2 - 3 * x + 1, x)
```

2. Equate \\(\frac{df}{dx}=0\\):

```python
sym.solveset(2 * x - 3, x)
```

3. Use the second derivate test on the solution:

```python
sym.diff(x ** 2 - 3 * x + 1, x, 2)
```

This diagram is a brief summary:

![](./img/knowledge_vs_technique/main.png)


## How this course will work

Most programming courses introduce students to the building blocks of programming and builds up to using more sophisticated tools for a specific purpose.

This is akin to teaching someone how to forge metal so as to make a nail and then slowly work our way to using more sophisticated tools such as power tools to build a house.

This course will do thing differentially: we will start with using and understanding tools that are helpful to mathematicians. In the later part of the course we will cover the building blocks and you will be able to build your own sophisticated tools.

1. Tools for mathematics;
2. Building tools.

As such the first part of the course will not make use of any novel mathematics. Instead we will consider a number of mathematics problem akin to what will be seen in secondary school:

- Algebraic manipulation
- Calculus (differentiation and integration)
- Permutations and combinations
- Probability
- Linear algebra

The questions we will tackle will be familiar in their presentation and description. **What will be different** is that no **by hand** calculations will be done. We will instead carry them all out using a programming language.

In the second part of the course you will be encouraged to build your own tools to be able to tackle a problem type of your choice (perhaps an area of mathematics you have been introduced to in the first Semester).

## Assessment

There are two pieces of coursework for this coures:

1. An individual piece of coursework: this will be a collection of secondary school type problems that you will solve using programming. This will assess the first part of the course.
2. A group piece of coursework culminating in a presentation. This will assess the second part of the course.

## What is a programming language

## What language will we use

## What tools will we use

## Overview of materials

Every chapter will have 4 parts:

- A tutorial: you will be walked through solving a problem. You will be specifically told what to do and what to expect.
- A how to section: this will be a shorter more succint section that will detail how to carry out specific things.
- A reference section: this will be a section with references to further resources as well as background information about specific things in the chapter.
- An exercise section: this will be a number of exercises that you can work on.
