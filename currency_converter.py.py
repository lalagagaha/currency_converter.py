import requests
print('Конвертер валют')
popular_currencies = ["EUR", "GBP", "RUB", "JPY", "CHF", "CAD", "AUD", "USD"]

try:
    code_currency = str.upper(input('Введите код валюты: '))
    if not code_currency.strip():
        print("Код валюты не может быть пустым.")
    if code_currency not in popular_currencies:
        print('Код валюты введен некорректно')
    else:
        quantity = int(input('Количество валюты: '))
except ValueError:
    print('Код валюты или его количество введены неверно')

def currency(x): 
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{x}")
    data = response.json()
    rates = data["rates"]
    if rates.get(f"{code_currency}") == True:
        for currency in popular_currencies:
            if code_currency != currency:
                print(f'{quantity} {code_currency} - {round(rates.get(f"{currency}") * quantity, 3)} {currency}')
currency(code_currency)