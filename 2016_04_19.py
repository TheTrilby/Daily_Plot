import matplotlib.pyplot as plt

early = [0, 0.002747253, 0.005494505, 0.008241758, 0.01098901,
    0.01373626, 0.01648352, 0.01923077, # first week
    0.03846154, 0.05769231, 0.07692308, 0.09615385, 0.11538462, #first 6 weeks
    0.1666667, 0.2500000, 0.3333333, 0.4166667, 0.5000000, 0.5833333, 0.6666667,
    0.7500000, 0.8333333, 0.9166667, 1.0000000, # first year
    1.083333, 1.166667, 1.250000, 1.333333, 1.416667, 1.500000, 1.583333, 1.666667,
    1.750000, 1.833333, 1.916667, 2.000000, #second year
    2.25, 2.5, 2.75, 3,
    3.25, 3.5, 3.75, 4,
    4.25, 4.5, 4.75, 5,
    5.5, 6, 6.5, 7,
    8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

early_twenties = [21, 22, 23, 24]
mid_twenties = [24, 25, 26, 27]
late_twenties = [27, 28, 29, 30]
early_thirties = [30, 31, 32]

plt.xlabel('Age', fontsize=18)
plt.ylabel('Reported Age', fontsize=18)
plt.title('Age Reporting', fontsize=24)

plt.step(early, early, linewidth=1.0, color='b')
plt.step(early_twenties, early_twenties, linewidth=15.0, color='b')
plt.step(mid_twenties, mid_twenties, linewidth=30.0, color='b')
plt.step(late_twenties, late_twenties, linewidth=50.0, color='b')
plt.step(early_thirties, early_thirties, linewidth=75.0, color='b')


plt.savefig('2016_04_19.png')

