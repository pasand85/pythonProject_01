

# Consecutive
arr = [ 67,2,5,10,6,10,5,5]

from collections import Counter

s = Counter(arr)

key = list(s)[:]
value = list(s.values())[:]

i=0
max = 0
for i in range(len(value)):
    if value[i] > max:
        max = value[i]
        k = i
print(key[k],max)



