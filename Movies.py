import requests
from bs4 import BeautifulSoup
import re
import string
import numpy as np

def url_alc_imdb(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    text = [p.text for p in soup.find('section', id='advisory-alcohol')]
    req = text[3]
    req = re.sub('\[.*?\]', '', req)
    req = re.sub('[%s]' % re.escape(string.punctuation), '', req)
    req = re.sub('\s+', ' ', req)
    alc_cont = ''
    alc_cont = req.split(' ').pop(1)
    if alc_cont == 'Be':
        alc_cont = 'Unrated'
    return alc_cont
def unique(url):
    seen = set()
    seen_add = seen.add
    return [x for x in url if not (x in seen or seen_add(x))]
def get_URL_list(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    text = [link.get('href') for link in soup.find_all('a',
            attrs={'href': re.compile("^\/title\/[t]{2}[0-9]{4,10}\/$"
            )})]
    preURL = 'https://www.imdb.com'
    postURL = 'parentalguide'
    url_list = []
    i = 0
    for x in text:
        x = preURL + x + postURL
        url_list.append(x)

    url_list = unique(url_list)
    print url_list
    return url_list
def get_movie_title_list(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    title_list = [link.text for link in soup.find_all('a',
                  attrs={'href': re.compile("^\/title")})]
    for x in title_list:
        if x == ' \n':
            title_list.remove(' \n')
    for x in title_list:
        if x == 'See full summary':
            title_list.remove('See full summary')
    print title_list

    return title_list

# URL OF TOP TAMIL MOVIES LIST

movie_list_2015_url = 'https://www.imdb.com/list/ls031392332/'
movie_list_2016_url = 'https://www.imdb.com/list/ls064266039/'
movie_list_2017_url = 'https://www.imdb.com/list/ls069242710/'
movie_list_2018_url = 'https://www.imdb.com/list/ls045861940/'
movie_list_2019_url = 'https://www.imdb.com/list/ls041663030/'
movie_list_2020_url = 'https://www.imdb.com/list/ls097124558/'
movie_list_2021_url = 'https://www.imdb.com/list/ls084663427/'

# movie_urls_list = ['https://www.imdb.com/list/ls031392332/', 'https://www.imdb.com/list/ls064266039/','https://www.imdb.com/list/ls069242710/', 'https://www.imdb.com/list/ls045861940/','https://www.imdb.com/list/ls041663030/', 'https://www.imdb.com/list/ls097124558/','https://www.imdb.com/list/ls084663427/']

# GETTING EACH YEARS DETAILS IN THE FORM OF A LIST

print '**2015 MOVIES**'
u1 = get_URL_list(movie_list_2015_url)
t1 = get_movie_title_list(movie_list_2015_url)

print '**2016 MOVIES**'
u2 = get_URL_list(movie_list_2016_url)
t2 = get_movie_title_list(movie_list_2016_url)

print '**2017 MOVIES**'
u3 = get_URL_list(movie_list_2017_url)
t3 = get_movie_title_list(movie_list_2017_url)

print '**2018 MOVIES**'
u4 = get_URL_list(movie_list_2018_url)
t4 = get_movie_title_list(movie_list_2018_url)

print '**2019 MOVIES**'
u5 = get_URL_list(movie_list_2019_url)
t5 = get_movie_title_list(movie_list_2019_url)

print '**2020 MOVIES**'
u6 = get_URL_list(movie_list_2020_url)
t6 = get_movie_title_list(movie_list_2020_url)

print '**2021 MOVIES**'
u7 = get_URL_list(movie_list_2021_url)
t7 = get_movie_title_list(movie_list_2021_url)

all_movie_titles = []
all_movie_links = []
all_movie_titles = t1 + t2 + t3 + t4 + t5 + t6 + t7
all_movie_links = u1 + u2 + u3 + u4 + u5 + u6 + u7

print all_movie_titles
print all_movie_links

#### Finding the alcohol content display severity by calling the url_alc_imdb(url) function

alc_content_movie = []
for x in all_movie_links:
    alc_content_movie.append(url_alc_imdb(x))
print alc_content_movie

import pandas as pd

dict = {'Movie Name': all_movie_titles, 'IMDB Link': all_movie_links,
        'Alcoholism Displayed': alc_content_movie}
df1 = pd.DataFrame({'Movie Name': all_movie_titles})
df2 = pd.DataFrame({'IMDB Link': all_movie_links})
df3 = pd.DataFrame({'Alcoholism Displayed': alc_content_movie})

df = [df1, df2, df3]

df_final = pd.concat(df, axis=1)
df_final.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv'
                , index=False)
pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv'
            )
one = df_final[df_final['Alcoholism Displayed'] == 'Severe'].count()
two = df_final[df_final['Alcoholism Displayed'] == 'Moderate'].count()
three = df_final[df_final['Alcoholism Displayed'] == 'Mild'].count()
four = df_final[df_final['Alcoholism Displayed'] == 'Unrated'].count()
print one
print two
print three
print four

from itertools import repeat
def mov_year(url, year):
    url_c = len(url)
    movie_year = []
    movie_year.extend(repeat(year, url_c))
    return movie_year


movie_years_list = mov_year(u1, '2015') + mov_year(u2, '2016') \
    + mov_year(u3, '2017') + mov_year(u4, '2018') + mov_year(u5, '2019'
        ) + mov_year(u6, '2020') + mov_year(u7, '2021')
print movie_years_list

#### Creating the final dataset after creating and cleaning
import pandas as pd

dict = {
    'Movie Name': all_movie_titles,
    'IMDB Link': all_movie_links,
    'Alcoholism Displayed': alc_content_movie,
    'Year of Release': movie_years_list,
    }
df1 = pd.DataFrame({'Movie Name': all_movie_titles})
df2 = pd.DataFrame({'IMDB Link': all_movie_links})
df3 = pd.DataFrame({'Alcoholism Displayed': alc_content_movie})
df4 = pd.DataFrame({'Year of Release': movie_years_list})

df = [df1, df2, df3, df4]

df_final = pd.concat(df, axis=1)
df_final.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv'
                , index=False)

pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv'
            )
#### Webscrape the alcohol revenue in Tamil Nadu to find out how much is consumed<br><br>Fetched from wikipedia

import requests
from bs4 import BeautifulSoup
import re
import string
import numpy as np
import pandas as pd
url = 'https://en.wikipedia.org/wiki/TASMAC'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')
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
    print 'saved'
    return df


getTable(url)
dict_crime = {
    '2016': 467369,
    '2017': 420876,
    '2018': 499188,
    '2019': 455094,
    }

import requests
from bs4 import BeautifulSoup
import re
import string
import numpy as np
import pandas as pd
url = 'https://en.wikipedia.org/wiki/Crime_in_India'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')


def get1Table(url):
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
    return df
df1 = get1Table(url)
df2 = df1[df1['State/UT'] == 'Tamil Nadu']
df_crime = df2.T
print df_crime
df2.head(5)

df_crime.to_csv(r'crime_tn.csv', index=False)

# transposing and displaying + adding data for missing years from govt portals

pd.read_csv(r'crime_tn.csv')
df_crime = pd.read_csv(r'crime_tn.csv')
df_crime.head(7)

#### Appending the data to CSV
# manually inserting 2019-2020 and 2020-2021 from
# https://www.business-standard.com/article/economy-policy/tamil-nadu-earned-rs-33-811-crore-revenue-from-liquor-sales-121090700965_1.html

new_data = {'Fiscal Year': ['2019\xe2\x80\x9320', '2020\xe2\x80\x9321'
            ], 'Revenue in Crores (\xe2\x82\xb9)\t': ['33,811.14',
            '33,133.24'], '% Change': ['8.51%', '\xe2\x88\x922.00%']}
df = pd.DataFrame(new_data)
df.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn.csv'
          , mode='a', index=False, header=False)
print 'Data appended successfully.'

#### Data Cleaning
df = \
    pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn.csv'
                )


def year_modify(x):
    x = x.split('\xe2\x80\x93', 1)
    x = x.pop(0)
    y = int(x)
    y = y + 1
    print y
    return y


df['Fiscal Year'] = df['Fiscal Year'].apply(year_modify)

df.head()
df.to_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn_dataset.csv'
          )
pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn_dataset.csv'
            )

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

g1 = \
    pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv'
                )
g2 = \
    pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\alc_tn_dataset.csv'
                )
print 'New dataframes created'

# only require 2015 onwards for alcohol data
# new dataframe with 2015-2021 alchol data

g2 = g2.iloc[12:]
print g2

# remove unrated movies

g1 = g1[g1['Alcoholism Displayed'] != 'Unrated']
g1.head()
alc_score = []
for x in g1['Alcoholism Displayed']:
    if x == 'None':
        alc_score.append(0)
    elif x == 'Mild':
        alc_score.append(1)
    elif x == 'Moderate':
        alc_score.append(2)
    elif x == 'Severe':
        alc_score.append(3)
    else:
        alc_score.append(0)

print alc_score
g1['Alcohol_Rating'] = alc_score
g1.head()

## VISUALIZATIONS

plt.figure(figsize=[9, 9])
g1['Alcoholism Displayed'].value_counts().plot.pie()
plt.title('2015-2021 ALCOHOL AND SUBSTANCES DISPLAYED ON MOVIES')
plt.ylabel('')
plt.show()

g1_mean = g1.groupby(['Year of Release']).mean()
print g1_mean
plt.figure(figsize=[10, 3])

plt.bar(g1_mean.index, g1_mean['Alcohol_Rating'])
plt.xlabel('Year of Release')
plt.ylabel('Severity')
plt.title('Display of Alc and Substances over the Years')
plt.show()
g2 = g2.replace(',', '', regex=True)
g2['Revenue in Crores'] = g2['Revenue in Crores'].astype(float)
print g2.head()
g2.dtypes

plt.figure(figsize=[10, 5])
plt.plot(g2['Fiscal Year'], g2['Revenue in Crores'])
plt.xlabel('Year')
plt.ylabel('Revenue in Rupees (Crores)')
plt.title('Revenue collected in Tamil Nadu for Alcohol from 2015-2021')
plt.show()

plt.figure(figsize=[10, 5])
plt.plot(g1_mean.index, g1_mean['Alcohol_Rating'])
plt.xlabel('Year')
plt.ylabel('Alcohol_Rating')
plt.title('Substances displayed in Top Tamil Movies from 2015-2021: Line Graph'
          )
plt.show()

new_df_year = g1_mean

rev_year = []
rev_mon = []
for x in g2['Fiscal Year']:
    rev_year.append(x)
for x in g2['Revenue in Crores']:
    rev_mon.append(x)
new_df_year['Year'] = rev_year
new_df_year['Revenue'] = rev_mon
print new_df_year
g1['Alcohol_Rating'] = alc_score


plt.rcParams['figure.figsize'] = (12, 4)
ax = new_df_year.plot(kind='line', x='Year', y='Alcohol_Rating',
                      color='Blue', linewidth=2)

ax2 = new_df_year.plot(
    kind='line',
    x='Year',
    y='Revenue',
    secondary_y=True,
    color='Red',
    linewidth=2,
    ax=ax,
    )

plt.title('Comparison')
ax.set_xlabel('Year')
ax.set_ylabel('Movies Displaying Alcohol and Substances', color='b')
ax2.set_ylabel('Alcohol Consumed - Revenue (Rs)', color='r')

plt.savefig('result1.jpg')
plt.show()

crime_list = []
for x in df_crime['Crime']:
    crime_list.append(x)

new_df_year['Crime'] = crime_list
new_df_year = new_df_year.head(6)

print new_df_year

plt.rcParams['figure.figsize'] = (12, 4)
ax = new_df_year.plot(kind='line', x='Year', y='Alcohol_Rating',
                      color='Blue', linewidth=2)

ax2 = new_df_year.plot(
    kind='line',
    x='Year',
    y='Crime',
    secondary_y=True,
    color='Red',
    linewidth=2,
    ax=ax,
    )

plt.title('Comparison of Crime Rate and Movie Alcohol Displayed')
ax.set_xlabel('Year')
ax.set_ylabel('Movies Displaying Alcohol and Substances', color='b')
ax2.set_ylabel('Crime', color='r')
plt.savefig('result2.jpg')
plt.show()

new_df_tail = new_df_year.tail()
plt.rcParams['figure.figsize'] = (12, 4)
ax = new_df_tail.plot(
    kind='line',
    x='Year',
    y='Revenue',
    linestyle='dashed',
    marker='o',
    color='Green',
    linewidth=2,
    )

ax2 = new_df_tail.plot(
    kind='line',
    x='Year',
    y='Crime',
    secondary_y=True,
    color='Blue',
    linewidth=2,
    ax=ax,
    )

plt.title('Comparison of Alcohol Revenue and Crime Rates in Tamil Nadu')
ax.set_xlabel('Year')
ax.set_ylabel('Revenue', color='g')
ax2.set_ylabel('Crime', color='b')
plt.savefig('result3.jpg')
plt.show()
import requests
from bs4 import BeautifulSoup
import re
import string
import numpy as np


def url_violence_imdb(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    text = [p.text for p in soup.find('section', id='advisory-violence'
            )]
    req = text[3]
    req = re.sub('\[.*?\]', '', req)
    req = re.sub('[%s]' % re.escape(string.punctuation), '', req)
    req = re.sub('\s+', ' ', req)
    alc_cont = ''
    alc_cont = req.split(' ').pop(1)
    if alc_cont == 'Be':
        alc_cont = 'Unrated'


    return alc_cont

crime_list = []
df1_link = \
    pd.read_csv(r'C:\Users\Roshni\OneDrive\Desktop\Roshni\Projects\Alcohol-Movies\movies_alc.csv'
                )
for x in df1_link['IMDB Link']:
    y = url_violence_imdb(x)
    crime_list.append(y)
print crime_list

df1_link['Violence'] = crime_list
violence_score = []
for x in df1_link['Violence']:
    if x == 'None':
        violence_score.append(0)
    elif x == 'Mild':
        violence_score.append(1)
    elif x == 'Moderate':
        violence_score.append(2)
    elif x == 'Severe':
        violence_score.append(3)
    else:
        violence_score.append(0)

df1_link['Violence Rate'] = violence_score
df1_link.head(150)
df_viol_mean = df1_link.groupby(['Year of Release']).mean()
print df_viol_mean.head(10)

plt.figure(figsize=[10, 5])
plt.plot(df_viol_mean.index, df_viol_mean['Violence Rate'],
         color='Green')
plt.xlabel('Year')
plt.ylabel('Violence Rate')
plt.title('Violence in Movies from 2015-2021: Line Graph')
plt.show()

violence_rate_list = []
for x in df_viol_mean['Violence Rate']:
    violence_rate_list.append(x)
df_viol_up = df_viol_mean.head(6)
df_viol_up = df_viol_up.tail(5)

violence_rate_list_fin = violence_rate_list[1:-1]
print violence_rate_list_fin
df_viol_up['Movie Violence'] = violence_rate_list_fin

df_tot = new_df_tail
df_tot['Movie Violence'] = violence_rate_list_fin
print df_tot.head()

plt.rcParams['figure.figsize'] = (12, 4)
ax = df_tot.plot(
    kind='line',
    x='Year',
    y='Movie Violence',
    linestyle='dashed',
    marker='o',
    color='Green',
    linewidth=3,
    )

ax2 = df_tot.plot(
    kind='line',
    x='Year',
    y='Crime',
    secondary_y=True,
    linestyle='dashed',
    marker='o',
    color='Blue',
    linewidth=3,
    ax=ax,
    )

plt.title('Comparison between Violence in Movies and Crime Rates in TN')
ax.set_xlabel('Year')
ax.set_ylabel('Movie Violence Rating', color='g')
ax2.set_ylabel('Crime', color='b')
plt.savefig('result4.jpg')
plt.show()

df_tot.head(15)
df_tot.to_csv(r'final_dataset.csv')
df_tot = pd.read_csv(r'final_dataset.csv')

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.ylabel('Crime')
plt.xlabel('Year')

plt.plot(df_tot['Year'], df_tot['Crime'])
train = df_tot[df_tot['Year'] <= 2019]
test = df_tot[df_tot['Year'] >= 2019]
print train
print test
plt.plot(train['Year'], train['Crime'], color='green')
plt.plot(test['Year'], test['Crime'], color='red')
plt.ylabel('Crime')
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.title('Train/Test split for Crime data')
plt.show()

from statsmodels.tsa.statespace.sarimax import SARIMAX
y = train['Crime']
ARMAmodel = SARIMAX(y, order=(1, 0, 1))

ARMAmodel = ARMAmodel.fit()

y_pred = ARMAmodel.get_forecast(len(test))
y_pred_df = y_pred.conf_int(alpha=0.05)
y_pred_df['Predictions'] = ARMAmodel.predict(start=y_pred_df.index[0],
        end=y_pred_df.index[-1])
y_pred_df.index = test.index
y_pred_out = y_pred_df['Predictions']


plt.plot(y_pred_out, color='green', label='Predictions')
plt.legend()

X = df_tot[['Year', 'Alcohol_Rating', 'Crime']]
y = df_tot['Movie Violence']

# x1 = year
# x2 = alc revenue
# x3 = crime rate
# y (to predict) = violence in movie

from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedViolence = regr.predict([[2020, 1.65, 30000]])
print predictedViolence

predictedViolence = regr.predict([[2021, 1.45, 32100]])
print predictedViolence

predictedViolence = regr.predict([[2022, 1.65, 30000]])
print predictedViolence

predictedViolence = regr.predict([[2026, 1.35, 30500]])
print predictedViolence

from sklearn.model_selection import train_test_split
(X_train, X_test, y_train, y_test) = train_test_split(X, y,
        test_size=0.33)

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)

from sklearn.metrics import mean_squared_error, mean_absolute_error
np.sqrt(mean_squared_error(y_test, y_pred))

# mean_absolute_error(y_test, y_pred)

from sklearn.model_selection import train_test_split
(X_train, X_test, y_train, y_test) = train_test_split(X, y,
        test_size=0.25, random_state=1)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error, mean_absolute_error
y_pred = model.predict(X_test)
import numpy as np
er = np.sqrt(mean_squared_error(y_test, y_pred))
er
