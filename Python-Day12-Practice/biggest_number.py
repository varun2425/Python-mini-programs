numbers = [10, 25, 7, 90, 45]

biggest =numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number

print("Numbers:", numbers)
print("Biggest number is:", biggest)