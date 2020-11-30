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

# Tutorial

We are going to solve a particular mathematical problem using a well suited
python library that is not part of the Anaconda distribution.

````{admonition} Problem
Consider 2 sets of pilots and co-pilots. The airline needs to pair every pilot
with a co-pilot. For various reasons every pilot and co-pilot has a preference
of who they fly with.

Before assigning the pairings, the airline asks everyone to list their preferred
rankings of who they would like to work with:

```{list-table} Pilots and their preferences
:header-rows: 1

* - Pilot
  - 1st Preference
  - 2nd Preference
  - 3rd Preference
  - 4th Preference
  - 5th Preference
* - Olivia
  - Emily
  - Mia
  - Grace
  - Poppy
  - Ella
* - Amelia
  - Emily
  - Grace
  - Poppy
  - Ella
  - Mia
* - Isla
  - Emily
  - Grace
  - Poppy
  - Ella
  - Mia
* - Ava
  - Poppy
  - Grace
  - Emily
  - Ella
  - Mia
* - Sophia
  - Ella
  - Emily
  - Mia
  - Poppy
  - Grace
```

```{list-table} Co-pilots and their preferences
:header-rows: 1

* - Co-pilot
  - 1st Preference
  - 2nd Preference
  - 3rd Preference
  - 4th Preference
  - 5th Preference
* - Emily
  - Olivia
  - Amelia
  - Sophia
  - Ava
  - Isla
* - Grace
  - Olivia
  - Amelia
  - Sophia
  - Ava
  - Isla
* - Mia
  - Olivia
  - Sophia
  - Amelia
  - Ava
  - Isla
* - Poppy
  - Sophia
  - Ava
  - Amelia
  - Isla
  - Olivia
* - Ella
  - Isla
  - Sophia
  - Ava
  - Amelia
  - Olivia
```

The airline wants to create a pairing such that no pilot or co-pilot could ask
to be paired with someone they prefer who also prefers them.

For example, if we paired Emily with Ava, and Mia with Olivia. Then both Emily
and Olivia would rather be paired with each other.

````

This problem is an example of a type of game theoretic problem called a
"matching game" {cite}`gusfield1989stable` and there is a Python library that is
designed to solve these problems called `matching` {cite}`matching-project`.

**You can read the full
documentation for the project here: <https://matching.readthedocs.io/>.**

The `matching` library is not included in the Anaconda distribution and the
first thing we need to do to use it is to install it. We follow the instructions
in the documentation and write the following in the command line:

```bash
$ python -m pip install matching
```

Once this is done we can follow the instructions in the documentation for the
library.

Here we adapt the tutorial to create the pilots and co-pilots:

```{code-cell} ipython3
from matching import Player

pilots = [
    Player(name="Olivia"),
    Player(name="Amelia"),
    Player(name="Isla"),
    Player(name="Ava"),
    Player(name="Sophia"),
]

copilots = [
    Player(name="Emily"),
    Player(name="Grace"),
    Player(name="Mia"),
    Player(name="Poppy"),
    Player(name="Ella"),
]
```

Now we set their preferences:

```{code-cell} ipython3
olivia, amelia, isla, ava, sophia = pilots
emily, grace, mia, poppy, ella = copilots

olivia.set_prefs([emily, mia, grace, poppy, ella])
amelia.set_prefs([emily, grace, poppy, ella, mia])
isla.set_prefs([emily, grace, poppy, ella, mia])
ava.set_prefs([poppy, grace, emily, ella, mia])
sophia.set_prefs([ella, emily, mia, poppy, grace])

emily.set_prefs([olivia, amelia, sophia, ava, isla])
grace.set_prefs([olivia, amelia, sophia, ava, isla])
mia.set_prefs([olivia, sophia, amelia, ava, isla])
poppy.set_prefs([sophia, ava, amelia, isla, olivia])
ella.set_prefs([isla, sophia, ava, amelia, olivia])
```

Finally we solve the problem and find a pairing:

```{code-cell} ipython3
from matching.games import StableMarriage

game = StableMarriage(pilots, copilots)
game.solve()
```

As discussed, this particular pairing will pair any pilots or co-pilots that
would rather be paired with someone who would rather be paired with them.

The `matching` documentation has an excellent set of documentation that includes
a theoretic overview of the mathematics used.

```{important}
In this tutorial we have

- Seen how to install a library
```
