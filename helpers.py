BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
WARN = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'


def _get_auction_info() -> (str, int, int, int, bool, str):
    auction_url = input(f"{CYAN}Link for the auction (ex: https://example.com): {RESET}")
    if (auction_url == '') or (' ' in auction_url) or ('https://allegrolokalnie.pl/' not in auction_url):
        raise ValueError('Wrong URL provided!')

    price_limit = int(
        # tha max price that you can pay
        input(f"{CYAN}Set the item's upper price limit (integer): {RESET}")
    )
    if price_limit <= 0:
        raise ValueError('Price limit <= 0, RLY??')

    users_current_bid = int(
        input(f"{CYAN}If you had already placed the bid enter its value (integer) (default=0): {RESET}") or 0
    )
    if users_current_bid < 0:
        raise ValueError('Users current bid < 0!')

    price_check_frequency = int(
        input(f"{CYAN}Price check frequency [sec] (default=60): {RESET}") or 60
    )
    if price_check_frequency <= 0:
        raise ValueError('Price check frequency <= 0!')

    browser_visible = input(f"{CYAN}Do you want the browser to be visible (default=y) (y/n): {RESET}") or 'y'
    if browser_visible not in ('y', 'n'):
        raise ValueError("Browser visibility can take only 'y' or 'n' values!")

    browser_visible = browser_visible == 'y'

    print(f'\n{WARN}Check the provided info!{RESET}')
    print(
        f'url: {BLUE}{auction_url}{RESET}',
        f'price limit: {BLUE}{price_limit} zł{RESET}',
        f'your current bid: {BLUE}{users_current_bid} zł{RESET}',
        f'price check frequency: {BLUE}{price_check_frequency} sec{RESET}',
        f'browser visibility: {BLUE}{browser_visible}{RESET}',
        sep='\n'
    )

    info_is_correct = input(f'{WARN}Is this information correct (default=y) (y/n): {RESET}') or 'y'
    print()

    return auction_url, price_limit, users_current_bid, price_check_frequency, browser_visible, info_is_correct


def ask_user_for_info() -> {str, int, int, bool}:
    """Ask user for url to the auction,
     maximum price for the item,
     and the value of increments for the bids"""
    (auction_url, price_limit, users_current_bid, price_check_frequency,
     browser_visible, info_is_correct) = _get_auction_info()
    while info_is_correct != 'y':
        (auction_url, price_limit, users_current_bid, price_check_frequency,
         browser_visible, info_is_correct) = _get_auction_info()

    return {
        'auction_url': auction_url,
        'price_limit': price_limit,
        'users_bid': users_current_bid,
        'price_check_frequency': price_check_frequency,
        'browser_visible': browser_visible
    }


def print_login_info() -> None:
    print(f'{GREEN}Press enter and login to your allegro account in the browser...{RESET}', end='')


def print_successful_login_info(username: str) -> None:
    print(f'{GREEN}Successfully logged in as:{RESET} {BLUE}{username}{RESET}')
    print()


def print_auction_info(item: str, current_price: int, your_offer: int) -> None:
    your_offer_color = GREEN if current_price == your_offer else RED
    print(f'item: {BLUE}{item}{RESET}, current price: {BLUE}{current_price} zł{RESET},'
          f' your offer: {your_offer_color}{your_offer}{RESET}')


def print_message(message: str, positive: bool = True) -> None:
    color = GREEN if positive else RED
    print(f'{color}{message}{RESET}')
