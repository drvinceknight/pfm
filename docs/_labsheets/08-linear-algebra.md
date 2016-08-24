---
layout: post
title:  "Lab Sheet 08: Linear Algebra"
---

In this lab sheet we will learn how to use Python to study linear algebra.

**Building blocks**

1. **Tickable** Linear algebra is the study of systems of linear equations. Many
   mathematical problems reduce to solving systems of linear equations. Here is
   one such system that we will use as a running example:

   $$\begin{cases}
   5\alpha+\beta-\gamma=0\\
   -\alpha+2\beta+4\gamma=-2\\
   \alpha+\beta+\gamma=4
   \end{cases}$$

   We can represent this system of equations as a **matrix** equation (if you
   are not familiar with this you will learn more about it soon):

   $$Ax=b$$

   Where \\(A\\) corresponds to the coefficients of the equations above, and
   \\(b\\) to the right hand side:

   $$A=\begin{pmatrix}
   5&1&-1\\
   -1&2&4\\
   1&1&1\\
   \end{pmatrix}
   $$

   $$b=\begin{pmatrix}
   0\\
   -2\\
   4
   \end{pmatrix}$$

   **Solving a system of linear equations can be done very efficiently when
   using this matrix notation.** There are various Python libraries that are
   able to do this. We will use **NumPy** which is a library that specialises in
   efficient numerical manipulation (it does a lot more than just solve linear
   equations). Let us set up the above matrix equation:

   ```python
   >>> import numpy as np  # We won't import * here to avoid confusion
   >>> A = np.array([[5, 1, -1], [-1, 2, 4], [1, 1, 1]])
   >>> A
   array([[ 5,  1, -1],
          [-1,  2,  4],
          [ 1,  1,  1]])
   >>> b = np.array([[0], [-2], [4]])
   >>> b
   array([[ 0],
          [-2],
          [ 4]])

   ```

   Once we have these NumPy objects we can solve our equation using the
   `.linalg.solve` command:

   ```python
   >>> np.linalg.solve(A, b)
   array([[-14.],
          [ 44.],
          [-26.]])

   ```

   **Experiment with another linear system.**

2. **Tickable** Manipulating matrices.

   It is possible to add two matrices together, this corresponds to adding each
   corresponding element:

   ```python
   >>> B = np.array([[1, 2, 0], [-4, 2, 2], [1, 3, 1]])
   >>> A + B
   array([[ 6,  3, -1],
          [-5,  4,  6],
          [ 2,  4,  2]])

   ```

   Similarly we can carry out scalar multiplication of matrices:

   ```python
   >>> 5 * A
   array([[25,  5, -5],
          [-5, 10, 20],
          [ 5,  5,  5]])

   ```

   Finally we can also carry out [matrix
   multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication):

   ```python
   >>> np.matmul(A, B)
   array([[ 0,  9,  1],
          [-5, 14,  8],
          [-2,  7,  3]])

   ```

   which in turn implies we can take the power of a matrix. Here is
   \\(A ^ 3 = AAA\\):

   ```python
   >>> np.linalg.matrix_power(A, 3)
   array([[107,  33,  -1],
          [ -9,  24,  44],
          [ 25,  17,  15]])

   ```

   **Modify the code here to try multiplying different matrices together.**

3. **Tickable** As we have matrix multiplication, that implies that there will
   be an element that does not have any effect when multiplying by it. (In normal
   multiplication this is the number \\(1\\) as \\(1 \times 5 = 5\\).

   This is referred to as the identity matrix and corresponds to a diagonal of
   \\(1\\)s. Here, for example is the identity matrix of size 3:

   $$
   I_3 = \begin{pmatrix}
   1 & 0 & 0\\
   0 & 1 & 0\\
   0 & 0 & 1
   \end{pmatrix}$$

   Here is the same matrix in python:

   ```python
   >>> I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
   >>> I
   array([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]])
   >>> np.matmul(I, A) == A  # We see that all elements are equal
   array([[ True,  True,  True],
          [ True,  True,  True],
          [ True,  True,  True]], dtype=bool)
   >>> np.array_equal(np.matmul(I, A), A)  # We see that the arrays are equal
   True

   ```

   As an inverse matrix of a given size is often used Numpy has a shorthand to
   get one:

   ```python
   >>> I = np.identity(3)
   >>> I
   array([[ 1.,  0.,  0.],
          [ 0.,  1.,  0.],
          [ 0.,  0.,  1.]])

   ```

   **Experiment with the above with different matrices.**

4. **Tickable** Related to the idea of the identity matrix is the notion of the
   inverse of a matrix \\(A^{-1}\\) so that:

   $$AA^{-1}=I$$

   Here is how we compute the matrix inverse in Python:

   ```python
   >>> Ainv = np.linalg.inv(A)
   >>> Ainv
   array([[ 1. ,  1. , -3. ],
          [-2.5, -3. ,  9.5],
          [ 1.5,  2. , -5.5]])

   ```

   We see that multiplying this inverse with the original matrix gives the
   identity matrix:

   ```python
   >>> np.matmul(np.linalg.inv(A), A)
   array([[  1.0...

   ```

   **Solving systems of linear equations corresponds to inverting a matrix:**

   $$Ax=b \Leftrightarrow A^{-1}Ax=A^{-1}b \Leftrightarrow x = A^{-1}b$$

   This can be checked here:

   ```python
   >>> np.matmul(Ainv, b)  # We obtain the same solution as before
   array([[-14.],
          [ 44.],
          [-26.]])

   ```

   **Experiment with the above.**

5. **Tickable** Related to the inverse of a matrix (it is used for its
   calculation) is called the
   [determinant](https://en.wikipedia.org/wiki/Determinant). We won't go in to
   detail about that here but this is how it is calculated:

   ```python
   >>> np.linalg.det(A)
   -2.0...

   ```

   **For the various matrices you have experimented with, calculate the
   determinant.**

6. **Worked example**: Large linear system.

   Let us consider the following hypothetical problem. A set of \\(N\\) business
   people who agree **together** to invest in a company. The first business
   person and the second business person agree to contribute a combined £1, the
   second and the third a combined £2, the third and the fourth a combined £3,
   and so on and so on until the \\(N-1\\)th and the \\(N\\)th a combined
   £\\(N-1\\).  Finally, the \\(N\\)th and the first business person contribute
   a combined £\\(N\\).

   Assume that \\(N=5\\), how much will each person contribute to the deal, and
   subsequently what is the total amount?

   If we let \\(x_i\\) represent the amount contributed by business person
   \\(i\\), then the above corresponds to:

   $$
   \begin{align}
   x_1 + x_2 &= 1\\
   x_2 + x_3 &= 2\\
   x_3 + x_4 &= 3\\
   \dots&\\
   x_{N-1} + x_{N} &= N-1\\
   x_{N} + x_{1} &= N\\
   \end{align}
   $$

   Let us build the matrix that corresponds to this linear system. First the
   coefficients of the equations:

   ```python
   >>> N = 5
   >>> A = np.array([[0 for col in range(N)] for row in range(N)])  # A 2d list of 0
   >>> for deal in range(N):  # Putting the 1s in the right position
   ...     A[deal][deal] = 1
   ...     A[deal][(deal + 1) % N] = 1
   >>> A
   array([[1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 1, 1],
          [1, 0, 0, 0, 1]])

   ```

   Now for the right hand side:

   ```python
   >>> b = np.array([[i + 1] for i in range(N)])
   >>> b
   array([[1],
          [2],
          [3],
          [4],
          [5]])

   ```

   We can now easily find out the contributions from each business person:

   ```python
   >>> contributions = np.linalg.solve(A, b)
   >>> contributions
   array([[ 1.5],
          [-0.5],
          [ 2.5],
          [ 0.5],
          [ 3.5]])
   >>> sum(contributions)  # Total contributions
   array([ 7.5])

   ```

   We see that the total contribution is £7.5, but that the second contributor
   actually gains money from the deal! (A negative contribution.)

   **Further work**

   These questions aim to push a bit further.

7. Consider a similar situation to that described in question 6 except that
   business person \\(i\\) and **half** of the contribution of business person
   \\(i+1\\) always equal to £5.

   (For the last pairing we have that the contribution of business person
   \\(N\\) and half of that of business person \\(0\\) is £5.

   What is the contribution of each player and what is the total contribution
   for \\(N=50\\)?

8. **Tickable** Modify the problem of question 7 with the assumption that the
   contributions are now made by triplets of players so that:
   business person \\(i\\) and **half** of the contribution of business person
   \\(i+1\\), and **a third** of the contributions of business person \\(i+2\\)
   is always equal to £5.

9. Further aspects of linear algebra are called eigenvalues and eigenvectors.
   Read about them and see how to compute them in numpy.

10. Scipy (another package) and Sympy can also be used for linear algebra.
    Explore those libraries and compare them to numpy.

# Further resources

- [NumPy docs for linear
  algebra](http://docs.scipy.org/doc/numpy/reference/routines.linalg.html)
- [A short
  tutorial](http://www.bogotobogo.com/python/python_numpy_matrix_tutorial.php)
- [A video about linear algebra with
  NumPy](https://www.youtube.com/watch?v=AqIrdW2-K6k)
- [Another course site](http://www.u.arizona.edu/~erdmann/mse350/topics/basic_linear_algebra.html)
