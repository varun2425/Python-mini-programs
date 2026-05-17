secret = 7
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct Guess!")
        break
    else:
        attempts -= 1
        print("Correct Guess")
        
if attempts ==0:
    print("Game Over")