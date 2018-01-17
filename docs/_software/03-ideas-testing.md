---
layout     : post
title      : "03 - Ideas and testing"
comments   : false
---


## Ideas and testing

# USP

Give very careful consideration to your unique selling point.

- If you are developing a code base for a company product, what is the unique
  selling point of the company?
- If you are undertaking some mathematical research or building software to
  carry out some mathematical research: what is the unique aspect you are
  considering?

# Is your code correct?

Once you have a USP and know what you want to write code for, it is important to
be able to confirm your code is correct **and that it stays correct**.

Let us continue to use the example of our deck of cards library.

Everytime we make a change to the library we could open and rerun the Jupyter
notebook and confirm the results stay the same.

There are potential pitfalls with this, one which includes the time it takes to
open a notebook and rerun it.

Another approach we will discuss here is using automated testing. First, we need
to explore a different approach to interfacing with a computer.

# The command line

We are used to interfacing with a computer using our mouse and clicking on the
"graphical user interface", another approach is to use a **command line** tool:

- On Windows: search for the "Anaconda prompt"
- On Mac OS: search for the "terminal"

Using this you can navigate files and folders of your computer. The following
command is `cd` which is used to change directory.

```bash
cd <directory>
```

Let us use this to navigate to the same folder as the `deck/`.

Commands that can be helpful:

- On Windows

  ```bash
  cd ..  # Go back to the parent directory
  dir  # List the current directory
  ```
- On Mac OS

  ```bash
  cd ..  # Go back to the parent directory
  ls  # List the current directory
  ```

Now that we have navigated to the correct directory, let us open our text editor
and write a new file called `test_deck.py`.

```python
import pack
deck = pack.get_deck()
hand = pack.deal(deck, 2)
print(len(hand), len(deck))
```

In the command line tool, let us run this python file (this is a new way to
execute python code!):

```bash
python test_deck.py
```

You should see the following output:

```
2, 50
```

That is in effect confirming that when we deal 2 cards from our deck we do not
lose any cards.

So if at any stage we were to modify the code we could re run this file and
expect to see the same output.

This is not ideal: it's an easy mistake to forget the expected output.

Let us modify the `test_deck.py` file to use the `assert` command:

```python
import deck
deck = pack.get_deck()
hand = pack.deal(deck, 2)
assert (len(hand), len(deck)) == (2, 50)
```

Now running the code gives no output.

## Using testing frameworks

In this particular case, a lack of input is what we expect. Note that it is
possible to write tests in a way that makes them a bit more helpful.

First, in the command line let us install a library called `pytest`:

```bash
pip install pytest
```

Next, change the `test_pack.py` file:

```python
import pack

def test_card_counts():
    deck = pack.get_deck()
    hand = pack.deal(deck, 2)
    assert (len(hand), len(deck)) == (2, 50)
```

Now in the command line, just type:

```bash
pytest
```

This will automatically find all files with `test_` in the name, and in those
files run all function with `test_` in the name.

## Writing tests for all our functions

The test we have written is a single test that checks one aspect, it is helpful
to write tests for each specific component.

For example let us change the `test_pack.py` file:

```python
import pack

def test_card_counts():
    deck = pack.get_deck()
    hand = pack.deal(deck, 2)
    assert (len(hand), len(deck)) == (2, 50)

def test_get_pack():
    deck = pack.get_deck()
    assert len(deck) == 52
    assert deck[0] == (0, 'D')
```

## More info

For further information about testing there are many great resources. The
documentation for `pytest` is a good place to start
[docs.pytest.org/en/latest/](https://docs.pytest.org/en/latest/).

For more information about using the command line see:
[vknight.org/rsd/chapters/01/](https://vknight.org/rsd/chapters/01/).
