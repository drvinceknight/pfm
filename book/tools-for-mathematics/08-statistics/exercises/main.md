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

# Exercises

**After** completing the tutorial attempt the following exercises.

**If you are not sure how to do something, have a look at the "How To" section.**

1. For each of the following sets of data:

   1. ```
      data_set_1 = (
          74,
          -7,
          58,
          82,
          60,
          3,
          49,
          85,
          24,
          99,
          73,
          76,
          11,
          -4,
          61,
          87,
          93,
          13,
          1,
          28,
      )
      ```
   2. ```
      data_set_2 = (
          65,
          59,
          81,
          81,
          76,
          93,
          91,
          88,
          55,
          97,
          86,
          94,
          79,
          54,
          63,
          56,
          58,
          77,
          85,
          88,
      )
      ```
   3. ```
      data_set_3 = (
          0.31,
          -0.13,
          0.19,
          0.46,
          -0.27,
          -0.06,
          0.20,
          0.42,
          -0.07,
          0.11,
          -0.11,
          -0.43,
          -0.36,
          0.45,
          -0.42,
          0.11,
          0.08,
          0.31,
          0.48,
          0.17,
      )
      ```
   4. ```
      data_set_4 = (
          2,
          4,
          2,
          2,
          2,
          2,
          2,
          3,
          2,
          2,
          2,
          4,
          2,
          4,
          2,
          2,
          3,
          4,
          3,
          4,
      )
      ```

      Calculate:

      - The mean,
      - The median,
      - The max,
      - The min,
      - The population standard deviation,
      - The sample standard deviation,
      - The population variance,
      - The sample variance,
      - The quartiles (the set of $n=4$ quantiles),
      - The deciles (the set of $n=10$ quantiles),

2. Calculate the sample covariance and the correlation coefficient for the
   following pairs of data sets from question 1:

   1. `data_set_1` and `data_set_4`
   2. `data_set_3` and `data_set_4`
   3. `data_set_2` and `data_set_3`
   4. `data_set_1` and `data_set_2`

3. For each of the data sets from question 1 obtain the covariance and
   correlation coefficient for the data set with itself.

4. Obtain a line of best fit for the pairs of data sets from question 2.

5. Given a collection of 250 individuals whose height is normally distributed with
   mean 165 and standard deviation 5. What is the expected number of individuals
   with height between 150 and 160?

6. Consider a class test where the score are normally distributed with mean 65
   and standard deviation 5.

   1. What is the probability of failing the class test (a score less than 40)?
   2. What proportion of the class gets a first class mark (a score above 70)?
   3. What is the mark that only 10% of the class would expect to get more than?
