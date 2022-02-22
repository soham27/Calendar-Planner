import datetime
import tkinter

####################################################################################
####################################################################################

# ENTERING THE CALENDAR PAGE

# We must obtain a few things:
# 1. Date, Day, Month, Year
# 2. Whether the year is a leap year
# 3. How many days in that month
# 4. Identified the days of the week depending on the month

##########################################

# Today's date

now = datetime.datetime.now()
date_today = now.strftime("%D")
# print(date_today)

day_today = date_today[3:5]
month_number_today = date_today[:2]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']

month_today = months[int(month_number_today) - 1]
year_today = '20' + date_today[6:]

##########################################

# Introducing the month and year for drawing the calendar

# If a specific date was selected for the calendar:
month = 'February'
year = '2000'

# If today's date was selected for the calendar:
# month = month_today
# year = year_today

##########################################

# Leap year identifier

is_leap_year = False

if int(year) % 4 == 0:
    is_leap_year = True
    if int(year) % 100 == 0:
        is_leap_year = False
        if int(year) % 400 == 0:
            is_leap_year = True
else:
    is_leap_year = False

# print(is_leap_year)

##########################################

# Number of days in the month

month_index = months.index(month)
number_of_days = month_days[month_index]

if month == 'February':
    if is_leap_year == True:
        number_of_days = '29'

# print(number_of_days)

# print('Today is ' + month + " " + day + " of " + year)

##########################################

# Next month button

# month = 'December'
if month == 'December':
    next_month = 'January'
    resulting_year = str(int(year) + 1)
    print('The next month is January ' + resulting_year)
else:
    next_month = months[month_index + 1]
    resulting_year = year
    print('The next month is ' + next_month + ' of ' + year)

# Button action opening next month's calendar with new values of month and year

##########################################

# Previous month button

# month = 'January'
if month == 'January':
    previous_month = 'December'
    resulting_year = str(int(year) - 1)
    print('The previous month is December ' + resulting_year)
else:
    previous_month = months[month_index - 1]
    resulting_year = year
    print('The previous month is ' + previous_month + ' of ' + year)

# Button action opening previous month's calendar with new values of month and year

##########################################
    
# Highlighting the cell having today's date

# if month == month_today and year == year_today:
    # Highlight today's cell having day_today

##########################################

# Identifying the days of the week depending on the month

#

####################################################################################
####################################################################################

# READING TASK INFO FROM CSV

##########################################

# Obtaining the task info cell from the CSV to fill out calendar dates

# Identifying the dates having existing tasks

##########################################

# Fill up a list containing all days having tasks

calendar_list = []
# Example: calendar_list = [[day1, day1_tasks], [day2, day2_tasks]]

# For each line in CSV:
    # if csv_month == month and csv_year == year:S
        # calendar_list.append([found_day, found_task_info])

##########################################

# Find out a way to display all tasks of all days on the monthly calendar

# for day in calendar_list:
    # Fill out task_info for the appropriate day

##########################################

# Obtaining all tasks for one date


task_info = 'Blue; STAB27: A1 due today|Red; LINA02: Quiz 3 today|White; GGRB32: Final exam today'

tasks_list = task_info.split('|')
print(tasks_list)

for task in tasks_list:
    colon_finder = task.find(';')
    task_desc = task[colon_finder + 2:]
    task_color = task[:colon_finder]
    # print('The task is "' + task_desc + '" colored ' + "'" + task_color + "'")

####################################################################################
####################################################################################

# ENTERING THE DATE ACTIONS PAGE

#

####################################################################################
####################################################################################

# ADDING A TASK

# We need to obtain:
# 1. Day, Month, Year
# 2. Raw Task Info

##########################################

color_entered = 'White'
name_entered = 'EESA11: Final exam today'
new_task = color_entered + "; " + name_entered
# print(new_task)

# task_info = task_info + "|" + new_task
# print(task_info)

# Button action to update the new task_info into CSV

####################################################################################
####################################################################################

# EDITING A TASK

# We need to obtain:
# 1. Day, Month, Year
# 2. Raw Task Info

##########################################

# Assigning the tasks list

tasks_list = task_info.split('|')
# print(tasks_list)

##########################################

# Framing the edited task

task_selected = 'White; GGRB32: Final exam today'
new_task_color = 'Whit'
new_task_name = 'GG: Done'
new_task_string = new_task_color + "; " + new_task_name
# print(new_task_string)

##########################################

# Updating the task info

task_index = tasks_list.index(task_selected)
tasks_list[task_index] = new_task_string

task_info = ''

for task in tasks_list:
    if task_info == '':
        task_info = task
    else:
        task_info = task_info + '|' + task

# print(task_info)

# Button action to update the new task_info into CSV

####################################################################################
####################################################################################

# DELETING A TASK

# We must obtain:
# 1. Day, Month, Year
# 2. Task Info

##########################################

# Assigning the tasks list

tasks_list = task_info.split('|')
# print(tasks_list)

##########################################

# Removing the task from the task list

task_selected = "Whit; GG: Done"
tasks_list.remove(task_selected)
task_info = ''

##########################################

# Updating the task list

for task in tasks_list:
    if task_info == '':
        task_info = task
    else:
        task_info = task_info + '|' + task

# print(task_info)

# Button action to update the new task_info into CSV

####################################################################################
####################################################################################

#












