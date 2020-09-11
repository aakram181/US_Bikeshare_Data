import time
import pandas as pd
import numpy as np
availmonths = ['january','february','march','april','may','june','july','all']
availcities = ['chicago','new york city','washington']
availdays = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Please enter city you want to explore (chicago, new york city, washington)").lower().strip()
        if city in availcities:
            break
        print("City entered invalid")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter month(s) you want to explore (all, january, february, ... , june)").lower().strip()
        if month in availmonths:
            break
        print("Month entered invalid")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter day(s) you want to explore").lower().strip()
        if day in availdays:
            break
        print("Day entered invalid")
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.day_name()

    # filter by month
    if month != 'all':
        #get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month) + 1
        # filter by month
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        # filter by day of week
         df =df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: {}'.format(availmonths[df['month'].mode()[0]-1].title()))

    # display the most common day of week
    print('Most common day of the week: {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    print('Most common hour: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most commonly used end startion is: {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station was : {}'.format((df['Start Station'] +' --AND-- '+df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    print('Total travel time is: {}'.format(df['Trip Duration'].sum()) + ' seconds')
    # display mean travel time
    print('Mean travel time is: {}'.format(df['Trip Duration'].mean()) + ' seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
   # df.fillna('NOT AVAIL', inplace= True)
    # Display counts of user types
    print('The count of each user type is: \n{}'.format(df['User Type'].value_counts().to_string()))

    #if city is washington return
    if city == 'washington':
        return

    # Display counts of gender
    print('The count of each gender is: \n{}'.format(df['Gender'].value_counts().to_string()))

    # Display earliest, most recent, and most common year of birth
    print('The earliest year of birth is: {}'.format(int(df['Birth Year'].min())))
    print('The most recent year of birth is: {}'.format(int(df['Birth Year'].max())))
    print('The most common year of birth is: {}'.format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
