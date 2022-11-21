

# LetterCount
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

age = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

cardiac_cases = [5, 15, 20, 40, 55, 55, 70, 80, 90, 95]

survival_chances = [99, 99, 90, 90, 80, 75, 60, 50, 30, 25]

plt.plot(age,cardiac_cases,color='black', linewidth=2,
label="Cardiac Cases", marker='o',markerfacecolor='white',markeredgecolor= 'blue',
         markeredgewidth = 4 ,markersize=12)

plt.plot(age,survival_chances,color='black', linewidth=2,
label="Survival Chances",markeredgecolor= 'blue',marker='s',markerfacecolor='blue',markersize=11)

plt.xlabel('AGE',fontsize = 20)
plt.ylabel('Percentage',fontsize = 20)
plt.legend(fontsize = 14,loc='lower right', ncol=1)

plt.grid()



plt.show()
