# Sides
# Pawelski
# 10/1/2024
# Programming Fundamentals

side = input("Do you want fries, onion rings, or cheese curds? >> ")
if side == "fries":
    print("Did you know they were invented in America?")
    ketchup = input("Do you need ketchup? (yes/no) >> ")
    if ketchup == "yes":
        print("K-up coming up!")
    else:
        print("Hold the tomato sauce!")
elif side == "onion rings":
    print("Tossing onion rings your way!")
    # Add your code here!
elif side == "cheese curds":
    print("You must be from Wisconsin!")
    # Add your code here!
else:
    print("No side for you!")
