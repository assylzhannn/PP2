#Write a Python program to print yesterday, today, tomorrow.
from datetime import date, timedelta
"""tday=date.today()
yday=date.today()- timedelta(1)
print(yday)"""
def time():
    for i in range (-1,2):
        print(date.today()-timedelta(i))
        i=+1
time()