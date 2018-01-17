---
layout     : post
title      : "06 - Documentation"
comments   : false
---

## Documentation

A very important part of writing software is documenting it.

Documentation can also be written in "markdown", although a lot of packages use
another language called "restructured text".

Good documentation is made up of 4 types of things:

- Tutorial: a basic walk through of doing something (anything) with the
  software.
- How tos: going through specific examples of things that can be done.
- Background: some background reading, perhaps discussing the theory behind the
  software.
- Reference: potential references or very specific code details (a list of all
  functions/classes for example).

These files can be kept in a `docs` directory.

```bash
Pack
|--- src/pack
         |--- __init__.py
         |--- deck.py
         |--- deal.py
|--- tests
     |--- test_pack.py
|--- setup.py
|--- docs/
     |--- tutorial.md
     |--- how-to.md
     |--- background.md
     |--- reference.md
```

## Testing the documentation

It is valuable to include example of python code in the documentation. For
example, `tutorial.md` could resemble:

```markdown
# Tutorial

Let us use the `pack` library to identify the probability of obtain black jack
over any given deal of a hand.

Here is how to obtain the probability using `pack`:

    >>> import pack
	>>> import random
	>>> random.seed(0)
	>>> count_blackjack = 0
	>>> repetitions = 5000
	>>> for _ in range(repetitions):
	...     deck = pack.get_deck()
	...     hand = pack.deal(deck, 2)
	...     values = set([card[0] for card in hand])
	...     if values == {1, 10}:
	...         count_blackjack += 1
	>>> count_blackjack / repetitions
	0.0466

We can also compute the probability theoretically:

	>>> import math
	>>> prob = 4 * 16 / (math.factorial(52) / (math.factorial(2) * math.factorial(52 - 2)))
    >>> round(prob, 6)
    0.048265

```

As we modify the code or write the documentation it is possible to make
mistakes.

The following command ensures `pytest` also checks all `md` files looking for
`>>>` and the correct output:

```bash
pytest --doctest-glob="*.md"
```

## Further information

- Blog post about documentation:
  [https://www.divio.com/en/blog/documentation/](https://www.divio.com/en/blog/documentation/)
- Talk about documentation:
  [https://youtu.be/azf6yzuJt54](https://youtu.be/azf6yzuJt54)
- Readthedocs (a service that will host documentation):
  [http://readthedocs.org](http://readthedocs.org)
