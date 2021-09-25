from requests import get, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(currency_code):
    content = response.split("<Valute ID=")
    for i in content:
        if currency_code.upper() in i:
            print(currency_code.upper(), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


# print(currency_rates("uSd"))
print(currency_rates(input("Код валюты: ")))
