import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from helpers import print_successful_login_info, print_auction_info, print_message


class AuctionBot:
    """Creates the AuctionBot object."""

    def __init__(self, auction_url: str, price_limit: int, users_bid: int,
                 price_check_frequency: int = 60, browser_visible: bool = False):
        """Creates the new instance of AuctionBot object.

        :Args:
         - auction_url - url to the auction
         - price_limit - the maximum price that you want to pay for the item
         - increment_value - new bid placed by the bot will be items_current_price + increment_value
         - browser_visible - (Optional) Whether you want to see the browser or not.
        """

        self.auction_url = auction_url
        self.price_limit = price_limit
        self.browser_visible = browser_visible
        self.price_check_frequency = price_check_frequency

        self.users_bid = users_bid

        self.auction_item = None
        self.current_price = None

        self.driver_options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=self.driver_options)
        self.driver.implicitly_wait(2)  # wait 2 seconds after every driver command

    def __del__(self):
        self.driver.quit()

    def login(self) -> None:
        """Log in to your allegro account"""

        # open login page
        self.driver.get('https://allegrolokalnie.pl/logowanie')

        # after successful log in
        WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.5) \
            .until(lambda x: ('https://allegrolokalnie.pl' in self.driver.current_url))

        username = self.driver.find_element(By.CSS_SELECTOR, 'span.mlc-masthead__username') \
            .get_attribute('innerHTML')
        print_successful_login_info(username)  # print info about logged user

        # if user set browser visibility to False -> hijack session and open in headless browser
        if not self.browser_visible:
            self._stealth_mode()

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

    def get_users_bid(self) -> int:
        return self.users_bid

    def get_price_check_frequency(self) -> int:
        return self.price_check_frequency

    def get_auction_title(self) -> str:
        self._go_to_auction_url()

        auction_heading = self.driver.find_element(By.CSS_SELECTOR, 'h1.ml-heading')
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1).until(
            lambda x: auction_heading.is_displayed()
        )

        self.auction_item = auction_heading.text or ''
        return self.auction_item

    def get_auction_current_price(self) -> int:
        self._go_to_auction_url()

        # I am too lazy to implement getting the decimal part, deal with it
        current_price_element = self.driver.find_element(By.CSS_SELECTOR, 'span.ml-offer-price__dollars')
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1).until(
            lambda x: current_price_element.is_displayed()
        )

        self.current_price = int(current_price_element.get_attribute('innerHTML') or -1)
        return self.current_price

    def get_auction_details(self, print_info: bool = True) -> None:
        self._go_to_auction_url()

        # get the title of the auction
        self.get_auction_title()

        # get current price
        self.get_auction_current_price()

        if print_info:
            print_auction_info(self.auction_item, self.current_price, self.users_bid)

    def check_if_offer_is_active(self) -> None:
        self._go_to_auction_url()

        try:
            auction_ended_banner = self.driver.find_element(By.CSS_SELECTOR, 'p.mlc-offer-ended-banner__text')
            expired = auction_ended_banner.is_displayed()
            if expired:
                print_message('The auction has ended!', False)
                exit(0)
        except NoSuchElementException:
            pass

    def price_changed(self) -> bool:
        """Wait for the item's price to change."""
        self._go_to_auction_url()

        # refresh the page just for safety
        self.driver.refresh()

        current_price_element = self.driver.find_element(By.CSS_SELECTOR, 'span.ml-offer-price__dollars')
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1).until(
            lambda x: current_price_element.is_displayed()
        )

        price_changed = self.current_price != int(current_price_element.get_attribute('innerHTML'))
        if price_changed:
            self.get_auction_details()

        return price_changed

    def make_an_offer(self) -> None:
        self._go_to_auction_url()

        # get bidding button
        bidding_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="offer-bidding-button"')
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.2).until(
            lambda x: bidding_button.is_displayed()
        )
        bidding_button.click()  # click the "Licytuj" button, it doesn't make the bid yet
        del bidding_button  # remove bidding button variable

        # get confirmation bidding button
        confirmation_bidding_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="offer-bidding-modal-accept"]'
        )
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.2).until(
            lambda x: confirmation_bidding_button.is_displayed()
        )

        # update items current price
        self.current_price = self.get_auction_current_price()

        # check if the price is not too high
        if self.current_price + 1 > self.price_limit:
            print_message("Price too high!", False)
            exit(0)

        # calculate your bid, by default the bids on allegrolokalnie increase by 1zł
        self.users_bid = self.current_price + 1

        # make an offer
        print_message(f"Click: {confirmation_bidding_button.get_attribute('innerHTML')}", True)
        confirmation_bidding_button.click()
        del confirmation_bidding_button  # remove confirmation bidding button variable
        time.sleep(1)  # wait 1 second after clicking the button

        # get new details and print
        self.get_auction_details()
