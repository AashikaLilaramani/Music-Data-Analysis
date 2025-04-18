#
# objecttier.py
# Builds Music-related objects from data retrieved through 
# the data tier.
import datatier

##################################################################
# Album class:
# Constructor(...)
# Properties:
# AlbumId: int, Title: string, ArtistId: int
# ALbum class definition (constructors & properties)
class Album:
   def __init__(self, Album_Id, Album_Title, Artist_Id):
      self._AlbumId = Album_Id
      self._Title = Album_Title
      self._ArtistId = Artist_Id
    
    # Properties
   @property
   def AlbumId(self):
      return self._AlbumId
   @property
   def Title(self):
      return self._Title
   @property
   def ArtistId(self):
      return self._ArtistId
##################################################################
# Artist Class
# Constructor(...)
# Properties:
# ArtistId: int, Name: string
# Artist class definition (constructors & properties)
class Artist:
   def __init__(self, Artist_Id, Artist_Name):
      self._ArtistId = Artist_Id
      self._Name = Artist_Name
   
   # Properties
   @property
   def ArtistId(self):
      return self._ArtistId
   @property
   def Name(self):
      return self._Name
##################################################################
# Customer Class
# Constructor(...)
# Properties:
# CustomerId: int, FirstName: string, LastName: string, Company: string, Address: string, City: string, State: string, Country: string, PostalCode: string, Phone: string, Fax: string, Email: string, SupportRepId: int
# Customer class definition (constructors & properties)
class Customer:
   def __init__(self, Customer_Id, First_Name, Last_Name, Cust_Company, Cust_Address, Cust_City, Cust_State, Cust_Country, Cust_PostalCode, Cust_Phone, Cust_Fax, Cust_Email, Support_RepId):
      self._CustomerId = Customer_Id
      self._FirstName = First_Name
      self._LastName = Last_Name
      self._Company = Cust_Company
      self._Address = Cust_Address
      self._City = Cust_City
      self._State = Cust_State
      self._Country = Cust_Country
      self._PostalCode = Cust_PostalCode
      self._Phone = Cust_Phone
      self._Fax = Cust_Fax
      self._Email = Cust_Email
      self._SupportRepId = Support_RepId
    
   @property
   def CustomerId(self):
      return self._CustomerId
   @property
   def FirstName(self):
      return self._FirstName
   @property
   def LastName(self):
      return self._LastName
   @property
   def Company(self):
      return self._Company
   @property
   def Address(self):
      return self._Address
   @property
   def City(self):
      return self._City
   @property
   def State(self):
      return self._State
   @property
   def Country(self):
      return self._Country
   @property
   def PostalCode(self):
      return self._PostalCode
   @property
   def Phone(self):
      return self._Phone
   @property
   def Fax(self):
      return self._Fax
   @property
   def Email(self):
      return self._Email
   @property
   def SupportRepId(self):
      return self._SupportRepId
   
##################################################################
# Employee Class
# Constructor(...)
# Properties:
# EmployeeId: int, LastName: string, FirstName: string, Title: string, ReportsTo: int, BirthDate: datetime, HireDate: datetime, Address: string, City: string, State: string, Country: string, PostalCode: string, Phone: string, Fax: string, Email: string
# Employee class definition (constructors & properties)
class Employee:
   def __init__(self, Employee_Id, Last_Name, First_Name, Emp_Title, Reports_To, Birth_Date, Hire_Date, Emp_Address, Emp_City, Emp_State, Emp_Country, Postal_Code, Emp_Phone, Emp_Fax, Emp_Email):
      self._EmployeeId = Employee_Id
      self._LastName = Last_Name
      self._FirstName = First_Name
      self._Title = Emp_Title
      self._ReportsTo = Reports_To
      self._BirthDate = Birth_Date
      self._HireDate = Hire_Date
      self._Address = Emp_Address
      self._City = Emp_City
      self._State = Emp_State
      self._Country = Emp_Country
      self._PostalCode = Postal_Code
      self._Phone = Emp_Phone
      self._Fax = Emp_Fax
      self._Email = Emp_Email
    
   @property
   def EmployeeId(self):
      return self._EmployeeId
   @property
   def LastName(self):
      return self._LastName
   @property
   def FirstName(self):
      return self._FirstName
   @property
   def Title(self):
      return self._Title
   @property
   def ReportsTo(self):
      return self._ReportsTo
   @property
   def Address(self):
      return self._Address
   @property
   def City(self):
      return self._City
   @property
   def State(self):
      return self._State
   @property
   def Country(self):
      return self._Country
   @property
   def PostalCode(self):
      return self._PostalCode
   @property
   def Phone(self):
      return self._Phone
   @property
   def Fax(self):
      return self._Fax
   @property
   def Email(self):
      return self._Email
##################################################################
# Genre Class
# Constructor(...)
# Properties:
# GenreId: int, Name: string
# Genre class definition (constructors & properties)
class Genre:
   def __init__(self, Genre_Id, Genre_Name):
      self._GenreId = Genre_Id
      self._Name = Genre_Name
   
   # Properties
   @property
   def GenreId(self):
      return self._GenreId
   @property
   def Name(self):
      return self._Name
##################################################################
# Invoice Items Class
# Constructor(...)
# Properties:
# InvoiceLineId: int, InvoiceId: int, TrackId: int, UnitPrice: int, Quantity: int
# Invoice_Items class definition (constructors & properties)
class Invoice_Items:
   def __init__(self, Inv_Line_Id, Inv_Id, Track_Id, Unit_Price, Inv_Quantity):
      self._InvoiceLineId = Inv_Line_Id
      self._InvoiceId = Inv_Id
      self._TrackId = Track_Id
      self._UnitPrice = Unit_Price
      self._Quantity = Inv_Quantity
   
   # Properties
   @property
   def InvoiceLineId(self):
      return self._InvoiceLineId
   @property
   def InvoiceId(self):
      return self._InvoiceId
   @property
   def TrackId(self):
      return self._TrackId
   @property
   def UnitPrice(self):
      return self._UnitPrice
   @property
   def Quantity(self):
      return self._Quantity
##################################################################
# Invoice Class
# Constructor(...)
# Properties:
# InvoiceId: int, CustomerId: int, InvoiceDate: datetime, BillingAddress: string, BillingState: string, BillingCountry: string, BillingPostalCode: string, Total: int
# Invoice class definition (constructors & properties)
class Invoice:
   def __init__(self, Inv_Id, Cust_Id, Inv_Date, Address, City, State, Country, PostalCode, Inv_Total):
      self._InvoiceId = Inv_Id
      self._CusomterId = Cust_Id
      self._InvoiceDate = Inv_Date
      self._BillingAddress = Address
      self._BillingCity = City
      self._BillingState = State
      self._BillingCountry = Country
      self._BillingPostalCode = PostalCode
      self._Total = Inv_Total
   
   # Properties
   @property
   def InvoiceId(self):
      return self._InvoiceId
   @property
   def CustomerId(self):
      return self._CusomterId
   @property
   def InvoiceDate(self):
      return self._InvoiceDate
   @property
   def BillingAddress(self):
      return self._BillingAddress
   @property
   def BillingCity(self):
      return self._BillingState
   @property
   def BillingState(self):
      return self._BillingState
   @property
   def BillingCountry(self):
      return self._BillingCountry
   @property
   def BillingPostalCode(self):
      return self._BillingPostalCode
   @property
   def Total(self):
      return self._Total
##################################################################
# Media Types Class
# Constructor(...)
# Properties:
# MediaTypeId: int, Name: int
# Media_Types class definition (constructors & properties)
class Media_Types:
   def __init__(self, Media_TypeId, Media_Name):
      self._MediaTypeId = Media_TypeId
      self._Name = Media_Name
   
   # Properties
   @property
   def MediaTypeId(self):
      return self._MediaTypeId
   @property
   def Name(self):
      return self._Name
##################################################################
# PLaylist Track Class
# Constructor(...)
# Properties:
# PlaylistId: int, TrackId, int
# Playlist_Track class definition (constructors & properties)
class Playlist_Track:
   def __init__(self, Playlist_Id, Track_Id):
      self._PlaylistId = Playlist_Id
      self._TrackId = Track_Id
   
   # Properties
   @property
   def PlaylistId(self):
      return self._PlaylistId
   @property
   def TrackId(self):
      return self._TrackId
##################################################################
# PLaylist Class
# Constructor(...)
# Properties:
# PlaylistId: int, Name: string
# Playlist class definition (constructors & properties)
class Playlist:
   def __init__(self, Playlist_Id, Playlist_Name):
      self._PlaylistId = Playlist_Id
      self._Name = Playlist_Name
   
   # Properties
   @property
   def PlaylistId(self):
      return self._PlaylistId
   @property
   def Name(self):
      return self._Name 
##################################################################
# Tracks Class
# Constructor(...)
# Properties:
# TrackId: int, Name: string, AlbumId: int, MediaTypeId: int, GenreId: int, Composer: string, Milliseconds: int, Bytes: int, UnitPrice: int
# Tracks class definition (constructors & properties)
class Tracks:
   def __init__(self, Track_Id, Track_Name, Album_Id, Media_TypeId, Genre_Id, Track_Composer, Milli_Seconds, Track_Bytes, Unit_Price):
      self._TrackId = Track_Id
      self._Name = Track_Name
      self._AlbumId = Album_Id
      self._MediaTypeId = Media_TypeId
      self._GenreId = Genre_Id
      self._Composer = Track_Composer
      self._Milliseconds = Milli_Seconds
      self._Bytes = Track_Bytes
      self._UnitPrice = Unit_Price
   
   # Properties
   @property
   def TrackId(self):
      return self._TrackId
   @property
   def Name(self):
      return self._Name
   @property
   def AlbumId(self):
      return self._AlbumId
   @property
   def MediaTypeId(self):
      return self._MediaTypeId
   @property
   def GenreId(self):
      return self._GenreId
   @property
   def Composer(self):
      return self._Composer
   @property
   def Milliseconds(self):
      return self._Milliseconds
   @property
   def Bytes(self):
      return self._Bytes
   @property
   def UnitPrice(self):
      return self._UnitPrice




##################################################################
# 
# num_albums:
# Returns the number of albums in the database, or -1 if an error occurs
def num_albums(dbConn):
   sql = f"SELECT COUNT(AlbumId) FROM albums"
   row = datatier.select_one_row(dbConn, sql)
   if row is None:
      return -1
   else:
      return row[0]
##################################################################
# 
# num_uniqueArtists:
# Returns the number of unique artists in the database, or -1 if an error occurs
def num_uniqueArtists(dbConn):
   sql = f"SELECT COUNT(DISTINCT ArtistId) FROM artists"
   row = datatier.select_one_row(dbConn, sql)
   if row is None:
      return -1
   else:
      return row[0]  
##################################################################
# 
# top_10_expensive:
# Returns the top 10 most expensive tracks
def top_10_expensive(dbConn):
   sql = f"SELECT TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice FROM Tracks ORDER BY UnitPrice DESC LIMIT 10"
   
   rows = datatier.select_n_rows(dbConn, sql)
   if rows is None:
      return []
   
   S = []
   for row in rows:
      tr = Tracks(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
      S.append(tr)
   
   return S
##################################################################
# 
# average_track_duration:
# Returns the average of all track durations as seconds
def average_track_duration(dbConn):
   sql = f"SELECT AVG(Milliseconds) / 1000 FROM Tracks"
   
   row = datatier.select_n_rows(dbConn, sql)
   if row is None:
      return -1
   else:
      return row[0]
##################################################################
# 
# tracks_by_genre:
# Returns the number of tracks in each genre
def tracks_by_genre(dbConn):
   sql = f"SELECT Genres.GenreId, Genres.Name, COUNT(Tracks.TrackId) FROM Genres JOIN Tracks ON Genres.GenreId = Tracks.GenreId GROUP BY Genres.GenreId ORDER BY COUNT(Tracks.TrackId) DESC"
   
   rows = datatier.select_n_rows(dbConn, sql)
   if rows is None:
      return []
   
   S = []
   for row in rows:
      tr = Genre(row[0], row[1])
      track_count = row[2]
      S.append((tr, track_count))
   
   return S
