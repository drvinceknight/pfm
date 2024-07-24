import matplotlib.pyplot as plt
import numpy as np

import math
import statistics as st

h_data = (
    76.0,
    72.0,
    71.0,
    74.0,
    71.0,
    69.0,
    68.0,
    68.0,
    66.0,
    64.0,
    65.0,
    63.0,
    63.0,
    62.0,
    65.0,
    63.0,
    65.0,
    64.0,
    64.0,
)
m_data = (
    5,
    5,
    21,
    30,
    42,
    20,
    20,
    35,
    80,
    120,
    140,
    180,
    205,
    225,
    237,
    280,
    300,
    356,
    360,
)

x = [math.log(value) for value in m_data]
y = [math.log(value) for value in h_data]

slope, intercept = st.linear_regression(x, y)

m_range = np.linspace(np.min(m_data), np.max(m_data), 100)
relationship_image = np.exp(intercept) * m_range ** (slope)

plt.figure()
plt.scatter(x=m_data, y=h_data)
plt.plot(m_range, relationship_image, color="black")
plt.xlabel("Minutes of exercise: $m$")
plt.ylabel("Resting heart rate: $h$")
plt.title(f"Data collected by Anne with fitted relationship: $h={np.exp(intercept):.2f}m^{{{slope:.2f}}}$");
plt.savefig("main.pdf")
