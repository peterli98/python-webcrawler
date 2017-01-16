import requests
from bs4 import BeautifulSoup

def search_spider():

        url = "https://www.google.ca/?gfe_rd=cr&ei=oSMtWJj1OKSC8QettpjQAw#q=swimming&start=" + str(start)
        source_code = requests.get(url) #get all the source codes and store them in a variable
        plain_text = source_code.text #get all the texts from source codes and store them in a variable
        soup = BeautifulSoup(plain_text,"html.parser") #transform the data from plain_text to a format beautifulsoup can read and store in soup
        for link in soup.findAll("a" ,{"onmousedown":"return rwt"}):
            title = link.string
            print(title)
        start += 10


search_spider(0)