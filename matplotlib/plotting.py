import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 15, 5, 25, 5]
plt.bar(x, y)
plt.title("Sales Over Time")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

plt.savefig("saleChart.svg")
