#!/usr/bin/python

amount = input('Enter the value of money you which to calulate your intrest of $: ')
rate = input ('Enter the rate in Percent: ')
years = input('Enter number of years: ')
intrest = float(amount) * (float(rate) / 100) * float(years)
print ('Intrest: ', intrest)
