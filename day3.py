age = int(input("Age: "))

if age >= 18:
    print("You may enter.")
elif age <5:
    print("You are baby.")
elif age <10:
    print("You are kid.")
else:
    print("Sorry, 18+ only.")


age = 20
has_ticket = True

if age >=18 and has_ticket:
    print("Enjoy the show.")
elif age >=18 and not has_ticket:
    print("You need a ticket.")
else:
    print("Sorry, you may not enter.")
