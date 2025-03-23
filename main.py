from pymongo import MongoClient

print("start")

# our mongodb is installed on this ubuntu server
client = MongoClient("mongodb://192.168.0.10:27017/")

# we have a database called bookstore
db = client.bookstore

# we have a collection called books
books = db.books

# use list to prevent pymongo.cursor.Cursor object at 0x0000027C2409FA10
array = list(books.find())
print(array)

print("end")

