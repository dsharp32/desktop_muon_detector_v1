#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 00:57:24 2020

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

fname = input("Enter file name of the data to be plotted (eg. save_file.txt):")

df = pd.read_csv(fname, skiprows=7, sep = ' ', header=None)

df.columns = ['Comp_date', 'Comp_time', 'Event', 'Ardn_time(mS)', 'ADC_value[0-1023]', 'SiPM', 'Deadtime(mS)',]

df['Up_time'] = df['Ardn_time(mS)'] - df['Deadtime(mS)']

print(df)

x = df.Up_time
y = df.SiPM

stats = linregress(x, y)

m = stats.slope
b = stats.intercept

# Change the default figure size
plt.figure(figsize=(50,10))

# Change the default marker for the scatter from circles to x's
plt.scatter(x, y, marker = '.')

# Set the linewidth on the regression line to 3px
plt.plot(x, m * x + b, color="red", linewidth=3)

# Add x and y lables, and set their font size
plt.xlabel("Arduino Time mS", fontsize=20)
plt.ylabel("Amplitude mV", fontsize=20)

# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.savefig("run_11_2_20.png")

df.to_excel('/Users/user/Desktop/Study/Python/Muon Detector Data/muon_data.xlsx',
            sheet_name='UNSW_run_25_2_20')

