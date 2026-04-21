import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West"]
profits = [4500, 3500, 4000, 2800]
plt.pie(profits, labels=regions, autopct="%1.1f%%")
plt.title("Profit Distribution by Region")
plt.show()
