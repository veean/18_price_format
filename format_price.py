import argparse


def choose_formatting(price):
    if price.is_integer():
        return ',.0f'
    else:
        return ',.2f'


def format_price(price):
    if price > 0:
        try:
            formatted_price = float(price)
        except (ValueError, TypeError):
            return None
    else:
        return None





if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('price', help='specify price to make it beautiful')
    # users_price = parser.parse_args().price

    users_price = input('price : ')

    formatted_price = users_price.replace(',', '.')

    pp = float(formatted_price)

    print(format(pp, ',.2f').replace(',', ' '))