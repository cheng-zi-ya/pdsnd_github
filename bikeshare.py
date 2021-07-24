import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITY_VALUE_LIST = ['new york city', 'chicago', 'washington']

FILTER_VALUE_LIST = ['month', 'day', 'both', 'none']

MONTH_VALUE_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_VALUE_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_value = input("\nWould you like to see data for Chicago, New York City, or Washington? \n")
    city_value.lower()
    
    while True:
        if city_value in CITY_VALUE_LIST:
            break
        else:
            city_value = input("\nPlease enter the city included--Chicago, New York City, or Washington: \n")
            city_value.lower()
    
    # make sure whether user want to filter uding month / day
    filter_value = input("\nWould you like to filter the data by month, day, both, or not at all? \n")
    filter_value.lower()
    
    while True:
        if filter_value in FILTER_VALUE_LIST:
            break
        else:
            filter_value = input("\nPlease enter the filter included--month, day, both, none: \n")
            filter_value.lower()
    
    
    # get user input for month (all, january, february, ... , june)  
    if filter_value == "none" or filter_value == "day":
        month_value = "all"
    else:
        month_value = input("\nWhich month - January, February, March, April, May, or June? \n")
        month_value.lower()

        while True:
            if month_value in MONTH_VALUE_LIST:
                break 
            else:
                month_value = input("\nPlease enter the month included:1-6, like january; or all: \n")
                month_value.lower()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_value == "none" or filter_value == "month":
        day_value = "all"
    else:
        day_value = input("\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n")
        day_value.lower()

        while True:
            if day_value in DAY_VALUE_LIST:
                break 
            else:
                day_value = input("\nPlease enter the month included:weekday, like Monday; or all: \n")
                day_value.lower()

    print('-'*40)
    return city_value, month_value, day_value


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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter month 
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    # filter day
    if day != "all":
        df = df[df['day_of_week'] == day.title()]
       
    return df


def display_data(df):
    """display raw data. Users could answer yes to continue look at next 5 lines of data and answer no to quit this function."""
    print_position = 0
    while True:
        display_value = input("\nWould you like to see raw data directly \n")
        display_value.lower()

        while True:
            if display_value in ['yes', 'no']:
                break
            else:
                display_value = input("\nPlease enter the command included--yes or no: \n")
                display_value.lower()

        if display_value == 'no':
            break
        else:
            print("\n" + df.iloc[print_position: print_position+5].to_string() + "\n")
            print_position += 5
            
    return 


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month: ", common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week: ", common_day)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ", common_end_station)

    # display most frequent combination of start station and end station trip
    df['Two Station'] = df['Start Station'] + ' -> ' + df['End Station']
    common_two_station = df['Two Station'].mode()[0]
    print("The most frequent combination of start station and end station trip: ", common_two_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time:", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time:", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df["User Type"].value_counts()
    print("The counts of user types: ", count_user_type)

    # Display counts of gender
    if "Gender" in df.columns.tolist():
        count_gender_type = df["Gender"].value_counts()
        print("The counts of gender: ", count_gender_type)

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns.tolist():
        early_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("The earliest year of birth: ", int(early_birth_year))
        print("The most recent year of birth: ", int(recent_birth_year))
        print("The most common year of birth: ", int(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
