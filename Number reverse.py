

# Number Reverse
import re

str1 = '50 40 10 ab'
res = re.findall(r'\w+', str1)
print(res)
k=len(res)
print('k= ', k)
p = k*[0]
print('k= ', p)

for i,j in enumerate(res):
    #print(i,j,p)
    p[i] = res[k-1-i]
print(' '.join(p))

