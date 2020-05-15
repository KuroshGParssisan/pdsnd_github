#References: Udacity, Stack Overflow.

import time as t
"""This program is called 'Explore US Bikeshare Data'. It allows us to query data from multiple files and apply filters and give statistics about the data."""
import datetime as dt
import pandas as pd
import numpy as np
from itertools import islice

#Dictionary with source data

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#Function to get the filters
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    print('\n')

    #Obtaining quality input and handling errors.

    while True:
        try:
            city = input('Select a city! (available cities: Chicago, New York City, Washington): ')
            city = city.lower()
            city = city.strip()
            if city == 'chicago' or city == 'new york city' or city == 'washington':
                break
            else:
                print('That is not a valid city!')
        except:
            print('That is not a valid city!')

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        try:
            month = input('Select a month! (available months: january, february, march, april, may, june or all): ')
            month = month.lower()
            month = month.strip()
            if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                break
            elif month == 'all':
                break
            else:
                print('That is not a valid month!')
        except:
            print('That is not a valid month!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            day = input('Select a day of the week! (available months: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all): ')
            day = day.lower()
            day = day.strip()
            if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
                break
            elif day == 'saturday' or day == 'sunday' or day == 'all':
                break
            else:
                print('That is not a valid day!')
        except:
            print('That is not a valid day!')

    print('-'*40)

    return(city, month, day)


#Function to load the data into a pandas DataFrame
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
    df.drop(['month', 'day_of_week'], axis = 1, inplace = True)

    return df

#Function to calculate the Time Stats
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['Monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month

    df['month'] = df['Start Time'].dt.month
    most_common_month_num = df['month'].value_counts().idxmax()
    most_common_month_name = months[most_common_month_num - 1]

    print('Most common month: ', most_common_month_name.title())

    # TO DO: display the most common day of week

    df['day_of_week'] = df['Start Time'].dt.weekday
    most_common_weekday_num = df['day_of_week'].value_counts().idxmax()
    most_common_weekday_name = days[most_common_weekday_num - 1]

    print('Most common day of the week: ', most_common_weekday_name.title())

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].value_counts().idxmax()

    print('Most common hour of the day: ', most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Function to calculate the Station Stats
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].value_counts().idxmax()

    print('Most commonnly used Start Station: ', most_common_start_station)

    # TO DO: display most commonly used end station

    most_common_end_station = df['End Station'].value_counts().idxmax()

    print('Most commonnly used End Station: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    most_common_start_and_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print('Most commonly used combination of Start and End Stations: ', most_common_start_and_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#Function to calculate the Trip Duration Stats
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()

    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()

    print('Mean travel time: ', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Function to calculate the User Stats
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type']
    user_types_count = user_types.value_counts()

    print('Count of user types: ')
    print(user_types_count.to_string(index = True))

    # TO DO: Display counts of gender

    try:
        print('\n')

        user_gender = df['Gender']
        user_gender_count = user_gender.value_counts()

        print('Count of gender: ')
        print(user_gender_count.to_string(index = True))
    except KeyError:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        print('\n')

        user_birth_year = df['Birth Year']
        user_recent_common_birth_year = user_birth_year.value_counts().idxmax()

        print('Most common recent year of birth: ', int(user_recent_common_birth_year))
    except KeyError:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Function to output raw data by chunks

def raw_data(city):
    counter = 0
    for chunk in pd.read_csv(city.replace(' ', '_') + '.csv', chunksize=5):
        if counter == 1:
            pass
        else:
            answer = input('\nDo you want to read the first 5 lines of raw data? Enter yes or anything else key to quit.\n')
        if answer.lower() == 'yes' or answer.lower() == 'y':
            if counter == 0:
                pass
            else:
                answer = input('\nDo you want to read the next 5 lines of raw data? Enter yes or anything else key to quit.\n')

            print('Showing raw data: ')
            print('\n')
            print(chunk)

            counter = 1
            continue
        else:
            break
#Main function
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #If there is no filtered data we ask the user to show the raw data:

        if month == 'all' and day == 'all':
            raw_data(city)
        else:
            print('If you want to see raw data select "all" in both month and day filters!')

        #We ask the user to restart the program

        restart = input('\nWould you like to restart the program? Enter yes or anything else key to quit.')
        if restart.lower() == 'yes' or restart.lower() == 'y':
            continue
        else:
            break

if __name__ == "__main__":
    main()
