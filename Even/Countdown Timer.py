import time

seconds = int(input("Seconds: "))

while seconds:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time up!")