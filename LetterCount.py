

# LetterCount
#str1 = "Hello thisss issss an appple pie"
str1 = 'thiis is an apple'
import re
from collections import Counter

# split on white-space
word_list = re.split(r"\s+", str1)
s=[0]*len(word_list)
j=0
maxValue = 0
pos = 0
k = -1
for i in word_list:
    s = Counter(i)
    key = list(s)[:]
    value = list(s.values())[:]
    print(max(value))
    k+=1
    if max(value)>maxValue:
        maxValue = max(value)
        pos = k
print('pos and value: ',pos,maxValue)
if maxValue == 1:
    print(-1)
else:
    print(word_list[pos])

