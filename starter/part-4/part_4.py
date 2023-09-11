### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_new_book():
#     title = input("What is the title of the book? ")
#     author = input("What is the author's name? ")
#     year = (input("What year was this book published? "))
#     rating = (input("What would you rate this book on a scale from 1-5? "))
#     pages = (input("How many pages are in this book? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     return book_dictionary

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_new_book():
#     title = input("What is the title of the book? ")
#     author = input("What is the author's name? ")
#     year = int(input("What year was this book published? "))
#     rating = float(input("What would you rate this book on a scale from 1-5? "))
#     pages = int(input("How many pages are in this book? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     return book_dictionary
# bom = create_new_book()
# print(type(bom["year"]))


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def create_new_book():
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

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return book_dictionary
# bom = create_new_book()
# print(bom)


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
jeffs_fav_books = [{"title": "Name of the wind","author": "Patrick Rothfus","year": 2005,"rating": 4.0,"pages": 587}, {"title": "The Book of Mormon","author": "Mormon","year": 1830,"rating": 5.0,"pages": 531}, {"title": "Unsouled","author": "Will Wight","year": 2016,"rating": 5.0,"pages": 205}]

# def main_menu(book_list):
#     user_input = input('Type "add" to add a book. Type "check" to get a list of book titles: ').lower()
#     if user_input == 'add':
#         book_list.append(create_new_book())
#     elif user_input == 'check':
#         for book in book_list:
#             print (book['title'])
#     else:
#         return 'That was not one of the options dummy'
    
# main_menu(jeffs_fav_books)
       
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
def main_menu(book_list):
    user_input = input('Type "add" to add a book. Type "check" to get a list of book titles. To exit type "exit": ').lower()
    while user_input != 'exit':
        if user_input == 'add':
            book_list.append(create_new_book())
        elif user_input == 'check':
            for book in book_list:
                print (book['title'])
        else:
            return 'That was not one of the options dummy'
        user_input = input('Type "add" to add a book. Type "check" to get a list of book titles. To exit type "exit": ')
        
main_menu(jeffs_fav_books)
