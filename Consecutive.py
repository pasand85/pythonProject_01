

# Consecutive
arr = [ 5,10,11,15]
#newArr = [0]*(max(arr)+1-min(arr))
#j=0
k=0
for i in range(min(arr),max(arr)+1):
#    newArr[j] = i
#    j+=1
    if i not in arr:
        k+=1

print(k)


'''
wholeArr = range(min(arr),max(arr),1)
newArr=[]
j=0
k=0
for i in wholeArr:
    newArr[j] = wholeArr[i]
    j+=1

    if i not in arr:
        k+=1

print(len(wholeArr)-k)
'''


