from flask import Flask, jsonify, request, render_template
import pymongo
import json
import os

# URL of the API.
#in order to run it you need to add your IP in mongodb database
connection_url = 'mongodb+srv://eboujou:A-zerty123@cluster0.gdqdj.mongodb.net/gemography?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)

#get database
gemography = client.get_database('gemography')
#get the collection
theguardianTable = gemography['theguardian']

@app.route('/')
def index():
    #predict will contain the result of searching, at the 1ft time there is no result
    return render_template('index.html', predict=None)

@app.route('/insertData')
def insertData():
    #delete the previous crawl results file
    os.system('del articles.json')

    #Run a new crawling and store the data in json file
    os.system('scrapy crawl theguardian -o articles.json')

    #open file results and insert it in the collection
    with open('articles.json', encoding="utf8") as f:
        file_data = json.load(f)
    query = theguardianTable.insert_many(file_data)

    #come back to the home page
    return render_template('index.html', predict=None)

#this function help to remove all the data from the database
@app.route('/deleteAll')
def deleteAll():

    query = theguardianTable.remove()
    return render_template('index.html', predict=None)


@app.route('/findByKeyword', methods=['POST'])
def findByKeyword():
    #get the keyword and number of result to show
    keyword = request.form.get('keyword')
    limit = request.form.get('limit')

    #In order to search in the article, we gonna use regex
    query = {
        "article": {
            "$regex": str(keyword),
            "$options": 'i'
        }
    }

    #if the user provide number of results to show we use limit function
    res = theguardianTable.find(query).sort('date',pymongo.DESCENDING).limit(int(limit)) if limit else theguardianTable.find(query).sort('date',pymongo.DESCENDING)

    #store everything in a list to loop over it in the html file
    output = []
    for x in res:
        output.append(x)
    return render_template('index.html',predict=output)


if __name__ == '__main__':
    app.run(debug=True)