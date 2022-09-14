#import libraries 
from bs4 import BeautifulSoup
import requests
import csv

#get url
url = "https://www.amazon.com/Best-Sellers-Books/zgbs/books"

#change the user-agent value based on your web brwser 
headers = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100'}

#get requests
page = requests.get(url,headers= headers)

#verify that URL is detected properly 
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

#get all books 
books = soup.find_all(id="gridItemRoot")
#just viewing the html code of the first book to inspect the elements individually 

#create csv headers 
csv_headers = ['Rank', 'Title', 'Author', 'Price']
with open('amazon_books.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)

#line29-43 is where I check whether code obtains the desired information
children = book.find("div", {"class":"zg-grid-general-faceout"}).div
#print(children)

title = children.contents[1].text
print(title)

author = children.contents[2].text
print(author)

price = children.contents[-1].text
print(price)

rating = children.contents[3].text
print(rating)

#altogether now, generating csv
for book in books: 
       
    rank = book.find("span",{"class": "zg-bdg-text"}).text[1:]

    children = book.find("div", {"class":"zg-grid-general-faceout"}).div

 
    title = children.contents[1].text
    author = children.contents[2].text
    price = children.contents[-1].text
    rating = children.contents[3].text
   
    with open('amazon_books.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([rank, title, author, price,rating])
