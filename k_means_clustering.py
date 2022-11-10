import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data
y = iris.target

plt.scatter(x[:,1], x[:,3], color='white', marker='o', edgecolor='red', s=25)
plt.grid()
plt.tight_layout()
plt.show()