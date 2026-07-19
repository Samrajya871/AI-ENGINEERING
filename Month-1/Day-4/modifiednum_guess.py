secret=7
for i in range(5):
    guess=int(input("Guess: "))
    if guess==secret:
        print(f"Guessed in {i+1} attempts")
    elif guess<secret:
        print("too low")
    else:
        print("too high")
