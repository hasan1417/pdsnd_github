# import important libraries
import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            "Please enter the city name (chicago, new york city, washington): ").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Please enter a valid city name")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = list(calendar.month_name)
    month_list[0] = 'All'
    while True:
        month = input('Please enter the month name or all: ').capitalize()
        if month in month_list:
            break
        else:
            print('Please enter a valid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = list(calendar.day_name)
    day_list.append('All')
    while True:
        day = input('Please enter the day name or all: ').capitalize()
        if day in day_list:
            break
        else:
            print('Please enter a valid day')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month == 'All' and day != 'All':
        df = df[df['Start Time'].dt.day_name() == day]
    elif month != 'All' and day == 'All':
        df = df[df['Start Time'].dt.month_name() == month]
    elif month != 'All' and day != 'All':
        df = df[(df['Start Time'].dt.month_name() == month)
                & (df['Start Time'].dt.day_name() == day)]
    else:
        pass
    return df


def raw_data(df):
    while True:
        choice = input('Do you want to see raw data? ').lower()
        try:
            if choice == 'yes':
                increment = 0
                counter = + increment
                next_counter = 5 + increment
                print(df.loc[counter: next_counter])
                increment += 5
            elif choice == 'no':
                break
            else:
                print('Please enter a either yes or no')
        except:
            print('either you used invalid input or reached the end of the dataset')


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Start Time'].groupby(
        df['Start Time'].dt.month).agg({'count'}).idxmax()[0]
    print('most common month is ', common_month)

    # TO DO: display the most common day of week
    common_day = df['Start Time'].groupby(
        df['Start Time'].dt.day).agg({'count'}).idxmax()[0]
    print('most common day is ', common_day)

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].groupby(
        df['Start Time'].dt.hour).agg({'count'}).idxmax()[0]
    print('most common hour is ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].groupby(
        df['Start Station']).agg({'count'}).idxmax()[0]
    print('most common start station is: ', most_start_station)
    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].groupby(
        df['End Station']).agg({'count'}).idxmax()[0]
    print('most common end station is: ', most_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    most_combination = df.groupby(
        ['Start Station', 'End Station']).size().idxmax()
    print('most common combination  station are: ', most_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_time)
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].groupby(df['User Type']).agg({'count'})
    print(user_types)
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].groupby(df['Gender']).agg({'count'})
        print(gender_count)
    except KeyError:
        print('The Dataset does not have Gender Columm')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early = df['Birth Year'].min()
        print('the earliest year is: ', early)
        recent = df['Birth Year'].max()
        print('the most recent year is: ', recent)
        common_year = df['Birth Year']. value_counts(). idxmax()
        print('the most common year is: ', common_year)
    except KeyError:
        print('The Dataset does not have Birth Year Columm')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
