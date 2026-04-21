import matplotlib.pyplot as plt

data=[1,2,3,4,5,6]

plt.hist(data,bins=1,color='purple',label='Frequency')
plt.title('Histogram Example')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
