from selenium import webdriver
from selenium.webdriver.common.by import By


class AuctionBot:
    """Creates the AuctionBot object."""

    def __init__(self, browser_visible: bool = False) -> None:
        """Creates the new instance of AuctionBot object.

        :Args:
         - browser_visible - (Optional) Whether you want to see the browser or not.
        """

        self.driver_options = webdriver.FirefoxOptions()
        if browser_visible:
            self.driver_options.add_argument('-headless')

        self.driver = webdriver.Firefox(options=self.driver_options)

    def __del__(self):
        self.driver.close()

    def login(self, username: str, password: str) -> None:
        """Log in to your allegro account"""

        # open login page
        self.driver.get('https://allegro.pl/logowanie')
        self.driver.implicitly_wait(2)

        # reject consent modal
        dont_accept_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-role="reject-rodo"]')
        dont_accept_button.click()
        self.driver.implicitly_wait(2)

        # time to log in
        username_field = self.driver.find_element(By.ID, 'login')
        password_field = self.driver.find_element(By.ID, 'password')

        username_field.send_keys(username)
        password_field.send_keys(password)

        print(username_field.get_attribute('value'))

