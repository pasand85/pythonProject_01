

# Palindrome two

strParam = 'Noel !sees - Leon'
str1 = ''.join(x for x in strParam if x.isalpha())
revStr = str1[::-1].lower()
print(revStr)
if str1.lower() == revStr:
  print(True)
else:
  print(False)