
# coding: utf-8

# In[2]:

from bs4 import BeautifulSoup
import urllib2

redditFile = urllib2.urlopen("http://www.weddingbee.com")
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))


# In[ ]:



