from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helpers import successful_login_info
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

        self.driver_options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=self.driver_options)

    def __del__(self):
        self.driver.close()

    def login(self) -> None:
        """Log in to your allegro account"""

        # open login page
        self.driver.get('https://allegro.pl/logowanie')

        # after successful log in
        WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.5) \
            .until(lambda x: (self.driver.current_url == 'https://allegro.pl/'))

        self.driver.implicitly_wait(30)
        username = self.driver.find_element(By.CSS_SELECTOR, 'span[data-role="header-username"]') \
            .get_attribute('innerHTML')
        successful_login_info(username)  # print info about logged user
        time.sleep(10)  # FIXME

        # if user set browser visibility to False -> hijack session and open in headless browser
        if not self.browser_visible:
            self._stealth_mode()

        # FIXME: just a quick test for a headless browser
        username = self.driver.find_element(By.CSS_SELECTOR, 'span[data-role="header-username"]') \
            .get_attribute('innerHTML')
        print(username)
        time.sleep(30)  # FIXME

    def _stealth_mode(self):
        self.driver_options.add_argument('-headless')

        cookies = self.driver.get_cookies()
        self.driver.close()

        self.driver = webdriver.Firefox(options=self.driver_options)
        self.driver.get('https://allegro.pl/')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://allegro.pl/')
