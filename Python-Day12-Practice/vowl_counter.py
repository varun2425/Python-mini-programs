text = input("Enter a word or sentence: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count = count + 1

print("Your text:", text)
print("Total vowels:", count)
