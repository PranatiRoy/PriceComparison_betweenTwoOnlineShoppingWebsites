cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
import time
import pandas as pd
from bs4 import BeautifulSoup # for the beautiful soup we have to send the source code for the page.
from selenium import webdriver
b=webdriver.Chrome(cd)
b.get("https://www.amazon.in/LG-Inverter-Direct-Cool-Refrigerator-GL-D201ARGY/dp/B07W56VWTS/ref=sr_1_2?dchild=1&keywords=lg+190l&qid=1604658995&sr=8-2")

time.sleep(5)
pg1source=b.page_source # return the source code
ref1=BeautifulSoup(pg1source,'html.parser')
#print(ref1)
f1=ref1.find('span',{'id':"priceblock_ourprice"})
print(f1.text)
a=f1.text[2:]
c=a.split(',')
p1=float(c[0]+c[1])

b.get("https://www.flipkart.com/lg-190-l-direct-cool-single-door-4-star-refrigerator/p/itmfgygmuavx9dfc?pid=RFRFGYGH53K4WSFS&lid=LSTRFRFGYGH53K4WSFS5VWFJG&marketplace=FLIPKART&q=LG+190+L+4+Star+Inverter+Direct-Cool+Single+Door+Refrigerator+%28GL-D201ARGY%2C+Ruby+Glow%2C+Base+Stand+with+drawer%29&store=j9e%2Fabm%2Fhzg&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=ba77752d-2f50-4d93-b281-0a4a8a115d16.RFRFGYGH53K4WSFS.SEARCH&ppt=pp&ppn=pp&ssid=j8p379teww0000001617122129189&qH=6b2232ef28f2b7b6")
pg2source=b.page_source # return the source code
ref2=BeautifulSoup(pg2source,'html.parser')
f2=ref2.find('div',{'class':"_30jeq3 _16Jk6d"})
print(f2.text)
e=f2.text[1:]
g=e.split(',')
p2=float(g[0]+g[1])

if p1>p2:
	print("Better to buy at flipkart")
elif p2>p1:
	print("Better to buy at amazon")
else:
	print("Anywhere you can buy")	
