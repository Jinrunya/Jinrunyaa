import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Sepal_Length = []
Sepal_Width = []
Petal_Length = []
Petal_Width = []

Sepal_Length = pd.read_csv("C:\\Users\\vip\\Desktop\\temp\\iris.csv", usecols=["Sepal_Length"])
Sepal_Length = np.array(Sepal_Length)

Sepal_Width = pd.read_csv("C:\\Users\\vip\\Desktop\\temp\\iris.csv", usecols=["Sepal_Width"])
Sepal_Width = np.array(Sepal_Width)

Petal_Length = pd.read_csv("C:\\Users\\vip\\Desktop\\temp\\iris.csv", usecols=["Petal_Length"])
Petal_Length = np.array(Petal_Length)

Petal_Width = pd.read_csv("C:\\Users\\vip\\Desktop\\temp\\iris.csv", usecols=["Petal_Width"])
Petal_Width = np.array(Petal_Width)

plt.figure(figsize=(20, 30), dpi=80)

plt.subplot(231)
plt.scatter(Sepal_Length, Sepal_Width, color='red', marker='*')
plt.xlabel("Sepal_Length")
plt.ylabel("Sepal_Width")
plt.title("Sepal_Length & Sepal_Width")
plt.legend()

plt.subplot(232)
plt.scatter(Sepal_Length, Petal_Length, color='orange', marker='*')
plt.xlabel("Sepal_Length")
plt.ylabel("Petal_Length")
plt.title("Sepal_Length & Petal_Length")
plt.legend()

plt.subplot(233)
plt.scatter(Sepal_Length, Petal_Length, color='yellow', marker='*')
plt.xlabel("Sepal_Length")
plt.ylabel("Petal_Width")
plt.title("Sepal_Length & Petal_Width")
plt.legend()

plt.subplot(234)
plt.scatter(Sepal_Width, Petal_Length, color='green', marker='*')
plt.xlabel("Sepal_Width")
plt.ylabel("Petal_Length")
plt.title("Sepal_Width & Petal_Length")
plt.legend()

plt.subplot(235)
plt.scatter(Sepal_Width, Petal_Width, color='blue', marker='*')
plt.xlabel("Sepal_Width")
plt.ylabel("Petal_Width")
plt.title("Sepal_Width & Petal_Width")
plt.legend()

plt.subplot(236)
plt.scatter(Petal_Length, Petal_Width, color='purple', marker='*')
plt.xlabel("Petal_Length")
plt.ylabel("Petal_Width")
plt.title("Petal_Length & Petal_Width")
plt.legend()

plt.show()
