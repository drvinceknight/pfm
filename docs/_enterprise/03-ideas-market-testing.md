---
layout     : post
categories : 2016-2017
title      : "03 - Ideas to Market and testing software"
comments   : false
---

- [Slides]({{site.baseurl}}/assets/ideas/main.pdf)

## Testing

When writing software that is to be used you should include tests.

Python has two tools for this:

- [The doctest library](https://docs.python.org/2/library/doctest.html)

  ```python
  def fibonacci(n):
      """
      Return the nth fibonacci number

      >>> fibonacci(3)
      3
      >>> fibonacci(4)
      5
      """
      if n in [0, 1, 2]:
          return 1
      return fibonacci(n - 1) + fibonacci(n - 2)
  ```

  You can doctest that by running:

  ```
  $ python -m doctest main.py
  ```

- [The unittest library](https://docs.python.org/2/library/unittest.html). Here
  is the code I wrote in `test_main.py`:

  ```python
  import unittest
  import main


  class TestFib(unittest.TestCase):
      """
      Test the fibonacci function
      """
      def test_small_numbers(self):
          self.assertEqual(main.fibonacci(0), 1)
          self.assertEqual(main.fibonacci(1), 1)
          self.assertEqual(main.fibonacci(2), 2)
          self.assertEqual(main.fibonacci(3), 3)
          self.assertEqual(main.fibonacci(4), 5)
          self.assertEqual(main.fibonacci(5), 8)
  ```

  You can run those tests by running:

  ```
  $ python -m unittest test_main
  ```
