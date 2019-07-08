import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')

class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name} cost {self.price} rating {self.rating}>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME
        item_name = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found book name, "{item_name}".')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK
        logger.debug(f'Found book link, "{self.parent.select_one(locator).attrs["href"]}".')
        return self.parent.select_one(locator).attrs['href']

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE
        item_text = self.parent.select_one(locator).string
        item = float(re.findall('[0-9]+\.[0-9]+', item_text)[0])
        logger.debug(f'Found book price, "{item}".')
        return item

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING
        classes = self.parent.select_one(locator).attrs['class']
        rating_classes = [self.RATINGS[r] for r in classes if r != 'star-rating']
        logger.debug(f'Found book rating, "{rating_classes[0]}".')
        return rating_classes[0]
