name = input("what is your name? ")
print("hi", name)

count = int(input("how many books do you want to enter? "))

books = []


for i in range(count):
    book = input("give a book name: ")
    books.append(book)

print("your books are: ")

for book in books:
    print(book)