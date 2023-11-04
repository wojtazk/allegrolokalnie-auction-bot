from auction_bot import AuctionBot
# from user_credentials_dialog import UserCredentialsDialog
from helpers import ask_user_for_info, print_login_info, print_message
from selenium.common.exceptions import (NoSuchElementException, NoSuchWindowException,
                                        WebDriverException, InvalidSessionIdException)
import time


# get user's credentials
# credentials_dialog = UserCredentialsDialog()
# user_login, user_password = credentials_dialog.get_credentials()
# if not (user_login and user_password):
#     exit(1)

try:
    # ask user to provide information for the bot
    bot_arguments = ask_user_for_info()

    # inform user about logging in
    print_login_info()
    input()

    # create instance of AuctionBot object
    auction_bot = AuctionBot(**bot_arguments)

    # login with normal browser (gui),
    # if you set the browser_visible to False then the browser will change to a headless browser
    auction_bot.login()

    # get auction details
    auction_bot.get_auction_details()

    # check if the auction is still active
    auction_bot.check_if_offer_is_active()

    # make an offer if user didn't already
    if auction_bot.get_users_bid() == 0:
        auction_bot.make_an_offer()

    # wait for price change and then stuff
    price_check_frequency = auction_bot.get_price_check_frequency()
    while True:
        while not auction_bot.price_changed():
            auction_bot.check_if_offer_is_active()
            time.sleep(price_check_frequency)

        auction_bot.make_an_offer()
except (KeyboardInterrupt, NoSuchElementException, NoSuchWindowException,
        WebDriverException, InvalidSessionIdException) as err:
    print()
    print_message('Bot terminated!', False)
    print_message(type(err).__name__, False)
    exit(1)
