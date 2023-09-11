import random
my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def dictionary_info(book_dictionary):
    book_info = f'{book_dictionary} is a nice book!'
    return book_info

print(dictionary_info(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_title(book_dictionary):
    book_title = f'The title of the book is {book_dictionary["title"]}.'
    return book_title


def book_author(book_dictionary):
    book_author = f'The author of the book is {book_dictionary["author"]}.'
    return book_author


def book_year(book_dictionary):
    book_year = f'The book was publicated in {book_dictionary["year"]}.'
    return book_year


def book_rating(book_dictionary):
    book_rating = f'The average rating of the book is {book_dictionary["rating"]}.'
    return book_rating


def book_length(book_dictionary):
    book_length = f'The book has {book_dictionary["pages"]} pages.'
    return book_length
print(book_length(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def random_book(book_list):
    ran_num = random.randint(0, len(book_list))
    ran_book = f'Here is a random book for you! {book_list[ran_num]["title"]}'
    return ran_book

def avg_page(book_list):
    num_books = len(book_list)
    total_pages = 0
    for book in book_list:
        total_pages += book['pages']
    avg_pages = total_pages / num_books
    return avg_pages

def avg_rating(book_list):
    num_books = len(book_list)
    total_rating = 0
    for book in book_list:
        total_rating += book['pages']
    avg_pages = total_rating / num_books
    return avg_rating