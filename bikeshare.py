import time
import pandas as pd
import numpy as np

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
    cities = ['chicago','new york city','washington']
    months = ["all",'january', 'february', 'march', 'april', 'may', 'june']
    days = ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    city = None
    month = None
    day = None
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in cities:
        city = str(input("Please enter city either chicago,new york city,washington:").lower())

    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in months:
        month = str(input('Pleas enter month in name eg "May" :').lower())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in days:
        day = str(input('Please enter day in name eg "saturday" :').lower())

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # display the most common day of week
    popular_dayOfweek = df['day_of_week'].mode()[0]
    print('Most Frequent day of week:', popular_dayOfweek)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:',start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:',end_station)
    
    # display most frequent combination of start station and end station trip
    df['Combined'] = df['Start Station'] + df['End Station']
    combined = df['Combined'].mode()[0]
    print('most combined:',combined)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df["Trip Duration"].sum()


    # display mean travel time
    mean_time = df["Trip Duration"].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_types = df["User Type"].value_counts()
    print("Number of User Type:", users_types)


    # Display counts of gender
    if 'Gender' in df:       
        genders = df["Gender"].value_counts()
        print("Number of Gender:", genders)
    else :
        print("no gender data")
    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        print("Earliest year of birth:",earliest_year_of_birth)
    
        #most recent year of birth
        recent_year_of_birth = df['Birth Year'].max()
        print("Recent year of birth:",recent_year_of_birth)
    
        #most common year of birth
        commonst_year_of_birth = df['Birth Year'].mode()[0]
        print("Commonst year of birth:",commonst_year_of_birth)



    
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    row = 0
    datas = df.iloc[row:row+5]
    get_raw_input = input("do you wanna see 5 raw data please enter yes or y if want or type any button for no:").lower()
    if get_raw_input == 'yes' or get_raw_input =='y':
        print(datas)
        new_raw = input("do you wanna see 5 raw data please enter yes or y if want or type any button for no:").lower()
        while new_raw == 'yes' or new_raw == 'y':
            row = row + 5
            datas = df.iloc[row:row+5]
            print(datas)
            new_raw = input("do you wanna see 5 raw data please enter yes or y if want or type any button for no:").lower()
            
            

                                 
        
        
    
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
