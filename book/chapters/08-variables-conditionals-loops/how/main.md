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

## Define an integer variable

To define an integer variable we use the `=` operator which is the assignment
operator. We create the name of the variable then the assignment operator
followed by the integer value.

````{tip}
```
name_of_variable = int_value
```
````

For example:

```{code-cell} ipython3
year = 2020
year
```

```{attention}
When choosing a variable name there are some rules to follow:

- No spaces, use `_` instead.
- Cannot start with a number or other special characters.

There are other important conventions:

- Use explicit names that clearly describe what the variable is (try not to use
  `i`, `a` unless those refer to specific mathematical variables).
- Do not use `CamelCase` but use `snake_case` when combining words. This follows
  the Python convention called [PEP8](https://www.python.org/dev/peps/pep-0008/)
```

## Define a float variable

To define a float variable we use the `=` operator which is the assignment
operator. We create the name of the variable then the assignment operator
followed by the real value.

````{tip}
```
name_of_variable = float_value
```
````

For example:

```{code-cell} ipython3
cms_in_an_inch = 2.54
cms_in_an_inch
```

## Define a string variable

To define a string variable we use the `=` operator which is the assignment
operator. We create the name of the variable then the assignment operator
followed by the string which is a combination of characters between quotation
marks.

````{tip}
```
name_of_variable = string_value
```
````

For example:

```{code-cell} ipython3
capital_of_dominica = "roseau"
capital_of_dominica
```

## Define a boolean variable

A boolean variable is one of two things: `True` or `False`. To define a boolean
variable we again use the `=` operator which is the assignment operator. We
create the name of the variable then the assignment operator followed by the
boolean variable (either `True` or `False`).


````{tip}
```
name_of_variable = boolean_value
```
````

For example:

```{code-cell} ipython3
john_nash_has_a_noble = True
john_nash_has_a_noble
```

```{tip}
{ref}`creating_boolean_variables` gives an overview of how to create boolean
variables from other variables.
```


## How to check the type of a variable

We can get the type of a variable using the `type` tool.

````{tip}
```
type(object)
```

Where `object` is any variable.
````

For example:

```{code-cell} ipython3
year = 2020
type(year)
```

```{code-cell} ipython3
cms_in_an_inch = 2.54
type(cms_in_an_inch)
```

```{code-cell} ipython3
capital_of_dominica = "roseau"
type(capital_of_dominica)
```

```{warning}
If a numeric variable is given with any decimal part (including 0) then it is
considered to be a float.
```

## How to manipulate numeric variables

Numeric values can be combined to create new numeric variables.

1. Addition, $2 + 2$: `2 + 2`;
2. Subtraction, $3 - 1$: `3 - 1`;
3. Multiplication, $3 \times 5$: `3 * 5`;
5. Division, $20 / 5$: `20 / 5`;
6. Exponentiation, $2 ^ 4$: `2 ** 4`;
7. Integer remainder, $5 \mod 2$: `5 % 2`;
8. Combining operations, $\frac{2 ^ 3 + 1}{4}$: `(2 ** 3 + 1) / 4`;

For example:

```{code-cell} ipython3
:tags: [nbval-ignore-output]

cms_in_an_inch = 2.54
average_male_height_in_cms = 170
average_male_height_in_inches = average_male_height_in_cms / cms_in_an_inch
average_male_height_in_inches
```

```{tip}
This is similar to what we did in
{ref}`carry_out_basic_arithmetic_operations`.
```

````{tip}
Some languages, including Python have a shortcut to manipulate a variable "in
place". The following takes the variable `money` and replaces it by 3 times
`money`:

```
money *= 3
```

This is equivalent to:

```
money = money * 3
```
````

## How to include variables in strings

Variables can be used in strings using *string formatting*. There are numerous
ways this can be done in Python but the current best practice is to use
`f`-strings.

````{tip}
```
f"{variable}"
```
````

For example the following creates a string that uses a random number:

```{code-cell} ipython3
import random

random.seed(0)
random_number = random.random()
string = f"Here is a random number: {random_number}"
string
```

## How to combine boolean variables

Boolean variables can be combined using the logical operators `and` and `or`.

````{tip}
```
new_boolean = first_boolean and second_boolean
```
```
````


````{tip}
```
new_boolean = first_boolean or second_boolean
```
```
````

For example:

```{code-cell} ipython3
is_tall = True
is_strong = False
is_tall_and_strong = is_tall and is_strong
is_tall_and_strong
```

```{code-cell} ipython3
is_tall = True
is_strong = False
is_tall_or_strong = is_tall or is_strong
is_tall_or_strong
```

## Run code **if** a condition holds

An important part of giving instructions to a computer is to specify when to do
different things.
This is done using what is called an `if` statement. Following an `if` a boolean
variable is expected, if that boolean is `True` then the indented code that
follows is run. Otherwise it is not.

````{tip}
```
if boolean:
    code to run if boolean is true
else:
    code to run if boolean is false
code to run after either of two previous code blocks are run.
```
````

```{attention}
An `else` statement is not always necessary. Specifically when combined with
functions as seen in {ref}`probability` when combined with `return` statement
the `else` is often not needed.
```

For example the following code selects a random integer between 0 and 100 and
then prints a different string depending on what the number was.


```{code-cell} ipython3
import random

random.seed(0)
random_number = random.randint(0, 100)
is_even = random_number % 2 == 0
if is_even:
    message = f"The random number ({random_number}) is even."
else:
    message = f"The random number ({random_number}) is odd."
message
```

## Repeat code **for** a given set of variables

Given an iterable, it is possible to repeat some code for every item in the
iterable. This is done using what is called a `for` loop. Following the `for` a
dummy variable is given then followed by the `in` keyword and the iterable.
After that the indented code that will be repeated for every value of the
iterable.

````{tip}
```
for dummy_variable in iterable:
    code to repeat
    ```
````

For example the following will print a message for every given value in the
iterable:

```{code-cell} ipython3
iterable = ("Dog", 3, 2, -1.0)
for item in iterable:
    type_of_variable = type(item)
    message = f"The variable {item} has type {type_of_variable}"
    print(message)
```

```{attention}
`for` loops are a common tool across most programming languages. They are
similar to the list comprehensions we saw in
{ref}`create_a_list_using_a_list_comprehension`.

- List comprehensions should be
  specifically used when the goal is to create a collection of items.
- Traditional `for` loops should be used when the code to run for every
  iteration is more complex.
```

```{attention}
Similarly to {ref}`creating_an_iterable_with_a_given_number_of_items` a common
use case of `for` loops is to combine them with a `range` statement to repeat
code a known number of items.
```

(repeat_code_while_a_given_condition_holds)=
## Repeat code **while** a given condition holds

To repeat code while a condition holds a `while` loop can be used. Similarly to
the `if` statement, Following a `while` a boolean
variable is expected, if that boolean is `True` then the indented code that
follows is repeated. After it is run, the boolean is checked once more. When the
boolean is `False` the indented code is skipped.


````{tip}
```
while boolean:
    code to repeat before checking boolean once more
code to run once boolean is False
```
````

Here is some code that repeatedly selects a random number until that number is
even.

```{code-cell} ipython3
import random

random.seed(4)
selected_integer = random.randint(0, 10)
number_of_selections = 1
while selected_integer % 2 == 1:
    selected_integer = random.randint(0, 10)
    number_of_selections += 1
number_of_selections
```
