#!/usr/bin/env python

# glitch-time.py
# Python port of PHP Glitch calendar code from api.glitch.com/docs/time/
# August 26, 2011 by Janice Barlow Collier <jbarlow.smc@gmail.com>
# in-game: Coraline Ripley

# usage: glitch-time.py

from math import floor
import time


def get_month_and_day(input_day):

# what day of the year does each month end on?
    ends_on = [29, 32, 85, 102, 175, 194, 207, 244, 249, 296, 307, 308] 

# Primuary is a special case
    if input_day <= ends_on[0]:
        return 0, input_day

    month_number = 1
    day_number = 1

    for end in ends_on:
        # is this day past the end of the month?
        # if so, move to the next month
        if input_day > end:
            month_number = month_number + 1
        # the current day of the month is
        # the day of the year minus the day the *prior* month ends on
        day_number = input_day - (ends_on[month_number-1])
        return month_number, day_number

        
            
# Glitch epoch starts 5am UTC on April 4th, 2009

game_epoch = 1238562000

# Constants for conversion of real time to Glitchian time
# is a dict overkill? probably, but hey, they're all in one place

real_time = {'glitch_year':4435200, 'glitch_day':14400, 'glitch_hr':600, 'glitch_min':10}

glitch_months = ['Primuary','Spork', 'Bruise', 'Candy', 'Fever', 'Junuary', 'Septa', 'Remember', 'Doom', 'Widdershins', 'Eleventy', 'Recurse']
glitch_days = ['Hairday', 'Moonday', 'Twoday', 'Weddingday', 'Theday', 'Fryday', 'Standday', 'Fabday']


# ts contains current real-world time, in epoch format, at runtime
# equivalent to PHP $ts

ts = time.time()

# how many real seconds have elapsed since game epoch?

real_sec = ts - game_epoch


# convert real seconds to Glitch years

year = floor(real_sec / real_time['glitch_year'])
real_sec -= year * real_time['glitch_year']

# convert remaining real seconds to Glitch days

day_of_year = floor(real_sec / real_time['glitch_day'])
real_sec -= day_of_year * real_time['glitch_day']

# convert remaining real seconds to Glitch hours

hour = floor(real_sec / real_time['glitch_hr'])
real_sec -= hour * real_time['glitch_hr']

# convert remaining real seconds to Glitch minutes

minute = floor(real_sec / real_time['glitch_min'])
real_sec -= minute * real_time['glitch_min']


# convert the day of the year to a proper
# month number and day of month

month, day_of_month = get_month_and_day(day_of_year)


# figure day of week

days_since_epoch = day_of_year + (307 * year)
day_of_week = days_since_epoch % 8

# spit out results

print "It's %s, %s %s %02d:%02d in the year %s." % (glitch_days[int(day_of_week)], glitch_months[int(month)], int(day_of_month), int(hour), int(minute), int(year))
