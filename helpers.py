BLUE = '\033[94m'
GREEN = '\033[92m'
WARN = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'


def _get_auction_info() -> (str, int, int, bool, str):
    auction_url = input(f"Link for the auction (ex: https://example.com): ")
    if (auction_url == '') or (' ' in auction_url) or ('https://allegrolokalnie.pl/' not in auction_url):
        raise ValueError('Wrong URL provided!')

    price_limit = int(input(f"Set the item's upper price limit (integer): "))  # the maximum price you want to pay
    if price_limit <= 0:
        raise ValueError('Price limit <= 0, RLY??')

    price_check_frequency = int(input(f"Price change check frequency [sec] (default=60): ") or 60)
    if price_check_frequency <= 0:
        raise ValueError('Price check frequency <= 0 !')

    browser_visible = input("Do you want the browser to be visible (default=y) (y/n): ") or 'y'
    if browser_visible not in ('y', 'n'):
        raise ValueError("Browser visibility can take only 'y' or 'n' values!")

    browser_visible = browser_visible == 'y'

    print(f'\n{WARN}Check the provided info!{RESET}')
    print(
        f'url: {BLUE}{auction_url}{RESET}',
        f'price limit: {BLUE}{price_limit}{RESET}',
        f'price check frequency: {BLUE}{price_check_frequency}{RESET}',
        f'browser visibility: {BLUE}{browser_visible}{RESET}',
        sep='\n'
    )

    info_is_correct = input(f'{WARN}Is this information correct (default=y) (y/n): {RESET}') or 'y'
    print()

    return auction_url, price_limit, price_check_frequency, browser_visible, info_is_correct


def ask_user_for_info() -> {str, int, int, bool}:
    """Ask user for url to the auction,
     maximum price for the item,
     and the value of increments for the bids"""
    auction_url, price_limit, price_check_frequency, browser_visible, info_is_correct = _get_auction_info()
    while info_is_correct != 'y':
        auction_url, price_limit, price_check_frequency, browser_visible, info_is_correct = _get_auction_info()

    return {
        'auction_url': auction_url,
        'price_limit': price_limit,
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
