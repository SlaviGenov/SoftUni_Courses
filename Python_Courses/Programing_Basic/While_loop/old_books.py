favorite_book = input()

checked_books = 0

while True:

    current_book = input()
    checked_books += 1

    if current_book == favorite_book:
        print(f"You checked {checked_books - 1} books and found it.")
        break

    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books - 1} books.")
        break