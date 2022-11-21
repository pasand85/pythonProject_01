'''Have the function HappyNumbers(num) determine if a number is Happy, ' \
'which is a number whose sum of the square of the digits eventually converges to 1. ' \
'Return true if it s a Happy number, otherwise return false.
For example: the number 10 is Happy because 1^2 + 0^2 converges to 1.'''

# Happy Numbers


num = 100
str1 = str(num)
k = len(str1)
p = k*[0]
for i in range(k):
    p[i] = int(str1[i])**2
if sum(p) == 1:
    print('Happy')
else:
    print('Not happy')





