import argparse


def choose_formatting(price):
    if price.is_integer():
        return ',.0f'
    else:
        return ',.2f'


def format_price(price):

    try:
        if isinstance(price, str):
            price = price.replace(',', '.')
        formatted_price = float(price)
    except (ValueError, TypeError):
        return None
    formatted_price = round(formatted_price, 2)

    if formatted_price > 0:
        return format(formatted_price, choose_formatting(formatted_price)).replace(',', ' ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='specify price to make it beautiful')
    users_price = parser.parse_args().price

    print(format_price(users_price))
