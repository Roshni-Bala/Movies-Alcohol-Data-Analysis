#!/usr/bin/env python
# coding: utf-8

# # Do Tamil Movies have an impact on the alcoholism and substance usage in Tamil Nadu?

# ### Functions for web scraping from IMDB using URLs

# In[54]:


import requests
from bs4 import BeautifulSoup
import re
import string
import numpy as np

def url_alc_imdb(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find('section', id = "advisory-alcohol")]
    req = text[3]
    req = re.sub('\[.*?\]', '', req)
    req = re.sub('[%s]' % re.escape(string.punctuation), '', req)
    req = re.sub('\s+', ' ', req)
    alc_cont = ''
    alc_cont = req.split(' ').pop(1)
    if(alc_cont == 'Be'):
        alc_cont = 'Unrated'
    
    #print(alc_cont)
    return alc_cont
    #return text

def unique(url):
    seen = set()
    seen_add = seen.add
    return [x for x in url if not (x in seen or seen_add(x))]

#unique(all_movie_links)

def get_URL_list(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    text = [link.get('href') for link in soup.find_all('a', 
                          attrs={'href': re.compile("^\/title\/[t]{2}[0-9]{4,10}\/$")})]
    preURL = 'https://www.imdb.com'
    postURL = 'parentalguide'
    url_list = []
    i=0
    for x in text:
        x = preURL + x + postURL
        url_list.append(x)
    #url_list = list(set(url_list))
    url_list = unique(url_list)
    print(url_list)
    return url_list


        
def get_movie_title_list(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')  
    title_list = [link.text for link in soup.find_all('a', attrs={'href': re.compile("^\/title")})]
    
    for x in title_list:
        if(x==' \n'):
            title_list.remove(' \n')
    for x in title_list:      
        if(x=='See full summary'):
            title_list.remove('See full summary')
    print(title_list)
        
            
    #print(text)
    return title_list

#URL OF TOP TAMIL MOVIES LIST
movie_list_2015_url = 'https://www.imdb.com/list/ls031392332/'
movie_list_2016_url = 'https://www.imdb.com/list/ls064266039/'
movie_list_2017_url = 'https://www.imdb.com/list/ls069242710/'
movie_list_2018_url = 'https://www.imdb.com/list/ls045861940/'
movie_list_2019_url = 'https://www.imdb.com/list/ls041663030/'
movie_list_2020_url = 'https://www.imdb.com/list/ls097124558/'
movie_list_2021_url = 'https://www.imdb.com/list/ls084663427/'

#movie_urls_list = ['https://www.imdb.com/list/ls031392332/', 'https://www.imdb.com/list/ls064266039/','https://www.imdb.com/list/ls069242710/', 'https://www.imdb.com/list/ls045861940/','https://www.imdb.com/list/ls041663030/', 'https://www.imdb.com/list/ls097124558/','https://www.imdb.com/list/ls084663427/']

# movie_titles = []
# movie_urls = []
# movie_urls = [get_URL_list(u) for u in movie_urls]
# movie_titles = [get_movie_title_list(u) for u in movie_urls]


# ### Top Tamil Movies list for each year from IMDB

# In[39]:


#GETTING EACH YEARS DETAILS IN THE FORM OF A LIST
print("**2015 MOVIES**")
u1 = get_URL_list(movie_list_2015_url)
t1 = get_movie_title_list(movie_list_2015_url)
#print(u1)
#print(t1)
print("**2016 MOVIES**")
u2 = get_URL_list(movie_list_2016_url)
t2 = get_movie_title_list(movie_list_2016_url)

print("**2017 MOVIES**")
u3 = get_URL_list(movie_list_2017_url)
t3 = get_movie_title_list(movie_list_2017_url)

print("**2018 MOVIES**")
u4 = get_URL_list(movie_list_2018_url)
t4 = get_movie_title_list(movie_list_2018_url)

print("**2019 MOVIES**")
u5 = get_URL_list(movie_list_2019_url)
t5 = get_movie_title_list(movie_list_2019_url)

print("**2020 MOVIES**")
u6 = get_URL_list(movie_list_2020_url)
t6 = get_movie_title_list(movie_list_2020_url)

print("**2021 MOVIES**")
u7 = get_URL_list(movie_list_2021_url)
t7 = get_movie_title_list(movie_list_2021_url)


# ### Concatenating the lists of URLs and Movie Titles

# In[40]:


all_movie_titles = []
all_movie_links = []
all_movie_titles = t1 + t2 + t3 + t4 + t5 + t6 + t7
all_movie_links = u1 + u2 + u3 + u4 + u5 + u6 + u7
# all_movie_titles.remove('Server Sundaram')
# all_movie_links.remove('https://www.imdb.com/title/tt7087984/parentalguide')
print(all_movie_titles)
print(all_movie_links)


# ### Finding the alcohol content display severity by calling the url_alc_imdb(url) function

# In[41]:


alc_content_movie = []
for x in all_movie_links:
    alc_content_movie.append(url_alc_imdb(x))
print(alc_content_movie)


# ### Creating dataframes and saving to CSV file locally

# In[42]:


import pandas as pd


dict = {'Movie Name':all_movie_titles, 'IMDB Link':all_movie_links, 'Alcoholism Displayed':alc_content_movie}
df1 = pd.DataFrame({'Movie Name':all_movie_titles})
df2 = pd.DataFrame({'IMDB Link':all_movie_links})
df3 = pd.DataFrame({'Alcoholism Displayed':alc_content_movie})

df = [df1, df2, df3]

df_final = pd.concat(df, axis=1)
df_final.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv', index=False)


# In[45]:


(pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv'))
one = df_final[df_final['Alcoholism Displayed'] == 'Severe'].count()
two = df_final[df_final['Alcoholism Displayed'] == 'Moderate'].count()
three = df_final[df_final['Alcoholism Displayed'] == 'Mild'].count()
four = df_final[df_final['Alcoholism Displayed'] == 'Unrated'].count()
print(one)
print(two)
print(three)
print(four)


# ### Mapping each movie to the year of release

# In[46]:


from itertools import repeat
def mov_year(url, year):
    url_c = len(url)
    #print(url_c)
    movie_year = []
    movie_year.extend(repeat(year,url_c))
    return (movie_year)
movie_years_list = mov_year(u1, '2015') + mov_year(u2, '2016') + mov_year(u3, '2017')+ mov_year(u4, '2018') + mov_year(u5, '2019') + mov_year(u6, '2020') + mov_year(u7, '2021')
print(movie_years_list)


# ### Creating the final dataset after creating and cleaning

# In[47]:


import pandas as pd


dict = {'Movie Name':all_movie_titles, 'IMDB Link':all_movie_links, 'Alcoholism Displayed':alc_content_movie, 'Year of Release':movie_years_list}
df1 = pd.DataFrame({'Movie Name':all_movie_titles})
df2 = pd.DataFrame({'IMDB Link':all_movie_links})
df3 = pd.DataFrame({'Alcoholism Displayed':alc_content_movie})
df4 = pd.DataFrame({'Year of Release': movie_years_list})

df = [df1, df2, df3, df4]

df_final = pd.concat(df, axis=1)
df_final.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv', index=False)


# In[48]:


(pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv'))


# ### Webscrape the alcohol revenue in Tamil Nadu to find out how much is consumed<br><br>Fetched from wikipedia

# In[49]:


import requests
from bs4 import BeautifulSoup
import re
import string
import numpy as np
import pandas as pd
url = 'https://en.wikipedia.org/wiki/TASMAC'
page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")

def getTable(url):
    rows = []
    for child in soup.find_all('tbody')[1].children:
        row = []
        for td in child:
            try:
                row.append(td.text.replace('\n', ''))
            except:
                continue
        if len(row) > 0:
            rows.append(row)

    df = pd.DataFrame(rows[1:], columns=rows[0])
    df.to_csv(r'alc_tn', index=False)
    print('saved')
    return df

getTable(url)


# ### Appending the data to CSV
# 

# In[72]:


#manually inserting 2019-2020 and 2020-2021 from
#https://www.business-standard.com/article/economy-policy/tamil-nadu-earned-rs-33-811-crore-revenue-from-liquor-sales-121090700965_1.html
new_data = {
    'Fiscal Year': ['2019–20', '2020–21'],
    'Revenue in Crores (₹)	': ['33,811.14','33,133.24'],
    '% Change': ['8.51%', '−2.00%']
}
df = pd.DataFrame(new_data)
df.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn.csv', mode='a', index=False, header=False)
print("Data appended successfully.")


# ### Data Cleaning

# In[14]:


df = pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn.csv')
def year_modify(x):
    x = x.split('–',1)
    x = x.pop(0)
    y = int(x)
    y = y+1
    print(y)
    return y

df['Fiscal Year'] = df['Fiscal Year'].apply(year_modify)


# In[15]:


df.head()
df.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn_dataset.csv')
pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn_dataset.csv')


# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

g1 = pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv')
g2 = pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn_dataset.csv')
print('New dataframes created')


# In[17]:


#only require 2015 onwards for alcohol data
#new dataframe with 2015-2021 alchol data
g2 = g2.iloc[12:]
print(g2)
#remove unrated movies
g1 = (g1[g1['Alcoholism Displayed'] != 'Unrated'])
g1.head()


# ### Creating values for each severity value<br><u>List:</u><ol><li>Severe: 3</li><li>Moderate: 2</li><li>Mild: 1</li><li>None: 0</li></ol>

# In[18]:


alc_score = []
for x in g1['Alcoholism Displayed']:
    if(x == 'None'):
        alc_score.append(0)
    elif(x == 'Mild'):
        alc_score.append(1)
    elif(x == 'Moderate'):
        alc_score.append(2)
    elif(x== 'Severe'):
        alc_score.append(3)
    else:
        alc_score.append(0)
        
print(alc_score)
g1['Alcohol_Rating']=alc_score
(g1.head())


# # VISUALIZATIONS
# 

# In[19]:


plt.figure(figsize=[9,9])
g1['Alcoholism Displayed'].value_counts().plot.pie()
plt.title("2015-2021 ALCOHOL AND SUBSTANCES DISPLAYED ON MOVIES")
plt.ylabel('')
plt.show()


# In[20]:


g1_mean = g1.groupby(['Year of Release']).mean()
print(g1_mean)


# In[21]:


plt.figure(figsize=[10,3])
#g1_mean['Alcohol_Rating'].value_counts().plot.barh()
plt.bar(g1_mean.index,g1_mean['Alcohol_Rating'])
plt.xlabel('Year of Release')
plt.ylabel('Severity')
plt.title("Display of Alc and Substances over the Years")
plt.show()


# In[22]:


#Converting the data type of Revenue to float
g2 = g2.replace(',','', regex=True)
g2['Revenue in Crores'] = g2['Revenue in Crores'].astype(float)
print(g2.head())
g2.dtypes


# In[23]:


plt.figure(figsize=[10,5])
plt.plot(g2['Fiscal Year'], g2['Revenue in Crores'])
plt.xlabel('Year')
plt.ylabel('Revenue in Rupees (Crores)')
plt.title('Revenue collected in Tamil Nadu for Alcohol from 2015-2021')
plt.show()


# In[24]:


plt.figure(figsize=[10,5])
plt.plot(g1_mean.index, g1_mean['Alcohol_Rating'])
plt.xlabel('Year')
plt.ylabel('Alcohol_Rating')
plt.title('Substances displayed in Top Tamil Movies from 2015-2021: Line Graph')
plt.show()

# plt.figure(figsize=[10,3])
# #g1_mean['Alcohol_Rating'].value_counts().plot.barh()
# plt.bar(g1_mean.index,g1_mean['Alcohol_Rating'])
# plt.xlabel('Year of Release')
# plt.ylabel('Severity')
# plt.title("Display of Alc and Substances over the Years")
# plt.show()


# ### Creating a new data frame to join the data with common year values

# In[25]:


new_df_year = g1_mean


# In[26]:


rev_year = []
rev_mon = []
for x in g2['Fiscal Year']:
    rev_year.append(x)
for x in g2['Revenue in Crores']:
    rev_mon.append(x)
new_df_year['Year'] = rev_year
new_df_year['Revenue'] = rev_mon
print(new_df_year)
g1['Alcohol_Rating']=alc_score


# In[30]:


plt.rcParams["figure.figsize"] = (12,4)
ax = new_df_year.plot(kind = 'line', x = 'Year',y = 'Alcohol_Rating', color = 'Blue',linewidth = 2)
 
ax2 = new_df_year.plot(kind = 'line', x = 'Year',y = 'Revenue', secondary_y = True, color = 'Red',  linewidth = 2,ax = ax)


plt.title("Comparison")
ax.set_xlabel('Year')
ax.set_ylabel('Movies Displaying Alcohol and Substances', color = "b")
ax2.set_ylabel('Alcohol Consumed - Revenue (Rs)', color = 'r')
 
plt.savefig("result1.jpg")
plt.show()


# 
# ## <br><span style="color:green"><b>RESULT:</b><br>We can conclude that in the past ten year when the top Tamil movies have a surge in displaying alcohol and substances content, the purchasing of alcohol (in turn the consumption) is reduced.<br><br>We notice this in 2016 when there is an all time low in revenue of alcohol and an all time high in displaying alcohol in Tamil movies. Similarly, we note the opposite effect in 2020. </span>
# 
# ## <b>NOTE:</b><br>There are several factors to be considered such as laws, economy, tourism which have been ignored for the project. I have only scraped data for the alcohol revenue in Tamil Nadu and IMDB rating for Alcohol, Smoking and Substance abuse. 
# 
# ## This project has been created to understand <br> <ul><li>Web Scraping via BeautifulSoup</li><li>Pandas</li><li>Matplotlib</li></ul>

# In[ ]:




