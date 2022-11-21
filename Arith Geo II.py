

# Arith Geo II
arr = [3,6,12,24,48]

arithmVal = arr[1] - arr[0]
geomVal = arr[1] / arr[0]
testAr = [arr[0]] * len(arr)
testGe = [arr[0]] * len(arr)


for i in range(1,len(arr)):
    testAr[i] = arr[0] + i*arithmVal
    testGe[i] =  testGe[i-1]*geomVal

if testAr == arr:
    print('Ar')
elif testGe == arr:
    print('Geom')
else:
    print('-1')


print(arr,testAr, testGe, len(arr),i)

