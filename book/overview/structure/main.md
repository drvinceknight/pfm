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

# How this book is structured

A traditional structure of this book would probably reorder the chapters as follows:

1. [Chapter 1](chp:using_notebooks).
2. Chapter on variables (seen in [Chapter 11](chp:variables_conditionals_and_loops)).
3. Chapter on conditionals (seen in [Chapter 11](chp:variables_conditionals_and_loops)).
4. Chapter on loops (seen in [Chapter 11](chp:variables_conditionals_and_loops)).
5. Chapter on functions (seen in [Chapter 12](chp:functions_and_data_structures)).
6. Chapter on data structures (seen in [Chapter 12](chp:functions_and_data_structures)).
7. [Chapter 13](chp:objects).
8. Chapter on Sympy (with an overview of the topics in Chapters [3](chp:algebra)–[5](chp:matrices) and [10](chp:differential_equations)).
9. [Chapter 6](chp:combinatorics).
10. [Chapter 7](chp:probability).
11. [Chapter 8](chp:sequences).
12. [Chapter 9](chp:statistics).
13. [Chapter 14](chp:cli).
14. [Chapter 15](chp:modularisation).
15. [Chapter 16](chp:documentation).
16. [Chapter 17](chp:testing).

The choice to _flip_ this structure and start with real use cases (and not code recipes) is deliberate.
The tools covered in chapters [1](chp:algebra)–[10](chp:differential_equations) can be used with
little to no programming knowledge, needing only an understanding of the mathematics.
Following this, the topics covered in chapters
[11](chp:variables_conditionals_and_loops)–[13](chp:objects) let the reader expand on their
knowledge and learn the basics of programming. Finally, the topics and techniques covered in
chapters [14](chp:cli)–[17](chp:testing) show how modern research software is designed.

# What is in this book?

Most programming texts introduce readers to the building blocks of programming and  
then build up to using more sophisticated tools for a specific purpose.

This is akin to teaching someone how to forge metal to make a nail and then  
slowly work towards using more sophisticated tools, such as power tools,  
to build a house.

This book approaches things differently: you will start by using and understanding  
tools that are helpful to mathematicians. In the later part of the book, you will  
cover the building blocks and be able to create your own sophisticated tools.

## How is this book organised?

The book is in two parts:

1. **Tools for mathematics**
2. **Building tools**

The first part of the book will not make use of any novel mathematics. Instead,  
you will explore topics typically covered in secondary school mathematics:

- Algebraic manipulation
- Calculus (differentiation and integration)
- Combinatorics (permutations and combinations)
- Probability
- Linear algebra
- Sequences
- Statistics
- Differential equations

The problems you will tackle aim to be familiar in their presentation and  
description. **What will be different** is that no **by-hand** calculations will  
be performed. You will instead use a programming language to carry them out.

In the second part of the book, you will be encouraged to build your own tools for  
tackling problems of your choice.

Every chapter will have four parts:

- **Tutorial**: You will be guided step-by-step through solving a problem.  
  You will be explicitly told what to do and what to expect.

- **How-to section**: A shorter, succinct reference section detailing how to  
  perform specific tasks.

- **Further information**: References to additional resources, background  
  information on key concepts, and answers to common questions.

- **Exercises**: A selection of exercises to practice and reinforce what you've  
  learned.

Several Python libraries, programming techniques, and frameworks are covered in this book:

- [Diataxis](chp:documentation)
- [Recursion](chp:sequences)
- [`itertools`](chp:combinatorics)
- [`random`](chp:probability)
- [`statistics`](chp:statistics)
- `sympy`  
  (Chapters [3](chp:algebra)–[5](chp:matrices),
  [10](chp:differential_equations))
