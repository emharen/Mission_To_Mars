

from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)


conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
db = client.Mars_db

collection=db.collection


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    inventory = list(db.collection.find())
    print(inventory)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", inventory=inventory)



@app.route("/scrape")
def scrape():
    db.collection.remove()
    db.collection.insert_many(
    [scrape_mars.scrape()])
     return redirect(url_for('/'))

if __name__ == "__main__":
    app.run(debug=True)

