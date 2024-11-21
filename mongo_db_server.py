from pymongo import MongoClient

# Connect to MongoDB server running on localhost
client = MongoClient("mongodb://127.0.0.1:27017/")

# Create or switch to the database
db = client['car']

# Create or switch to the collection
collection = db['temperatures']

# Insert a document into the collection
collection.insert_one({"data":234})

print("Document inserted successfully.")