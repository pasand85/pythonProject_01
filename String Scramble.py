

# String Scramble
str1 = 'adbcaaccbbdd'
str2 = 'abcdd'

all_freq1 = {}
all_freq2 = {}

for i in str1:
    if i in all_freq1:
        all_freq1[i] += 1
    else:
        all_freq1[i] = 1

for i in str2:
    if i in all_freq2:
        all_freq2[i] += 1
    else:
        all_freq2[i] = 1

k=0
for i in all_freq2:
    if i in all_freq1 and all_freq2[i]<=all_freq1[i]:
        pass
    else:
        k=1
        break

if k == 0:
    print('OKKkkK!')
else:
    print('nopeeee')
'''
k = 0
for i in str2.isalpha():
    if i in str1.isalpha():
        k += 1
if k == len(str2.isalpha()):
    print('OK')
else:
    print('Not OK')
'''
