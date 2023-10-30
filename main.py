from auction_bot import AuctionBot
from user_credentials_dialog import UserCredentialsDialog


# get user's credentials
credentials_dialog = UserCredentialsDialog()
user_login, user_password = credentials_dialog.get_credentials()
if not (user_login and user_password):
    exit(1)


# create instance of AuctionBot object
auction_bot = AuctionBot()

# login with provided username and password
auction_bot.login(user_login, user_password)
