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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('put your desired city (chicago , new york city , washington): ').lower()
    while city not in CITY_DATA:
         city = input('TRY again, put your desired city (chicago , new york city , washington): ').lower()
            
    # TO DO: get user input for month (all, january, february, ... , june)
    months =  ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('choose a month from jan to june (or "all" for no filter) : ').lower()
    while month not in months: 
        month = input('Try again, choose a month from jan to june (or "all" for no filter) : ').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all' , 'monday' , 'tuesday' ,'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('type a day(sunday ,  monday...ect) or "all" for no filter :').lower()
    while day not in days:
        input('try again, type a day(sunday ,  monday...ect) or "all" for no filter : ').lower()
        

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    commonMonth = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Common month: ' , months[commonMonth-1])
    # TO DO: display the most common day of week
    commonDay = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  
    print('Most Common day: ' , days[commonDay])                                
    # TO DO: display the most common start hour
    commonHour = df['hour'].mode()[0]
    print('Most common hour: ' , commonHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonStation = df['Start Station'].mode()[0]
    print('Most common start station: ' , commonStation)

    # TO DO: display most commonly used end station
    commnonEnd = df['End Station'].mode()[0]
    print('Most common end station: ' , commnonEnd)

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost frequent combination of start station and end station trip:\n\n' , df.groupby(['Start Station' , 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    print('total travel time' , df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time: ' , df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts() , '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts() , '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest birth year:' , df['Birth Year'].min())
        print('Recent birth year: ' ,df['Birth Year'].max())
        print('Common birth year:' ,df['Birth Year'].mode()[0])
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        yes_no = ['yes' , 'no']
        inp = input('Do you want to check the first 5 rows of the dataset related to the chosen city? (yes or no): ').lower()
        while inp not in yes_no:
            inp = input('try again, "yes" for checking the first 5 rows and "no" for moving on:  ').lower()
        m , n = 0 , 5
        while True:
            if inp.lower() == 'yes':
                print(df.iloc[m : n])
                m +=5
                n +=5
                inp = input('\nWould you like to see more data? (yes or no): \n').lower()
                while inp not in yes_no:
                    inp = input('Please Enter Yes or No:\n').lower()
            else:
                break
                
        restart = input('\nWould you like to restart? (yes or no): .\n')
        if restart.lower() != 'yes':
            print('Hope to see you again!')
            break            


if __name__ == "__main__":
    main()
