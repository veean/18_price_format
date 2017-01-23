# Price Formatter

Данный скрипт приводит цену к наглядному виду. 
К примеру : 3245.000000 приводится к виду 3 245. Для этого в виде параметра скрипта необходимо указать цену для форматирования.
Если цену не удалось отформатировать скрипт вернет  `None` .

## Использование
* Скачиваем скрипт :  `git clone https://github.com/veean/18_price_format.git`
* Используем из командной строки : `python format_price 7654.567890` 
* Запускаем тесты для скрипта `python tests.py`
* Используем в виде импортируемого модуля 
    
      import format_price
      
      print(format_price.format_price('446,00'))
      
## Зависимости

 * Python 3.5 и выше.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
