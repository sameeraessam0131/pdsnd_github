import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    month = ''
    day = '' 
    city = ''

    # Changes from refactoring branch 
    

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Would you like to see the data for chicago, new york city, or washington? ')
        city = city.lower()

        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Please Enter a valid input")

    while True: 
         
         selection = input('Would you like to filter the data by month, day, both, or not at all? (none = for all time) ')

         if selection in ['month', 'day', 'both', 'not at all', 'none']: 

            if selection == 'month':
                while True:
                    month = input('Which Month?  ')
                    if month in ['january', 'february', 'march', 'april', 'may', 'june', 'august', 'september', 'october'
                        'november', 'december', 'all', 'both', 'not at all']:
                        break
                    else: 
                        print('Please Enter a Valid Value...')
                break
            elif selection == 'day':
                while True: 
                    day = input('Which day? 1= Sunday? ')
                    if int(day) > 0 and int(day) < 8:
                        break
                    else:
                        print('Please enter a valid value...')
                break

            elif selection == 'both':
                while True:
                    month = input('Which Month? ')
                    if month in ['january', 'february', 'march', 'april', 'may', 'june', 'august', 'september', 'october'
                        'november', 'december', 'all', 'both', 'not at all']:
                        break
                    else: 
                        print('Please Enter a Valid Value...')
                while True: 
                    day = input('Which day? 1= Sunday? ')
                    if int(day) > 0 and int(day) < 8:
                        break
                    else:
                        print('Please enter a valid value...')
                break

            elif selection == 'not at all' or selection == 'none':
                break
            else:
                print('Please Enter a Valid Value...')
                


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day




def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    if month != '' and day != '':
        filter_methode = 'both'
    elif day != '': 
        filter_methode = 'day'
    elif month != '':
        filter_methode = 'month'
    elif month == '' and day == '':
        filter_methode = 'all'

    

    days_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month
    months = ['january', 'february', 'march', 'april', 'may', 'june']


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if filter_methode == 'both':

        month = months.index(month)+1
        # df = df.query('month == '+ str(month))
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == days_list[int(day)-1]]



    elif filter_methode == 'day':
        df = df[df['day_of_week'] == days_list[int(day)-1]]

    elif filter_methode == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november', 'december']
        month = months.index(month)+1
        df = df[df['month'] == month]

    elif filter_methode == 'all':
        pass


    



 

    







    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 
    'june', 'july', 'august', 'september', 'october','november', 'december']

    popular_month = df['month'].mode()[0]

    print('\nMost popular month is: ' + months[popular_month])


    # display the most common day of week

    common_day = df['day_of_week'].mode()[0]

    print('\nMost common week day is: ' + common_day)



    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost common hour: ' + str(popular_hour))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]

    print('\nMost common start station: ' + common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('\nMost common End station: ' + common_end_station)


    # display most frequent combination of start station and end station trip
    after_groupby = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending= False).idxmax
    print("most frequent combination of start station and end station trip: " + after_groupby(0)[0] + ' To ' + after_groupby(0)[1])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['TimeInterval'] = (df['End Time']- df['Start Time']).dt.seconds
    sum = df['TimeInterval'].sum()
    count = df['TimeInterval'].count()
    average = sum / count
    

    print('Total Time : '+ str(sum))
    print('Average time: '+ str(average))


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_row_data(df): 

    selction = input('Would you like to view 5 rows of individual trip data? Enter yes or no\n')

    counter = 1 
    while selction == 'yes':

        print(df[counter+1 : counter+6].to_string)
        selction = input('Do you wish to continue? yes or no ')
        if selction == 'no': 
            break
        elif selction == 'yes':
            counter = counter + 5
        else:
            print('Please enter a valid value...')








def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    if city != 'washington':
        # Display counts of gender
        gender = df['Gender'].value_counts()

        print(gender)


        # Display earliest, most recent, and most common year of birth

        df = df.sort_values(by = 'Birth Year', ascending=False)
    

    




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df







def main():
    while True:
        # get_filters()
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        df = user_stats(df, city)
        print_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
