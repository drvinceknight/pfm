import matplotlib.pyplot as plt

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

plt.figure()
plt.scatter(x=m_data, y=h_data)
plt.xlabel("Minutes of exercise: $m$")
plt.ylabel("Resting heart rate: $h$")
plt.title("Data collected by Anne")
plt.savefig("main.pdf")
