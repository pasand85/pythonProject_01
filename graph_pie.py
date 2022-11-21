

# 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

products = np.array([
    ["Apple", "Orange"],
    ["Beef", "Chicken"],
    ["Candy", "Chocolate"],
    ["Fish", "Bread"],
    ["Eggs", "Bacon"]])


randomProducts = np.random.randint(2, size = 5)
randomPerc = np.random.randint(10,25, size = 4)
print(randomPerc)


choice = []
counter = 0
for prod in products:
    choice.append(prod[randomProducts[counter]])
    counter+=1
    print(choice)


a = ['']*len(products)
b = ['']*(len(products)-1)

for j,i in enumerate(randomProducts):
    print(products[j][i])
    a[j] = products[j][i]

choice = []
counter = 0
for product in products:
    choice.append(product[randomProducts[counter]])
print(choice,a)


for i in range(len(products)-1):
    b[i] = randomPerc[i]
b.append(100 - np.sum(randomPerc))

print(b)
plt.pie(b, labels=choice)
plt.legend(loc = 'lower right', fontsize = 8, ncol = 1)
plt.show()
