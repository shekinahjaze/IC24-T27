# Sub question 1

# libraries we're using

import pandas as pd
import datetime

# Looking for how many total participants for all years of the program
df = pd.read_csv('Data_Level3_GreenTerp - Cleaned.csv')
print('total participants:' , len(df))

# splitting up the participation based on the years
yearcounts = df["AY"].value_counts()
print('2018-2019 participants: 4016')
print('2019-2020 participants: 3201')
print('2021-2022 participants: 3205')
print('2022-2023 participants: 573')

# seeing when people sign up the most (trends according to holidays/months)
df["Form Times"] = pd.to_datetime(df["Timestamp"], errors='coerce').dt.tz_localize(None)
print("months according to their participation\n" + str(df["Form Times"].dt.month.value_counts()))

# finding the ratio of how many people are certified to how many people signed up
# note: certified means completed 10 things to help the environment and signed up to get a prize
# https://sites.google.com/umd.edu/greenterp/home holds a lot of information for this program

