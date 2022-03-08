import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
def show_menu():
    print("\n  -- Main Menu --")
     print("View Books\n View Store Locations\n My Account\n Exit Program")
def show_books:
    _cursor.execute("SELECT book_id, book_name, author, details from book")
 print("\n  -- DISPLAYING BOOK LISTING --")
def show_locations:
    execute("SELECT store_id, locale from store")
    print("\n  -- DISPLAYING STORE LOCATIONS --")
for location in locations:
        print("Locale:\n".format)
def validate_user():
  " validate the users ID "
def show_account_menu():
    " display the users account menu "
return account_option
    except ValueError:
        print("\nInvalid number, program terminated")
def show_wishlist:
execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist "
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id".format(_user_id)
    print("\nDISPLAYING WISHLIST ITEMS")
 for book from wishlist
        print("Book Name:Author")
def show_books_to_add(user_id):
query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id)".format(user_id))
print(query)
for book in books_to_add:
        print("Book Id:Name:format)

def add_book_to_wishlist:
    execute("INSERT INTO wishlist(user_id, book_id) VALUES)".format(_user_id, _book_id)) 
print("Welcome to the WhatABook Application! ")
user_selection = show_menu() 
    add_book_to_wishlist
db.commit
print("Book id was added to your wishlist!")

except mysql.connector.error: 
  if error== errorcode.ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
elif error == errorcode.BAD_ERROR:
        print("The specified database does not exist")

    db.close()
