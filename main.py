# PLN
# USD -> PLN  #
# EUR -> PLN  #

# 1. Wybór język programowania
# 2. Kodowanie = programowanie
# 3. Testowanie = QA (Quality Assurance) = kontrola jakość

# Język programowania:  https://www.python.org/downloads/
# Edytor kodu (Word dla programistów):  Visual Studio Code  https://code.visualstudio.com

# W terminalu:
# python program.py
# clear / cls
# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-05-15/?format=json

# A = kursy średnie
# B = kursy zakupu/sprzedaży

# 1. wziąć z Castoramy skrzynkę z narzędziami (m.in. z wiertarką)
# 2. wyciągnąć wiertarkę ze skrzynki i położyć na biurku
# 3. użyć wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "092/A/NBP/2023",
#             "effectiveDate": "2023-05-15",
#             "mid": 4.1490
#         }
#     ]
# }

from requests import get
import tkinter as tk
from tkinter import *
import datetime

actual_time = datetime.date.today()
actual_weekday = actual_time.weekday()


# funkcja pobierania i wyświetlania aktualnego kursu waluty euro


def euro_currency():
    waluta = 'EUR'
    if actual_weekday == 5:
        dzien = actual_time - datetime.timedelta(days=1, hours=1)
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")

    elif actual_weekday == 6:
        dzien = actual_time - datetime.timedelta(days=2, hours=1)
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")

    else:
        dzien = actual_time
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")


def usd_currency():
    waluta = 'USD'
    if actual_weekday == 5:
        dzien = actual_time - datetime.timedelta(days=1, hours=1)
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")

    elif actual_weekday == 6:
        dzien = actual_time - datetime.timedelta(days=2, hours=1)
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")

    else:
        dzien = actual_time
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")


def funt_currency():
    waluta = 'GBP'
    if actual_weekday == 5:
        dzien = actual_time - datetime.timedelta(days=1, hours=1)
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")

    elif actual_weekday == 6:
        dzien = actual_time - datetime.timedelta(days=2, hours=1)
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")

    else:
        dzien = actual_time
        strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")
        dane = strona.json()
        kurs = dane["rates"][0]["mid"]
        general_info.config(text=f"1 {waluta} = {kurs} PLN w dniu {dzien}")


# create the window
currency_window = tk.Tk()
currency_window.geometry("500x200")
currency_window.title("Aktualne kursy walut")
currency_window.iconphoto(False, tk.PhotoImage(file="D:\Python\Waluty\Obrazki\icon.png"))
currency_window.resizable(False, False)

# Opis funkcjonalności programu
purpose = tk.Label(currency_window, text="Wybierz walutę, której chcesz poznać aktualy kurs",
                   borderwidth=3, font=('Times New Roman', 12))
purpose.pack()

work_text="Tutaj będzie wyświetlony kurs wybranej waluty"
general_info = tk.Label(currency_window, text=work_text, font=('Times New Roman', 14))
general_info.pack()

# Tworzenie obrazków walut
euro_sign = tk.PhotoImage(file="D:\Python\Waluty\Obrazki\Euro.png")
dolar_sign = tk.PhotoImage(file="D:\Python\Waluty\Obrazki\Dolar.png")
funt_sign = tk.PhotoImage(file="D:\Python\Waluty\Obrazki\GBP.png")

# Przycisk Euro
Euro_button = tk.Button(currency_window, image=euro_sign, command=euro_currency)
Euro_button.pack(side=BOTTOM)
Euro_button.place(x=10, y=90)

# Przycisk Dolar
Dolar_button = tk.Button(currency_window, image=dolar_sign, command=usd_currency)
Dolar_button.pack(side=BOTTOM)
Dolar_button.place(x=200, y=80)

# Przycisk Funt Brytyjski
Funt_button = tk.Button(currency_window, image=funt_sign, command=funt_currency)
Funt_button.pack(side=BOTTOM)
Funt_button.place(x=380, y=80)

currency_window.mainloop()
