from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime


def scrape_data():
    url = "https://books.toscrape.com/catalogue/page-*.html"
    number_of_pages = 51
    current_datetime = datetime.now().strftime("%y%m%d-%H%M")

    # Creating a unique csv file to save the book data
    with open(f"fetched_books_{current_datetime}.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'price', 'rating', 'stock'])

        for page in range(1,number_of_pages):
            page_url = url.replace('*', str(page))
            webpage = requests.get(page_url).text
            soup = BeautifulSoup(webpage, "lxml")
            books = soup.findAll(class_="product_pod") 
            
            for book in books:
                book_title = book.h3.a['title']
                book_price = book.find(class_="price_color").text
                star_rating = book.p['class']
                stock = book.find(class_="instock availability").text
                print(f"{book_title.replace(',', '')}, {book_price.replace('Â', '')}, {star_rating[-1]}, {stock.strip()}", file=f)
    f.close()


if __name__ == '__main__':
    scrape_data()