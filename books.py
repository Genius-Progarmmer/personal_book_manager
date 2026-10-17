import json

def asking_books(books):

    count = int(input("how many books do you want to enter? "))

    for i in range(count):
        book = input("give a book name: ")
        books.append(book)

    print("your books are: ")

    for book in books:
        print(book)

def save_books_info(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=2)

def load_books_info():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 