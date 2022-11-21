'''
Consonant Count
Have the function ConsonantCount(str) take the str string parameter being passed
and return the number of consonants the string contains.
'''

str1 = 'Hello World'
k=0
vowels = ['a','e','i','o','u',' ','A','E','I','O','U','*','-','!','?']
for i in str1:
    if i not in vowels:
        k += 1
print(k)