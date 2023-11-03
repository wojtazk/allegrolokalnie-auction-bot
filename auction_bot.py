from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helpers import print_successful_login_info, print_auction_info
import time


class AuctionBot:
    """Creates the AuctionBot object."""

    def __init__(self, auction_url: str, price_limit: int, increment_value: int, browser_visible: bool = False) -> None:
        """Creates the new instance of AuctionBot object.

        :Args:
         - auction_url - url to the auction
         - price_limit - the maximum price that you want to pay for the item
         - increment_value - new bid placed by the bot will be items_current_price + increment_value
         - browser_visible - (Optional) Whether you want to see the browser or not.
        """

        self.auction_url = auction_url
        self.price_limit = price_limit
        self.increment_value = increment_value
        self.browser_visible = browser_visible

        self.auction_item = None
        self.current_price = None
        self.next_bid = None

        self.driver_options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=self.driver_options)

    def __del__(self):
        self.driver.close()

    def login(self) -> None:
        """Log in to your allegro account"""

        # open login page
        self.driver.get('https://allegrolokalnie.pl/logowanie')

        # after successful log in
        WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.5) \
            .until(lambda x: ('https://allegrolokalnie.pl' in self.driver.current_url))

        self.driver.implicitly_wait(30)
        username = self.driver.find_element(By.CSS_SELECTOR, 'span.mlc-masthead__username') \
            .get_attribute('innerHTML')
        print_successful_login_info(username)  # print info about logged user
        time.sleep(10)  # FIXME

        # if user set browser visibility to False -> hijack session and open in headless browser
        if not self.browser_visible:
            self._stealth_mode()

        # FIXME: just a quick test for a headless browser
        # username = self.driver.find_element(By.CSS_SELECTOR, 'span.mlc-masthead__username') \
        #     .get_attribute('innerHTML')
        # print(username)
        # time.sleep(10)  # FIXME

    def _stealth_mode(self) -> None:
        """Change from normal browser to headless"""
        self.driver_options.add_argument('-headless')

        cookies = self.driver.get_cookies()
        self.driver.close()

        self.driver = webdriver.Firefox(options=self.driver_options)
        self.driver.get('https://allegrolokalnie.pl/')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://allegrolokalnie.pl')

    def _go_to_auction_url(self) -> None:
        if self.driver.current_url != self.auction_url:
            self.driver.get(self.auction_url)

    def get_auction_title(self) -> str:
        self._go_to_auction_url()

        auction_heading = self.driver.find_element(By.CSS_SELECTOR, 'h1.ml-heading')
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1).until(
            lambda x: auction_heading.is_displayed()
        )

        return auction_heading.text or ''

    def get_auction_current_price(self) -> int:
        self._go_to_auction_url()

        # auctions dont have decimal parts, only integers
        current_price_element = self.driver.find_element(By.CSS_SELECTOR, 'span.ml-offer-price__dollars')
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1) \
            .until(lambda x: current_price_element.is_displayed())

        return int(current_price_element.get_attribute('innerHTML') or -1)

    def get_auction_details(self) -> None:
        self._go_to_auction_url()

        # get the title of the auction
        self.auction_item = self.get_auction_title()

        # get current price
        self.current_price = self.get_auction_current_price()

        print_auction_info(self.auction_item, self.current_price)  # FIXME
