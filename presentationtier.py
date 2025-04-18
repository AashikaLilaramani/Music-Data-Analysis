
#
# header comment!
#
import sqlite3
import objecttier



def print_stats(dbConn):

    num_albums = objecttier.num_albums(dbConn)
    num_uniqueArtists = objecttier.num_uniqueArtists(dbConn)
    print("General Statistics:")
    print(f" Number of Albums in Database: {num_albums:,}")
    print(f" Number of unique Artists in Database: {num_uniqueArtists:,}")
    menu_selection(dbConn)


def menu_selection(dbConn):
    print()
    print("Select a menu option: ")
    print("  1. Print general statistics about the database")
    print("or x to exit the program.")
    cmd = input("Your choice --> ")
    print()

    if(cmd == '1'):
        print_stats(dbConn)
    elif(cmd == 'x'):
        print("Exiting program.")
    else:
        print("Error, unknown command, try again...")
        print()
        menu_selection(dbConn)


def main():
    print("Personal Project: Music Analysis")
    print("Author: Aashika Lilaramani")
    print()
    print("This application allows you to analyze various")
    print("aspects of the chinook Music database.")
    print()
    dbName = input("Enter the name of the database you would like to use: ")
    dbConn = sqlite3.connect(dbName)
    print()
    print("Successfully connected to the database!")

    menu_selection(dbConn)

if __name__ == "__main__":
    main()