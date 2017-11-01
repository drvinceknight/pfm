---
layout     : post
categories : 2017-2018
title      : "2017-2018: Handout 06 - Returning multiple things and classes"
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

chat: [https://gitter.im/computing-for-mathematics/Lobby](https://gitter.im/computing-for-mathematics/Lobby)

**Office hours: Thursday 1300-1500**

# What was in this lab sheet

- Object oriented programming

# Returning multiple things

It is possible to return more than one thing from a function (this was
particularly relevant when returning the roots of a polynomial equation). For
example let us write a function that returns the \\(n-1\\) and \\(n+1\\) for a
given \\(n\\).

This is one approach that creates a single `list` and returns it:

```python
>>> def boundaries(n):
...     """Return the integers either side of n"""
...     boundaries = [n - 1, n + 1]
...     return boundaries
>>> boundaries(4)
[3, 5]

```

It's also possible to return them as a `tuple` (a particular variable type
we have not spent much time on):

```python
>>> def boundaries(n):
...     """Return the integers either side of n"""
...     return n - 1, n + 1
>>> boundaries(4)
(3, 5)

```

# Another example of object oriented programming

Consider a very simple game (first we need characters):

```python
>>> class Warrior():
...    """ A class for a warrior. 
... 
...    Attributes: 
... 
...     - Name (a string) 
...     - Weapon (a string) 
...     - HP (hit points - a number) 
...     - AP (attack points - a number) 
... 
...    Methods: 
...     - __init__ 
...     - attack (a method that attacks another warrior) 
...     - defend (a method that defends against an attack) 
...    """
...    def __init__(self, name, weapon, AP):
...        self.name = name
...        self.weapon = weapon
...        self.HP = 100
...        self.AP = AP
... 
...    def attack(self, otherwarrior):
...        otherwarrior.defend(self)
... 
...    def defend(self, otherwarrior):
...        self.HP -= otherwarrior.AP

```

Now let us create a function to see who wins a fight:

```python
>>> def whowins(warrior1, warrior2):
...     """ 
...     A function that gets two warriors to fight until one of their HP 
...     becomes negative 
...
...     Arguments: warrior1: an instance of the Warrior class 
...     warrior2: an instance of the Warrior class 
...
...     Output: The name of the winner 
...     """
...
...
...     while warrior1.HP > 0 and warrior2.HP > 0:
...         warrior1.attack(warrior2)
...         warrior2.attack(warrior1)
...     if warrior1.HP > 0:
...         return warrior1.name
...     if warrior2.HP > 0:
...         return warrior2.name
...     return None

```

Let's see how this works out:

```python
>>> sophitia = Warrior('Sophitia', 'Sword and Shield', 6)
>>> siegfried = Warrior('Siegfried', 'BIG sword', 9)
>>> whowins(sophitia, siegfried)
'Siegfried'

```
