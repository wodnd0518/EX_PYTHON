import smtplib
import datetime as dt
import random

MY_EMAIL = "wodnd0518@gmail.com"
MY_PASSWORD = "stcj pffr ettx duee"
SET_WEEKDAY = 5 ## Mon:0


def is_Saturday():
    if dt.datetime.now().weekday() == SET_WEEKDAY:
        return True


def pick_random_quote():
    with open('quotes.txt', 'r', encoding='utf-8') as f:
        quotes = f.readlines()
        quote = random.choice(quotes)
    return quote


def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Today's Quote\n\nHELLO, This Is Today's Quote.\n\n{quote}"
        )

if is_Saturday():
    send_email(pick_random_quote())