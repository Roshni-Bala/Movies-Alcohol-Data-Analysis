# Movies, Alcohol and Crime in Tamil Nadu:<br> Data-Analysis Project

## Question:
Does consumption of alcohol and violence in Tamil Movies released in the past 5 years have an affect on the statistics of Tamil Nadu's population? 
## Processes:
1. Data collection
2. Data cleaning
3. Data analyzing 
4. Data visualizations
## Process Goals:
1. Collect data about top Tamil movies from IMDB (2015-2021)
2. Collect data about Alcohol from Wikipedia (2015-2021)
3. Collect data about Crime rates in Tamil Nadu (2015-2021)
4. Clean datasets
5. Join datasets using primary key as year
6. Form visualizations to understand effect

### Data collection process
1. Identify top tamil movie lists for each year
2. Webscrape individual hyperlinks from the movie lists webpage
3. Webscrape movie details from every hyperlink saved in dataframe
4. Indentify data source for Alcohol and crime details (Wikipedia)
5. Webscrape tables from source site

## Tools used:
1. Python(Jupyter Notebook)
2. Libraries: 
    a. Pandas
    b. BeautifulSoup
    c. Matplotlib

## Results :
![result4](https://user-images.githubusercontent.com/54448939/152679294-669ee6d0-7b99-445d-8d50-2ea54d4fd84a.jpg)
<br>
We see that the two fields being compared on the y-axis have rises and falls on the same years. Hence, we can say that with increase in violence displayed in movies, there are higher chances of people being influenced by it and committing violent crimes.
<br>
<br>
![result1](https://user-images.githubusercontent.com/54448939/152679289-6e09eb16-e2cd-4cd3-b8ef-e4d728fae245.jpg)
<br>
There is an inversely proportional effect being observed between alcohol consumption and display in movies. 
<br>
<br>
We can conclude that there could be a possibility of influence of the types of movies that are released in Tamil Nadu from real data like Alcohol consumption and crimes committed.

### NOTE:
There are several factors to be considered such as new state laws, economy, tourism, pandemic, unrated data which have been ignored for the project. I have only scraped data for the alcohol revenue in Tamil Nadu and IMDB rating for Alcohol, Smoking and Substance abuse. 

This project has been created only for personal understanding of the following <br> <ul><li>Web Scraping via BeautifulSoup</li><li>Pandas</li><li>Matplotlib</li></ul>
