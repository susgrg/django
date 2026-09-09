number = int(input("Enter a number betwwen 1 to 12:"))
if (number) >1 and (number) <=12:
    print(number)
    for n in range(13):
        print(f"{number}: {number} x {n} = {(number)*n}",end=" ") 
        print(" ")
else:
    number = int(input("Enter a valid number between 1 to 12:" ))
    #print("Not Valid")

