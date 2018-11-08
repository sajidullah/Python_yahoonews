"""
Created on Thu Nov  8 15:11:57 2018

@author: sajid Ullah
"""

import bs4
import lxml #xml parser
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def news(xml_news_url):
	
	Client=urlopen(xml_news_url)
	xml_page=Client.read()
	Client.close()
	
	soup_page=soup(xml_page,"xml")
	
	news_list=soup_page.findAll("item")
	
	for news in news_list:
		
		print(news.title.text)
		print(news.link.text)
		print(news.pubDate.text)	
		print("\n\n")



		
news_url="https://news.yahoo.com/rss/mostviewed"
news(news_url)	

