The web application is developed using the python flask framework. Given its versatility and my familiarity with it, Python was my language of choice.

The flow of the application is as follows
1) The home page displays the prices of bitcoin and etherium from two sites namely blockchain.com and coingecko.com.
2) The home page also recommends the place to buy and sell.
3) These prices and recommendations are dynamic and the page also indicates when the prices were fetched via a timestamp.
4) The webpage is enabled with a refresh button to retrieve realtime results.
5) The homepage also hosts a navigation bar that allows navigation between the home page and about page.
6) The about page houses my contact information. Please use this to reach out.

Design choices for the backend
1) The helper.py is the crux of the application which retrieves the prices of both blockchain and ethereum.
2) It is important to note that blockchain.com provides an api to retrieve the prices and hence the api is consumed to fetch the data.
3) On the contrary, data has to be scraped from coingecko.com to achieve the same results and hence BeautifulSoup is used.
4) The main.py function calls the helper functions and creates response objects that can be sent to the frontend.
5) Please note for simplicity and brevity, two direct response objects are created one each for bitcoin and ethereum.
5) Code is commented inline to facilitate easy understanding.

Files and folder hierarchy
1) main.py - main python file that is to be run
2) helper.py - houses the helper functions to facilitate data retrieval
3) static - this folder houses the html templates and css files that are rendered
4) table_view.html - the home page
5) about_page.html - the about page

Questionnaire
1) Are there any sub-optimal choices( or short cuts taken due to limited time ) in your implementation?
	For the sake of simplicity and brevity, two direct response objects are created one each for bitcoin and ethereum. As the number of websites used for data retrieval increases, a more suitable data structure such as a json array can be chosen.

2) Is any part of it over-designed?
	I believe, no part of the application is over designed.

3) If you have to scale your solution to 100 users/second traffic what changes would you make, if any?
	In order to scale the solution to upwards of 100 users/second, I would use a messaging queue system. This handles the communication to clients and significantly reduces the load on the server. Apache Kafka is a popular choice and a reliable system for this use case. Kafka has better throughput, built-in partitioning, replication and inherent fault-tolerance, which makes it a good fit for intensive applications.

4) What are some other enhancements you would have made, if you had more time to do this implementation?
	Firstly, I would have looked to scrape a couple of more websites which makes the application more appealing. From my previous experience in large scale web scraping, I would have generated a dynamic web scraping system which understands the html structure of websites and scrape data automatically. Also, the trading prices are not considered to keep it simple, and this can impact the recommendation because sometimes the price might be low, but a higher trading price dictates different recommendations.


