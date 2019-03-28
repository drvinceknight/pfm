Post: Reactive discussion
=========================

Goals of session are to give an overview of a number of minor issues I am used
to seeing when students write LaTeX.

Ask students to pick a subject and we will write a "small paper" on this
subject.

Using the example, aim to write a report but showcase the following things in
LaTeX:

- Discuss referencing, specifically highlighting Mendeley and what it does.
- Discuss using columns::

    \usepackage{multicol}

    \begin{multicols}{2}

        \begin{align}
            p_n &= \left(1 - \frac{1}{n + 1}\right)\left(\frac{1}{n - 1}\right)\\
            p_n &= \left(\frac{n + 1 - 1}{n + 1}\right)\left(\frac{1}{n - 1}\right)\\
            p_n &= \frac{n}{(n + 1)(n - 1)}\\
            p_n &= \frac{n}{(n^2 - 1)}
        \end{align}

        \columnbreak

    Using Python to verify the algebra:

        \begin{minted}{python}
        import sympy as sym
        n = sym.symbols('n')
        p_n = (1 - 1 / (n + 1)) * (1 / (n - 1))
        p_n.simplify()
        \end{minted}

    \end{multicols}

- Discuss uploading figures from code to overleaf::

      import matplotlib.pyplot as plt
      plt.figure()
      plt.scatter(range(5), range(20))
      plt.savefig("plot.pdf")


  Then upload the picture to overleaf and include in document.

- Including tables in LaTeX:

  - Get some data and create a pandas dataframe.
  - Get pandas to convert that to LaTeX. Copy and paste but also show how to
    write to file and copy that in and use `\input`.

**REMIND STUDENTS ABOUT THE PLAN NEXT WEEK**
