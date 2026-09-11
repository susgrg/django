# fruits = ["apple","strawberry","cherry"]
# fruits.append("orange")
# fruits.append("banana")
# fruits.insert(1,"blueberry")
# fruits.pop()  # it removes value of last
# fruits.remove("cherry")
# # fruits[0] = "kiwi" used to replace

# print(fruits[3])
# print(len(fruits))
# print(fruits[1:3])

# point = (1,2)
# # point [0] = 5 it is immutable and index cannot be changed
# x,y = point
# print(x,y)

book = {
    "title" : "Django classwork",
    "author" : "someone",
    "publishedAt" : 2026,
    20 : "gragse"
}

book["pages"] = 300
print(book["author"])

for key, value in book.items():
    print(f"{key}: {value}")

languages ={"English","Nepali","English"}
languages.add("chinese")
languages.add("Japanese")
print(languages)


a = [1,2,3]
b = a   #same list
b.append(4)
print(a) #[1,2,3,4]

c = a.copy()  #or list(a)