import re
import logging

from bs4 import BeautifulSoup

from locators.books_page_locators import BooksPageLocators
from parsers.book import BookParser

logger = logging.getLogger('scraping.all_books_page')


class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using "{BooksPageLocators.BOOK}".')
        locator = BooksPageLocators.BOOK
        books_tags = self.soup.select(locator)
        return [BookParser(e) for e in books_tags]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(BooksPageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: "{content}"')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: "{pages}"')
        return pages
