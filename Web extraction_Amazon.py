# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:58:16 2021

@author: DELL
"""
#Extract reviews of any product from ecommerce website like amazon
#Web scraping(review extraction) from amazon

#Importing the libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

#Get the link
link = "https://www.amazon.in/Nike-Mens-Vapormax-Running-Shoes/product-reviews/B07ZQ71J9J/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
page=requests.get(link)
page

#Get the page content
page.content

#creating soup object to iterate over the extracted content
soup=bs(page.content,'html.parser') 

#To get the html doc type
print(soup.prettify())



#To get the profile names
names=soup.find_all('span',class_='a-profile-name')
names
len(names)

#To extract the customer names
cust_name=[]
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())

cust_name
cust_name.pop(0)
cust_name.pop(0)
cust_name.pop(0)
cust_name

#To extract the review title
title=soup.find_all('a',class_='review-title')
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title

To remove the slashes in b/w
review_title[:]=[titles.lstrip('\n') for titles in review_title]
review_title
review_title[:]=[titles.rstrip('\n') for titles in review_title]
review_title


#To extract the ratings
rating=soup.find_all('i',class_='review-rating')
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate    
len(rate)
rate.pop(0)
rate.pop(0)
rate
len(rate)

#To extract the content of the review
review=soup.find_all('span',{'data-hook':'review-body'})
review
review_content=[]
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content
#remove the slashes in b/w the review_content
review_content[:]=[reviews.lstrip('\n\n') for reviews in review_content]
review_content
review_content[:]=[reviews.rstrip('\n\n') for reviews in review_content]
review_content

len(review_content)

cust_name
review_title
rate
review_content

import pandas as pd
df=pd.DataFrame()
df['customer name']=cust_name
df
df['Review Title']=review_title
df['Ratings']=rate
df['Reviews']=review_content






















