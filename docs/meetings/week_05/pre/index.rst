Pre: Demo of group theory exercise
==================================

Corresponding lab sheet:
------------------------

- `Object oriented programming <vknight.org/cfm/chapters/05/>`_

Objectives
----------

- Motivate the use of classes by exploring the permutation group.

Notes
-----

Tell students we are going to investigate some group theory.

**Ask them to speak in groups and write down the four properties of a group.**

- Closure: if :math:`a,b\in G` then :math:`\a\cdot\b\in G`.
- Identity: :math:`\exists e in G:\; e\cdot a = a \cdot e = a\forall; a\in G`
- Inverse: :math:`\forall\;a\in G\exists\;a^{-1}\in G:\; a\cdot a^{-1}=e`
- Associativity: :math:`\forall; a,b,c\in G:\; (a\cdot b)\cdot c = a\cdot (b \cdot
  c)`

Consider the permutation group: https://en.wikipedia.org/wiki/Permutation_group.
On two elements: :math:`\{0, 1\}` there are two permutations:

- :math:`\sigma_{01}(0) = 0` and :math:`\sigma_{01}(1) = 1` (identity)
- :math:`\sigma_{10}(0) = 1` and :math:`\sigma_{10}(1) = 0` (flip)

**Ask student to write down the multiplication table for the permutation group
on 2 elements:**

.. math::

   \begin{pmatrix}
    01 & 10\\
    10 & 01
   \end{pmatrix}

Explain that we can create an **abstract** object in Python that allows us to
manipulate these elements in the same way that we can manipulate integers and/or
floats. Or in the same way that :code:`<insert popular video game>` manipulates
characters.

Here is how we create a very basic class that allows us to create an element
corresponding to a given :math:`\sigma`::


    >>> class Permutation():
    ...     """A class that corresponds to an element of a permutation group"""
    ...     def __init__(self, sigma):
    ...         """When creating an instance set attributes."""
    ...         self.sigma = sigma
    ...         self.N = len(sigma)
    ...     def permute(self, vector):
    ...         """Given a vector of integers permute them."""
    ...         return [self.sigma[i] for i in vector]


We can use this to create specific elements of the Permutation group::

    >>> pi_01 = Permutation([0, 1])
    >>> pi_10 = Permutation([1, 0])
    >>> pi_01.sigma, pi_01.N
    ([0, 1], 2)
    >>> pi_10.sigma, pi_10.N
    ([1, 0], 2)


The :code:`permute` method allows us to permute a given vector: for example what
does :math:`\sigma_{10}` do to :math:`(0, 1)`::

    >>> pi_10.permute([0, 1])
    [1, 0]


We now have all we need to define the group operation on the permutation class::


    >>> class Permutation():
    ...     """A class that corresponds to an element of a permutation group"""
    ...     def __init__(self, sigma):
    ...         """When creating an instance set attributes."""
    ...         self.sigma = sigma
    ...         self.N = len(sigma)
    ...     def permute(self, vector):
    ...         """Given a vector of integers permute them."""
    ...         return [self.sigma[i] for i in vector]
    ...     def operate(self, other):
    ...         """Define the group operation on self and other"""
    ...         return Permutation(self.permute(other.permute(range(self.N))))


Redefining our new instances::

    >>> pi_01 = Permutation([0, 1])
    >>> pi_10 = Permutation([1, 0])
    >>> pi_10.operate(pi_01)
    <__main__.Permutation ...>

We see that a new instance of the `Permutation` class has been produced (which
is expected) but we cannot really tell what it is. Let us implement another
special method to do so::

    >>> class Permutation():
    ...     """A class that corresponds to an element of a permutation group"""
    ...     def __init__(self, sigma):
    ...         """When creating an instance set attributes."""
    ...         self.sigma = sigma
    ...         self.N = len(sigma)
    ...     def permute(self, vector):
    ...         """Given a vector of integers permute them."""
    ...         return [self.sigma[i] for i in vector]
    ...     def __repr__(self):
    ...         return str(self.sigma)
    ...     def operate(self, other):
    ...         """Define the group operation on self and other"""
    ...         return Permutation(self.permute(other.permute(range(self.N))))

Redefining our new instances::

    >>> pi_01 = Permutation([0, 1])
    >>> pi_10 = Permutation([1, 0])
    >>> pi_10.operate(pi_01)
    [1, 0]

We see that when :math:`\sigma_{01}` operates on `\sigma_{10}` we get
`\sigma_{10}` back. A nice way to be able to check this using Python's
:code:`==` operator is to include a new special method::

    >>> class Permutation():
    ...     """A class that corresponds to an element of a permutation group"""
    ...     def __init__(self, sigma):
    ...         """When creating an instance set attributes."""
    ...         self.sigma = sigma
    ...         self.N = len(sigma)
    ...     def permute(self, vector):
    ...         """Given a vector of integers permute them."""
    ...         return [self.sigma[i] for i in vector]
    ...     def __repr__(self):
    ...         return str(self.sigma)
    ...     def __eq__(self, other):
    ...         return self.sigma == other.sigma
    ...     def operate(self, other):
    ...         """Define the group operation on self and other"""
    ...         return Permutation(self.permute(other.permute(range(self.N))))

Let us confirm this now::

    >>> pi_01 = Permutation([0, 1])
    >>> pi_10 = Permutation([1, 0])
    >>> pi_10.operate(pi_01) == pi_10
    True

One final change we're going to make is replace the :code:`operate` method to
use a special python method::

    >>> class Permutation():
    ...     """A class that corresponds to an element of a permutation group"""
    ...     def __init__(self, sigma):
    ...         """When creating an instance set attributes."""
    ...         self.sigma = sigma
    ...         self.N = len(sigma)
    ...     def permute(self, vector):
    ...         """Given a vector of integers permute them."""
    ...         return [self.sigma[i] for i in vector]
    ...     def __repr__(self):
    ...         return str(self.sigma)
    ...     def __eq__(self, other):
    ...         return self.sigma == other.sigma
    ...     def __mul__(self, other):
    ...         """Define the group operation on self and other"""
    ...         return Permutation(self.permute(other.permute(range(self.N))))

We can now use the :code:`*` operator::

    >>> pi_01 = Permutation([0, 1])
    >>> pi_10 = Permutation([1, 0])
    >>> pi_10 * pi_01 == pi_10
    True

**Ask student to write code that uses this class to obtain the multiplication
table for our group**::

    >>> def display_multiplication_table(elements):
    ...     for first in elements:
    ...         products = []
    ...         for second in elements:
    ...             products.append(first * second)
    ...         print(products)


We can now use this::

    >>> permutations = [pi_01, pi_10]
    >>> display_multiplication_table(elements=permutations)
    [[0, 1], [1, 0]]
    [[1, 0], [0, 1]]


Let us modify this to look at permutations of size :math:`N=3`.
Explain that we will make use of a very handy Python library for creating
permutations of things::

    >>> import itertools
    >>> N = 3
    >>> permutations = [Permutation(list(perm)) for perm in itertools.permutations(range(N))]
    >>> permutations
    [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

Let us take a look at the multiplication table::

    >>> display_multiplication_table(elements=permutations)
    [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    [[0, 2, 1], [0, 1, 2], [2, 0, 1], [2, 1, 0], [1, 0, 2], [1, 2, 0]]
    [[1, 0, 2], [1, 2, 0], [0, 1, 2], [0, 2, 1], [2, 1, 0], [2, 0, 1]]
    [[1, 2, 0], [1, 0, 2], [2, 1, 0], [2, 0, 1], [0, 1, 2], [0, 2, 1]]
    [[2, 0, 1], [2, 1, 0], [0, 2, 1], [0, 1, 2], [1, 2, 0], [1, 0, 2]]
    [[2, 1, 0], [2, 0, 1], [1, 2, 0], [1, 0, 2], [0, 2, 1], [0, 1, 2]]


**Can students see the various properties closure, associativity, inverse and
identity?**

In any remaining time, invite students to write code that checks these
conditions.

**Walk and discuss with them.**

Closure::

    >>> def test_closure(elements):
    ...     return all(first * second in elements
    ...                for first in elements
    ...                for second in elements)
    >>> test_closure(elements=permutations)
    True

Identity::

    >>> def test_specific_identity_element(elements, identity):
    ...     return all(first * identity == first for first in elements)
    >>> def test_identity_element(elements):
    ...     return any(test_specific_identity_element(elements=elements, identity=identity)
    ...                for identity in permutations)
    >>> test_identity_element(elements=permutations)
    True

Inverse::

    >>> def test_inverse_element_for_given_identity(elements, identity):
    ...     has_inverse = []
    ...     for first in elements:
    ...         products = []
    ...         for second in elements:
    ...             products.append(first * second)
    ...         has_inverse.append(identity in products)
    ...     return all(has_inverse)
    >>> def test_inverse_element(elements):
    ...     return any(test_inverse_element_for_given_identity(elements=permutations, identity=identity)
    ...                for identity in elements)
    >>> test_inverse_element(elements=permutations)
    True

Associativity::

    >>> def test_associativity(elements):
    ...     return all((first * second) * third == first * (second * third)
    ...                for first, second, third in itertools.product(elements, repeat=3))
    >>> test_associativity(elements=permutations)
    True

These can all be brought together::

    >>> def test_group(elements):
    ...     return (test_closure(elements=elements) and
    ...             test_identity_element(elements=elements) and
    ...             test_inverse_element(elements=elements) and
    ...             test_associativity(elements=elements))
    >>> test_group(elements=permutations)
    True

Not all subsets of a group are a group::

    >>> test_group(elements=permutations[:-1])
    False

We can also use this to easily check for larger group sizes::

    >>> N = 4
    >>> permutations = [Permutation(list(perm)) for perm in itertools.permutations(range(N))]
    >>> test_group(elements=permutations)
    True
    >>> N = 5  # This takes a little while
    >>> permutations = [Permutation(list(perm)) for perm in itertools.permutations(range(N))]
    >>> test_group(elements=permutations)
    True

Lab sheet
---------

Highlight the concepts we've seen in the lab sheet. Highlight that most of the
code we have written in this session is "normal python code", there is just a
little bit of novelty surrounding the ability to create abstract things.
