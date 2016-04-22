import matplotlib.pyplot as plt

plt.figure(figsize=(30,10))

early = [0, 0.25, 0.5, 0.75, 1,
    2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
preteen = [6, 7, 8, 9, 10, 11, 12, 13]
teen = [13, 14, 15, 16, 17, 18, 19, 20, 21]

early_twenties = [21, 22, 23, 24, 25]
mid_twenties = [25, 26, 27, 28]
late_twenties = [28, 29, 30]
early_thirties = [30, 31, 32]

plt.xlabel('Age', fontsize=18)
plt.ylabel('Reported Age', fontsize=18)
plt.title('Age Reporting', fontsize=24)

def plotter(ages, error):
    plt.step(ages, ages, color='b')
    plt.errorbar(ages, ages, xerr=0, yerr=error, fmt='o', color='black')

plotter(early, 0.25)
plotter(preteen, 0.5)
plotter(teen, 1)
plotter(early_twenties, 2)
plotter(mid_twenties, 4)
plotter(late_twenties, 8)
plotter(early_thirties, 10)

plt.savefig('2016_04_20.png')

