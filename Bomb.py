import time

stop = int(input("Time to detonate the explosive: "))
password = input("Password for the explosive: ")

for second in range (stop,0,-1):
    print(f"Bomb will detonate in {second} seconds...")
    time.sleep(1)

    guess = input("Enter the password to disable the explosive: ")
    if guess == password:
        print("Bomb has been disabled")
        break

else:
    print("Bomb has been detonated")