import statistics as stat
import matplotlib.pyplot as plt

x = (0, 2, 2, 3, 4, 5.6)
y = (-1, -3, -4, -5, 4, -7)

slope, intercept = stat.linear_regression(x, y)

start_point, end_point = min(x), max(x)
image_start_point = slope * start_point + intercept
image_end_point = slope * end_point + intercept

plt.figure()
plt.scatter(x, y)
plt.plot((start_point, end_point), (image_start_point, image_end_point))
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("main.pdf")
