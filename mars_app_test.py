#from flask import Flask, render_template, redirect
import pymongo
import scrape_mars


# Create connection to mongoDB
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
collection = db.mars_data



#mars_data = {}
mars_data = scrape_mars.scrape()
print("In the test app")
print(mars_data)
print("Before inserting records")

#for  x in mars_data:
#    print(x)

# Insert records into the db

collection.update({},mars_data,upsert=True)


