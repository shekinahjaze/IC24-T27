%%bash

grep -c "Certified" "/home/m262418/sd212/IC24/Data_Level3_GreenTerp - Cleaned.csv"

# output is 851 
# ratio is 851 / 10995

grep "Certified" "/home/m262418/sd212/IC24/Data_Level3_GreenTerp - Cleaned.csv" | grep -c "2022"
# 275

grep "Certified" "/home/m262418/sd212/IC24/Data_Level3_GreenTerp - Cleaned.csv" | grep -c "2023"
# 51
