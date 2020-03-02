Post: Reactive discussion + peer exercise
=========================================

Discuss with students what we have seen this week:

- Recursion
- Reading and writing from file

Ask students to go over the corresponding topics in the list of topics. With
their neighbour discuss the expected output, the code itself and ask them to
write their own examples.

Use this as an opportunity to ask students to write code snippets that do the
following problems. Write the problems on the board and let them work on ones of
their choice.

- Verify Pythagoras equation for a given example:

>>> a = 4
>>> b = 3
>>> c = 4
>>> c ** 2 == a ** 2 + b ** 2
False

(Change the c to a 5.)

- Say if a number is a perfect square:

>>> import math
>>> number = 54
>>> if int(math.sqrt(number)) ** 2 == number:
...     print("perfect square")
... else:
...     print("not a perfect square")
not a perfect square

- Find a perfect cube:

>>> candidate = 2
>>> while round(candidate ** (1 / 3)) ** 3 != candidate:
...     candidate += 1
>>> print(candidate)
8

- Obtain a list of 10 random numbers:

>>> import random
>>> numbers = [random.random() for _ in range(10)]
>>> len(numbers) == 10
True

- Use functions and a list to find 50 perfect cubes:

>>> def is_cube(number):
...     return round(number ** (1 / 3)) ** 3 == number
>>> perfect_cubes = []
>>> candidate = 0
>>> while len(perfect_cubes) < 50:
...     candidate += 1
...     if is_cube(candidate):
...         perfect_cubes.append(candidate)

Let us take a look:

>>> for cube in perfect_cubes:
...     print(cube)
1
8
27
64
125
216
343
512
729
1000
1331
1728
2197
2744
3375
4096
4913
5832
6859
8000
9261
10648
12167
13824
15625
17576
19683
21952
24389
27000
29791
32768
35937
39304
42875
46656
50653
54872
59319
64000
68921
74088
79507
85184
91125
97336
103823
110592
117649
125000

Another approach is:

>>> perfect_cubes = [n ** 3 for n in range(1, 51)]
>>> for cube in perfect_cubes:
...     print(cube)
1
8
27
64
125
216
343
512
729
1000
1331
1728
2197
2744
3375
4096
4913
5832
6859
8000
9261
10648
12167
13824
15625
17576
19683
21952
24389
27000
29791
32768
35937
39304
42875
46656
50653
54872
59319
64000
68921
74088
79507
85184
91125
97336
103823
110592
117649
125000
