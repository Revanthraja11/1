n=str(input())
a=['a','e','i','o','u']
if n.isalpha() and n in a:
  print("Vowel")
elif n.isalpha() and n not in a:
  print("Consonant")
else:
  print("invalid")
