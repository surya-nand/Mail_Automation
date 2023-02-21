import smtplib
import datetime as dt
import random

your_email = "suryaanand10@gmail.com"
your_password = "hmeqczmthuatbzhl"
recipient_email = "hastagsurya10@gmail.com", "psrkgodavari@gmail.com"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        with open("quotes.txt") as quotes_data:
            quote_lines = quotes_data.readlines()
            quote = random.choice(quote_lines)
        connection.starttls()
        connection.login(user=your_email, password=your_password)
        connection.sendmail(
            from_addr=your_email, to_addrs=recipient_email,
            msg=f"subject:Monday Motivation\n\n{quote}"
        )