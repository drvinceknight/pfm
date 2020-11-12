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

# How

## How to define a class

We define a class using the `class` keyword:

````{tip}
```
class Name:
    """
    A docstring between triple quotation to describe what the class represents
    """
    INDENTED BLOCKS OF CODE
```
````

For example to create a class for a country:

```{code-cell} ipython3
class Country:
    """
    A class to represent a country
    """
```

## How to create an instance of the class

Once a class is defined we call it using the `()`:

````{tip}
```
Name()
```
````

For example:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

first_country = Country()
first_country
```

```{code-cell} ipython3
:tags: [nbval-ignore-output]

second_country = Country()
second_country
```

The at … is a pointer to the location of the instance in memory. If you re run
the code that location will change.

## How to create an attribute

Attributes are variables that belong to instances of classes. There can be
created and accessed using `.name_of_variable`.

For example, the following creates the attributes:

```{code-cell} ipython3
first_country.name = "Narnia"
first_country.amount_of_magic = 500
```

We can access them:

```{code-cell} ipython3
first_country.name
```

```{code-cell} ipython3
first_country.amount_of_magic
```

We can manipulate them in place:

```{code-cell} ipython3
first_country.amount_of_magic += 100
first_country.amount_of_magic
```

## How to create and call a method

Methods are functions that belong to classes. We define a function using the
`def` keyword (short for define). The first variable of a method is always the
specific instance that will call the method (it is passed implicitly).

````{tip}
```
class Name:
    """
    A docstring between triple quotation to describe what the class represents
    """
    def name(self, variable1, variable2, …):
        """
        A docstring between triple quotation to describe what is happening
        """
        INDENTED BLOCK OF CODE
        return output
```
````

For example let us create a class for a country that has the ability to "spend"
magic:

```{code-cell} ipython3
class Country:
    """
    A class to represent a country
    """

    def spend_magic(self, amount_spent):
        """Updates the magic attribute by subtracting amount_spent"""
        self.amount_of_magic -= amount_spent
```

Now we can use it:

```{code-cell} ipython3
first_country = Country()
first_country.name = "Narnia"
first_country.amount_of_magic = 500
first_country.spend_magic(amount_spent=100)
first_country.amount_of_magic
```

```{attention}
Even though the method is defined as taking two variables as inputs: `self` and
`amount_spent` we only have to explicitly pass it `amount_spent`. The first
variable in a method definition always corresponds to the instance on which the
method exists.
```

(how_to_create_and_call_magic_methods)=

## How to create and call magic methods

Some methods can be called in certain situations:

- When creating an instance.
- When wanting to display an instance.

This are referred to as dunder methods as they are all in between two
underscores: `__`.

The method that is called when an instance is created is called `__init__` (for
initialised). For example:

```{code-cell} ipython3
class Country:
    """
    A class to represent a country
    """

    def __init__(self, name, amount_of_magic):
        self.name = name
        self.amount_of_magic = amount_of_magic
```

Now instead of creating an instance and then creating the attributes we can do
those two things at the same time, by passing the variables to the class itself
(which in turn passes them to the `__init__` method):

```{code-cell} ipython3
first_country = Country("Narnia", 500)
first_country.name
```

```{code-cell} ipython3
first_country.amount_of_magic
```

The method that returns a representation of an instance is `__repr__`. For
example:

```{code-cell} ipython3
class Country:
    """
    A class to represent a country
    """

    def __init__(self, name, amount_of_magic):
        self.name = name
        self.amount_of_magic = amount_of_magic

    def __repr__(self):
        """Returns a string representation of the instance"""
        return f"{self.name} with {self.amount_of_magic} magic."
```

```{code-cell} ipython3
first_country = Country("Narnia", 500)
first_country
```

There are numerous other magic methods, such as the `__add__` one used in
{ref}`objects_tutorial`.

(how_to_use_inheritance)=
## How to use inheritance

Inheritance is a tool that allows us to create one class based on another. This
is done by passing the `Old` class to the `New` class.

````{tip}
```
class New(Old)
```
````

For example let us create a class of `MuggleCountry` that overwrites the
`__init__` method but keeps the `__rep__` method of the `Country` class written
in {ref}`how_to_create_and_call_magic_methods`:

```{code-cell} ipython3
class MuggleCountry(Country):
    """
    A class to represent a country with no magic. It only requires the name on
    initialisation.
    """

    def __init__(self, name):
        self.name = name
        self.amount_of_magic = 0
```

This has replaced the `__init__` method but the `__repr__` method is the same:

```{code-cell} ipython3
other_country = MuggleCountry("Wales")
other_country
```
