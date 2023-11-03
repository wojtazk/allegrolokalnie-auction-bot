from auction_bot import AuctionBot
# from user_credentials_dialog import UserCredentialsDialog
from helpers import ask_user_for_info, print_login_info


# get user's credentials
# credentials_dialog = UserCredentialsDialog()
# user_login, user_password = credentials_dialog.get_credentials()
# if not (user_login and user_password):
#     exit(1)


# ask user to provide information for the bot
# bot_arguments = ask_user_for_info()  # FIXME


# inform user about logging in
# login_info()
# input()

# create instance of AuctionBot object
# FIXME: uncomment this
# auction_bot = AuctionBot(**bot_arguments)

# login with normal browser (gui),
# if you set the browser_visible to False then the browser will change to a headless browser
# auction_bot.login()

# FIXME: get auction details test
test_bot = AuctionBot('https://allegrolokalnie.pl/oferta/raspberry-pi-4-model-b-416-gb',
                      160, 1, False)

# test_bot.login()
test_bot.get_auction_details()


