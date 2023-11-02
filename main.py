from auction_bot import AuctionBot
# from user_credentials_dialog import UserCredentialsDialog
from helpers import ask_user_for_info, login_info


# get user's credentials
# credentials_dialog = UserCredentialsDialog()
# user_login, user_password = credentials_dialog.get_credentials()
# if not (user_login and user_password):
#     exit(1)


# ask user to provide information for the bot
bot_arguments = ask_user_for_info()


# login with normal browser (gui),
# if you set the browser_visible to False then the browser will change to a headless browser
login_info()
input()

# create instance of AuctionBot object
auction_bot = AuctionBot(**bot_arguments)
auction_bot.login()
