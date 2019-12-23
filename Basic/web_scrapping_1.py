# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
import requests
from bs4 import BeautifulSoup as b_s

base_url = "https://www.yelp.com/search?find_desc=&find_loc="
print("Enter the location you want to get data of ")
loc = input()
page = int(input())
val = (page-1)*10 

#format example 'New York, NY'
url = base_url + loc +  "&start=" + str(val)

yelp_r = requests.get(url) 
#Execute "yelp_r" to check connection status.

#Above written gives the whole source code.

yelp_soup = b_s(yelp_r.text, 'html.parser')
print(yelp_soup.prettify())
#The above 2 lines make the source code of the page more readable.

print(yelp_soup.findAll('a'))
#The above line of codegets al the link on the page.

for link in yelp_soup.findAll('a'):
    print(link)
#It print all the links on the page in a more formatted way.

for name in yelp_soup.findAll('a', {'class':'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'}):
    print(name.text)
#Above code give the names of all the restaurants having anchor tag of above written class.
