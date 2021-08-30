# Scarping-theguardian
This is a demo project to crawl the guardian web site using scrapy library and deploy an application by Flask API, and store data on hosted mongoDB : mongoDB Atlas.

### Prerequisites
You must have installed:
- Scrapy.
- pymongo.
- dnspython.
- Flask (for API).

### Project Structure
This project has four major parts :
1. app.py - This contains Flask APIs that receives keyword through GUI or API calls, search by it and returns it.
2. templates - This folder contains the HTML template to allow user to enter the keyword and displays the articles.
3. theguardianCrawl - contains the spider to the website, theguardianSpider has the logic of the crawling.

### Running the project
1. Ensure that you are in the project home directory. Run app.py using below command to start Flask API

```
python app.py
```
By default, flask will run on port 5000.

2. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :
![HomeApplication](https://user-images.githubusercontent.com/61110435/131260695-e910ec06-bfe0-4aef-a6e6-96c2f106dab7.PNG)


3. Enter a **keyword to search**, you can also add **number of results (optional)**.

If everything goes well, you should  be able to see all the articles **sorted by date** contains the keyword on the HTML page!
![ResultsApplication](https://user-images.githubusercontent.com/61110435/131260757-a90f3288-9703-443f-be8d-257b6b588f6c.PNG)

4. To add new data go to the url below, wait for a while, you will be redirect to the home page after finishing. 

```
http://127.0.0.1:5000/insertData
```

5. To delete all the data go to the url below, you will be redirect to the home page after finishing.

```
http://127.0.0.1:5000/deleteAll
```
