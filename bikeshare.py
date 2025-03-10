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
    
    
    while True:
        city = input("Which city? chicago, new york city or washington? ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Invalid answer. Please type again.")
            continue
        else:
            break
    


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
            
        month = input("Which month? all, january, february, ... , june? ").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Invalid answer. Please type again.")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day? all, monday, tuesday, ... , sunday? ").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Invalid answer. Please type again.")
            continue
        else:
            break


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
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    
    if day != 'all':
                df = df[df['day'] == day.title()]
                
       
                    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("the most common month :", popular_month)
                       


    # TO DO: display the most common day of week 
    popular_day = df['day'].mode()[0]
    print("the most common day :", popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("the most common start hour :", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("the most commonly used start station :", start_station)
                      


    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("the most commonly used end station :", end_station)


    # TO DO: display most frequent combination of start station and end station trip
    comb_station = df.groupby(['Start Station', 'End Station']).count()
    print("the most frequent combination trip :", "from", start_station, "to", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("total travel time :", total_travel_time)
                           


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time :", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
   

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    
    
    users_type = df['User Type'].value_counts()
    print("user types :", users_type)
    


    # TO DO: Display counts of gender
    try:
        gender_cnt = df['Gender'].value_counts()
        print("gender :", gender_cnt)
    
    except KeyError:
        print("no data is found")
       


    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        earliest_year = df['Birth Year'].min()
        print("the earliest year of birth :", earliest_year)
    except KeyError:
        print("no data is found")
    
    try:                        
        most_recent = df['Birth Year'].max()
        print("the most recent year of birth :", most_recent)
    except KeyError:
        print("no data is found")
    
    try:
        most_common = df['Birth Year'].value_counts().idxmax()
        print("the most common year of birth :", most_common)
    except KeyError:
        print("no data is found")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   
  


def ask_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no ").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
