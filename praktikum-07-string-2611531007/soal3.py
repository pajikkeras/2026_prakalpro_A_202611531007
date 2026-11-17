# Name: Muhammad Rasya Fahrozi
# NIM: 2611531007
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text= "Muhammad Rasya Fahrozi"
count = 0
for char in text.lower():
    if char in ["a","i","u","e","o"]:
        count += 1
print("Vowels:", count)


