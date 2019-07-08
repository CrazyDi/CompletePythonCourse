import requests
import logging

from pages.books_page import BooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get(f'http://books.toscrape.com').content
page = BooksPage(page_content)

books = None
for i in range(page.page_count):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{i+1}.html').content
    page = BooksPage(page_content)
    logger.debug('Creating AllBooksPAge from page content.')
    if books is None:
        books = page.books
    else:
        books.extend(page.books)


print(len(books))
