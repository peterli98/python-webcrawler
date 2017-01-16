import requests
from bs4 import BeautifulSoup

def search_spider(max_page):
    page = 0
    while page <= max_page:
        url = "https://myanimelist.net/topanime.php?limit=" + str(page) //save desired url to a variable
        source_code = requests.get(url) #get the information of that link
        plain_text = source_code.text #strip the source code of that link store it in variable plain_text
        soup = BeautifulSoup(plain_text, 'html.parser') #turn the source code into an object so we can apply methods
        for link in soup.findAll('a' ,{'class': 'hoverinfo_trigger fl-l fs14 fw-b'}): #this specific point in this html
            title = link.string #get the title
            href = link.get('href') #the the url of this link 
            print (title) 
            print(href)
            single_item(href) #calls function
        page += 50



def single_item (item_url):
    source_code = requests.get(item_url) 
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')  

    for score in soup.findAll('span', {'itemprop': 'ratingValue'}): #get rating
        print("Score: " + score.string)

search_spider(50)
