
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

def music_tracks(dbConn):
    print("Select an option: ")
    print("  1. Print the top 10 most expensive tracks")
    print("  2. Print the average track duration")
    print("  3. Print the amount of tracks in each genre")
    cmd = input("Your choice --> ")
    print()

    most_expensive = objecttier.top_10_expensive(dbConn)
    average_duration = objecttier.average_track_duration(dbConn)
    tracks_by_genres = objecttier.tracks_by_genre(dbConn)

    if(cmd == '1'):
        print("Top 10 Most Expensive Tracks:")
        for tr in most_expensive:
            print(f"{tr.Name} - ${tr.UnitPrice}")
    elif(cmd == '2'):
        print(f"Average Track Duration (in seconds): {average_duration}")
    elif(cmd == '3'):
        print("Amount of Tracks in Each Genre:")
        for genre, count in tracks_by_genres:
            print(f"{genre.Name} (ID: {genre.GenreId} has {count} tracks)")
    else:
        print("Unknown input. Try again.")
        menu_selection(dbConn)



def albums_artists(dbConn):
    print("Select an option: ")
    print("  1. Print albums by artist")
    print("  2. Print most prolific artists")
    cmd = input("Your choice --> ")
    print()

    prolific_artists = objecttier.most_prolific_artists(dbConn)
    albums_by_artist = objecttier.albums_by_artist(dbConn)

    if(cmd == '1'):
        print("Albums by Artist:")
        for album, artist in albums_by_artist:
            print(f"{album.Title} - {artist}")
    elif(cmd == '2'):
        print("Most Prolific Artists:")
        for artist, count in prolific_artists:
            print(f"{artist.Name} - {count} albums")
    else:
        print("Unknown input. Try again.")
        menu_selection(dbConn)

def sales_revenue(dbConn):
    print("Select an option: ")
    print("  1. Print total revenue by country")
    print("  2. Print top 10 highest spending customers")
    print("  3. Print monthly sales trends")
    cmd = input("Your choice --> ")
    print()


    if(cmd == '1'):
        print("Total Revenue By Country:")
    elif(cmd == '2'):
        print("Top 10 Highest Spending Customers:")
    elif(cmd == '3'):
        print("Monthly Sales Trends:")
    else:
        print("Unknown input. Try again.")
        menu_selection(dbConn)

def playlists_usage(dbConn):
    print("Select an option: ")
    print("  1. Print playlist track counts")
    print("  2. Print most common media types")
    cmd = input("Your choice --> ")
    print()


    if(cmd == '1'):
        print("Number of Trakcs per Playlist:")
    elif(cmd == '2'):
        print("Most Common Media Types:")
    else:
        print("Unknown input. Try again.")
        menu_selection(dbConn)




def menu_selection(dbConn):
    print()
    print("Select a menu option: ")
    print("  1. Print general statistics about the database")
    print("  2. Print information about music and tracks")
    print("  3. Print information about albums and artists")
    print("  4. Print information about sales and revenue")
    print("  5. Print information about playlists and usage")
    print("or x to exit the program.")
    cmd = input("Your choice --> ")
    print()

    if(cmd == '1'):
        print_stats(dbConn)
    elif(cmd == '2'):
        music_tracks(dbConn)
    elif(cmd == '3'):
        albums_artists(dbConn)
    elif(cmd == '4'):
        sales_revenue(dbConn)
    elif(cmd == '5'):
        playlists_usage(dbConn)
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