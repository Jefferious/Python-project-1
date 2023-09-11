### Step 1 - Store data in a .txt


## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_new_book(book_source):
    title = input("What is the title of the book? ")
    author = input("What is the author's name? ")
    try:
        year = int(input("What year was this book published? "))
    except:
        year = int(input("Please type a number for the year. "))
    try:
        rating = float(input("What would you rate this book on a scale from 1-5? "))
    except:
        rating = float(input("Please enter a number from 1-5. "))
    try:
        pages = int(input("How many pages are in this book? "))
    except:
        pages = int(input("Enter a whole number dummy. "))
    
    with open(book_source, "a") as f:
        f.write(f'{title}, {author}, {year}, {rating}, {pages}\n')


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
# def view_all_books(book_source):

#     print("\nHere are all your books...\n")

#     with open(book_source, "r") as f:
#         file = f.readlines()

#         for line in file:
#             title, author, year, rating, pages = line.split(", ")

#             print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def view_all_books(book_source):
    book_list = []
    with open(book_source, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            book_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return book_list

def get_printed_book(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")

def view_all_books_in_list(book_source):
    print("\nHere are all of your books\n")
    for book in view_all_books(book_source):
        get_printed_book(book)

def get_lowest_book(book_source):
    list = view_all_books(book_source)
    return min(list, key=lambda x: int(x["rating"]))

def get_highest_book(book_source):
    list = view_all_books(book_source)
    return max(list, key=lambda x: int(x["rating"]))


def main_menu(book_source):
    active = True
    while active:
        user_input = input("""
Choose 1 to add a book.
Choose 2 to see all your books.
Choose 3 to see how many books you have.
Choose 4 to see lowest rated book.
Choose 5 to see highest rated book.                  
Choose 6 to see how many total pages there are.                          
Choose 0 to exit.                      
Type here: """).lower()
        if user_input == '1':
            create_new_book(book_source)
        elif user_input == '2':
            view_all_books_in_list(book_source)
        elif user_input == '3':
            print(f"\nYou have {len(view_all_books(book_source))} amount of books.\n")
        elif user_input == '4':
            print("\nThis is your lowest rated book\n")
            get_printed_book(get_lowest_book(book_source))
        elif user_input == '5':
            print("\nThis is your highest rated book\n")
            get_printed_book(get_highest_book(book_source))
        elif user_input == '6':
            print(f"\nAll of your books have {sum([x['pages'] for x in view_all_books(book_source)])} amount of pages.\n")
        elif user_input == '0':
            print("\nBye, come again soon")
            active = False
        else:
            return 'That was not one of the options dummy'
        

if __name__ == "__main__":
    main_menu("library.txt")