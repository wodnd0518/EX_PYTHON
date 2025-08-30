import pandas as pd
import datetime as dt
import random
import os
import smtplib

# Essential Parameters
MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "****"
FILE_PATH = './letter_templates/'

# 1. Update the birthdays.csv
df = pd.read_csv('./birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
month, day = dt.datetime.now().month, dt.datetime.now().day ## Today

is_hbd_today = (df['month'] == month) & (df['day'] == day)
names = df[is_hbd_today]['name'].tolist()
emails = df[is_hbd_today]['email'].tolist()

hbd_people = list(zip(names, emails))

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
file_list = os.listdir(FILE_PATH)

for name, email in hbd_people:
    picked_file = FILE_PATH + random.choice(file_list)
    with open(picked_file) as f:
        content = f.read()
    content = content.replace('[NAME]', name)

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:HAPPY BIRTHDAY {name}!!!\n\n{content}"
        )
    print(f"SUCCESS🟩 sent to {name} {email}")



