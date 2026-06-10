score = 0

print("=== Python Quiz ===")

answer = input("1. What is the capital of India? ")

if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. Which keyword is used to create a function in Python? ")

if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. What is 5 + 5? ")

if answer == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"\nFinal Score: {score}/3")