from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class AuctionBot:
    """Creates the AuctionBot object."""

    def __init__(self, browser_visible: bool = False) -> None:
        """Creates the new instance of AuctionBot object.

        :Args:
         - browser_visible - (Optional) Whether you want to see the browser or not.
        """

        self.browser_visible = browser_visible

        self.driver_options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=self.driver_options)

    def __del__(self):
        self.driver.close()

    def login(self) -> None:
        """Log in to your allegro account"""

        # open login page
        self.driver.get('https://allegro.pl/logowanie')
        self.driver.implicitly_wait(2)  # FIXME

        # reject consent modal
        dont_accept_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-role="reject-rodo"]')
        dont_accept_button.click()
        self.driver.implicitly_wait(30)  # FIXME

        # after successful log in
        print(self.driver.current_url)
        WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.5) \
            .until(lambda x: (self.driver.current_url == 'https://allegro.pl/'))

        username = self.driver.find_element(By.CSS_SELECTOR, 'span[data-role="header-username"]') \
            .get_attribute('innerHTML')
        print(f'Successfully logged in as: {username}')
        time.sleep(10)  # FIXME

        # if user set browser visibility to False -> hijack session and open in headless browser
        if not self.browser_visible:
            self.driver_options.add_argument('-headless')

            cookies = self.driver.get_cookies()
            self.driver.close()

            self.driver = webdriver.Firefox(options=self.driver_options)
            self.driver.get('https://allegro.pl/')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get('https://allegro.pl/')

        # FIXME: just a quick test for a headless browser
        username = self.driver.find_element(By.CSS_SELECTOR, 'span[data-role="header-username"]') \
            .get_attribute('innerHTML')
        print(username)
        time.sleep(30)  # FIXME
