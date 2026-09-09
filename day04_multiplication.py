number = input("Enter a number betwwen 1 to 12:")
if int(number) >1 and int(number) <=12:
    print(number)
    for n in range(13):
        print(f"{number}: {number} x {n} = {int(number)*n}",end=" ") 
        print(" ")
else:
    print("Not Valid")

