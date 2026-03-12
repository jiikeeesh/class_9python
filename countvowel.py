a = input("Enter a string: ")
a = a.upper()
vowel = 0 
cons = 0
print(a)
# We use len(a) to create a range of numbers (0, 1, 2...)
for i in range(len(a)):
    if a[i] in "AEIOU":
        vowel += 1
    else:
        cons += 1
print("Number of vowels:", vowel)
print("Number of consonants:", cons)