from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Create connection to mongoDB
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
collection = db.mars_data

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # @TODO: YOUR CODE HERE!
    mars_rec = collection.find_one()
    return render_template("index.html", mars_data=mars_rec)
    # Return template and data
 
# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
 
    mars_data = {}
    mars_data = scrape_mars.scrape()

    # Insert records into the db
    collection.update({},mars_data,upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
