import matplotlib.pyplot as plt
import numpy as np

import statistics as st

x = (1, 5, 10, 12, 13, 20)
y = (-3, -14, -31, -6, -40, -70)
slope, intercept = st.linear_regression(x, y)

x_range = np.array((np.min(x), np.max(x)))
relationship_image = slope * x_range + intercept

plt.figure()
plt.scatter(x=x, y=y)
plt.plot(x_range, relationship_image, color="black")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title(f"Data with fitted line: $y={slope:.2f}x+{intercept:.2f}$")
plt.savefig("main.pdf")
