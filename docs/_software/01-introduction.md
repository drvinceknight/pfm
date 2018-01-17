---
layout     : post
title      : "01 - Enterprise and Software development"
comments   : false
---


## Introduction to software development

# One big group exercise

- Mathematics
- Code
- Add value

# Setting up your company/group

4 members

- Project manager: responsible for direction and delivery.
- Secretary: responsible for communication.

(Fill in the google form: see email)

# Minutes

- Meetings 2 or 3 times a week.
- Secretary responsibility: bring minutes to the Lecture.

# Assessment

- Week 3: 3 page report (30%)
- Week 6: Grand council
- Week 11: Group presentations (70%)

Marking criteria:

- [Project proposal (30%)]({{site.baseurl}}/dev/proposal)
- [Presentation (70%)]({{site.baseurl}}/dev/presentation)

## Personal development

This component is an opportunity for personal development.

- Identify and respond to others' needs, thus building upon their networking
  and negotiation skills.
- Build trust and develop effective relationships with others both in and
  outside of the team.
- Work with/connect with external bodies, groups or stakeholders in order to
  develop their networking, negotiating and relationship building skills.
- Develop awareness of recognising value in ideas.
- Think speculatively, employing both convergent and divergent approaches to
  arriving at a solution.
- Develop and produce multiple solutions to identified problems through
  evaluation and analysis.
- Review and evaluate multiple solutions in contexts that anticipate change and
  contain elements of ambiguity, uncertainty or risk.
- Recognise that generating innovative solutions can sometimes be more
  meaningful and useful than the final outcome itself.

## Suggested timeline

# Phase 1: Research

- Week 1 - Introductory lecture: identify idea and group.
- Week 2 - Lecture on library skills: identify research for project.
- Week 3 - What is USP of your project: research and plan.

# Phase 2: Development

- Week 4 - Project management
- Week 5 - Pitching: prepare pitch
- Week 6 - Grand Council

# Phase 3: Production

- Week 7 - Version control
- Week 8 - Documentation
- Week 9 - Packaging
- Week 10 - Preparation
- Week 11 - Final presentation

## Project

The goal of your project is to write a Python library.
You have used libraries already. When
you call `import numpy` you are using the `numpy` library.

**Your goal is to write a library with a set of useful functions/classes**

There are various tools you will need to do this.

### Text editor

Open a text editor (I recommend [VS Code](https://code.visualstudio.com) or
[atom](https://atom.io)) and create a file entitled `my_library.py`.

In that file let us define the following function:

```python
def fibonacci(n):
    """
    A function to return the nth Fibonacci number
    """
    if n in [0, 1]:
        return 1
    return fibonacci(n) + fibonacci(n - 1)
```

Now, open a Jupyter notebook in the same directory as that file and run the
following:

```python
import my_library
my_library.fibonacci(5)
```

Let us now create a directory/folder entitled `pack`. In there let us create
three files:

```
pack/
|--- __init__.py
|--- cards.py
|--- deal.py
```

In the `cards.py` file write:

```python
import itertools
values = list(range(1, 11)) + [10] * 3
suits = ["D", "S", "H", "C"]

def get_deck():
    """
    Return a standard deck of 52 cards.
    """
    return list(itertools.product(values, suits))
```

In the `deal.py` file write:

```python
import random
def shuffle(deck):
    """
    Randomly shuffle a deck
    """
    random.shuffle(deck)

def deal(deck, number_of_cards):
    """
    Return a hand of `number_of_cards` cards.
    """
    shuffle(deck)
    hand = []

    for _ in range(number_of_cards):
        hand.append(deck.pop())

    return hand
```

Finally, let us bring this together in the `__init__.py` file:

```python
from .cards import get_deck
from .deal import deal
```

Now open a Jupyter notebook and type:

```python
import pack
deck = pack.get_deck()
hand = pack.deal(deck, 2)
hand, len(deck)
```

This is essentially all that a library is.
Other things that will be covered in this term:

- Packaging and structure (so that it's possible for anyone to use the code you
  create).
- Version control (making it possible to track and merge changes of a project
  over time).
- Automated testing of code (ensuring code does what it is supposed to do).


## Tools

I suggest you consider using some of the following tools for your workflow:

# Messaging system

These allow for quick exchange of information. There are various solutions
available:

- WhatsApp, Messenger, Snapchat: familiarity however not all are portable or
  support productivity tools.
- [Slack](https://slack.com/is), [gitter](https://gitter.im): popular in the
  workplace and good support for integration with other tools.

# Issue tracker (to do list)

Having a cloud based issue/task tracker is common practice. There are a number
of these available:

- [Trello](https://trello.com/): simple user interface and a lot of
  functionality.
- [Github](https://github.com/): this is very specific to software projects and
  is connected to using a software tool called "git".

# Version control

With your code some of you might want to learn version control: this is a tool
to handle different versions of files and merge them for you. One of the most
popular version control tools is called [git](https://git-scm.com/).

For more information about git and github see:

- [https://vknight.org/rsd/chapters/05/](https://vknight.org/rsd/chapters/05/)
- [https://vknight.org/rsd/chapters/06/](https://vknight.org/rsd/chapters/06/)
