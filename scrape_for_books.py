from bs4 import BeautifulSoup
import requests


def scrape_data():
    url = "https://books.toscrape.com/catalogue/page-*.html"
    number_of_pages = 51

    # Creating the file to save the book data
    with open(f"fetched_books.csv", 'w', encoding='utf-8') as f:
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