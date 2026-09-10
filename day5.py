#def greet():
    #print("Hello")

#def greetUser(username):
   # print(f"Namaste : {username}")

#greetUser("Ram")
#greetUser("Hari")

#def sum(a,b):
   # return a+b

def calculateAvg(x,y,z):
    total = x+y+z
    avg = total/3
    return avg

myavg = calculateAvg(2,5,6)
print(myavg)

#total = sum(5,10)
#total2 = sum(11,99)
#print(total)
#print(total2)

def make_profile(name,age,city="Pokhara"):
    print(f"{name},is {age} from {city}")

make_profile("Mac", 22, "Pokhara")
make_profile("Ram",19, "Kathmandu")
make_profile("Hari", 19)

x = 10 #globally accesed is all x value in overall file

def foo():
    x = 5 #local varibale
    print(x)

foo()