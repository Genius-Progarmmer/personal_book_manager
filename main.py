from books import asking_books, save_books_info, load_books_info

name = input("what is your name? ")
print("hi", name)

books = []
load_books = load_books_info()

asking_books(load_books)
save_books_info(load_books)