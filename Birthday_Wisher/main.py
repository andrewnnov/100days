import smtplib
import datetime as dt


my_email = "xxxxxx"
password = "xxxxxx"


with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="xxxxxxxxxx",
                        msg="Subject:Hello\n\nThis is the body")

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
ms = now.microsecond
print(now)
print(year)
print(ms)

date_of_bith = dt.datetime(year=1952, month=12, day=22, hour=4)
print(date_of_bith)