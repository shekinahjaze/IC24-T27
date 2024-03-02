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

certified = df[df["GT_Participation"] == "Yes- Certified and received prize"]
print('ratio of people certified to people who signed up (all years):' , len(certified)/len(df))

# looking into how many frats and sororities participate in the program

greeklife = df[df["Form_Access"] == "Fraternity/Sorority Chapter Meeting"]
year2023 = df[df["AY"] == "2022-2023"]
year2022 = df[df["AY"] == "2021-2022"]
year2018 = df[df["AY"] == "2018-2019"]
greeklife2023 = year2023[year2023["Form_Access"] == "Fraternity/Sorority Chapter Meeting"]
print('greek life ratio in 2023:' , len(greeklife2023)/int(100))
greeklife2022 = year2022[year2022["Form_Access"] == "Fraternity/Sorority Chapter Meeting"]
print('greek life ratio in 2022:' , len(greeklife2022)/int(1130))
greeklife2018 = year2018[year2018["Form_Access"] == 'Fraternity/Sorority Chapter Meeting']
print('greek life ratio in 2018:' , len(greeklife2018)/int(1292))

# seeing who participates the most, off campus or on campus

housing = df[df["Housing"] == "On Campus (including South Campus Commons)"]
print('ratio of on campus housing to total participants:' , len(housing)/len(df))

# which hall participates the most

halls = df["Res-Hall"].value_counts()
print(halls)