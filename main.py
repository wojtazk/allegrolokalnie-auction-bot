from auction_bot import AuctionBot
from user_credentials_dialog import UserCredentialsDialog


# get user's credentials
# credentials_dialog = UserCredentialsDialog()
# user_login, user_password = credentials_dialog.get_credentials()
# if not (user_login and user_password):
#     exit(1)


# create instance of AuctionBot object
auction_bot = AuctionBot(browser_visible=False)

# login with normal browser (gui),
# if you set the browser_visible to False then the browser will change to a headless browser
auction_bot.login()
