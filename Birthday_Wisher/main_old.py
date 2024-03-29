import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

my_email = ""
password = ""

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: Motivation quote\n\n{quote}")

