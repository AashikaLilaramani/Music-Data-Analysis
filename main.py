import sqlite3
import presentationtier  # Import the presentation tier module to handle user interaction

def main():
    # Prompt the user for the database file name
    db_name = input("Enter the name of the SQLite database (e.g., 'music.db'): ")
    
    try:
        # Connect to the SQLite database
        dbConn = sqlite3.connect(db_name)
        print(f"Connected to the database: {db_name}")

        # Call the menu selection to start interacting with the music database
        presentationtier.menu_selection(dbConn)

    except sqlite3.Error as e:
        print(f"Error while connecting to the database: {e}")
        print("Make sure the database exists and try again.")

    finally:
        # Close the database connection when done
        if dbConn:
            dbConn.close()
            print("Connection closed.")

# Entry point to the program
if __name__ == "__main__":
    main()