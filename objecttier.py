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