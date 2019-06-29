import time
import pandas as pd
import numpy as np

#loading data files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

print("Welcome to the US Bikeshire Data exploration...!\n")

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
        city = input("Would you like to see data for what city : Chicago, New York City, or Washington ?\n").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Please, enter the name of the appropriate city.\n")
        else:
            break

     # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month (January, February, March, April, May, June) to filter by, or ''all'' to apply no month filter.\n").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Please, enter the apropriate value.\n")
        else:
            break

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day of week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) to filter by, or ''all'' to apply no day of weeke filter.\n").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Please, enter the apropriate value.\n")
        else:
            break
<<<<<<< HEAD


    print('-'*40)
||||||| merged common ancestors


    print('-'*40)
=======


    print('-'*45)
>>>>>>> 32fa352d804ccf8e6b0f77535a813c5a9c1c8c9f
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
    # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if possible
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # now filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if possible
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = months[df['month'].mode()[0] - 1]
    count_month = int(df['month'].value_counts()[df['month'].mode()[0]])
    print("\nThe most common month : {},    Count : {}.".format(common_month,count_month))

    # TO DO: display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    count_weekday = int(df['day_of_week'].value_counts()[0])
    print("\nThe most common day of week : {},    Count : {}.".format(common_weekday,count_weekday))

    # TO DO: display the most common start hour
    # extract hour from Start Time to create new column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    count_hour = int(df['hour'].value_counts()[0])
    print("\nThe most common start hour : {},    Count : {}.".format(common_hour,count_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    count_sstation = int(df['Start Station'].value_counts()[0])
    print("\nThe most common start station : {},    Count : {}.".format(common_sstation,count_sstation))

    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    count_estation = int(df['End Station'].value_counts()[0])
    print("\nThe most common end station : {},    Count : {}.".format(common_estation,count_estation))

    # TO DO: display most frequent combination of start station and end station trip
    freq_comb_station = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("\nThe most frequent combination of start satation and end station trip : {}.".format(freq_comb_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()

    count_duration = int(df['Trip Duration'].count())
    print("\nTotal duration : {} seconds,    Count : {},   Average Duration : {} seconds.".format(total_duration, count_duration, average_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


<<<<<<< HEAD

||||||| merged common ancestors

=======
>>>>>>> 32fa352d804ccf8e6b0f77535a813c5a9c1c8c9f
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("\nTypes of users (Suscribers, Customers) :\n {}.".format(count_user_type))

    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print("\nCount of gender among users :\n {}.".format(count_gender))
    except:
        print("Column ''GENDER'' not exist in the data source.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yb = int(df['Birth Year'].min())
        latest_yb = int(df['Birth Year'].max())
        common_yb = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth : {},  The latest year of birth : {},  The common year of birth : {}.".format(earliest_yb, latest_yb, common_yb))
    except:
        print("''BIRTH DATE'' data in not available for this periode.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)

def dsp_raw_data(df):

    """
    Loads raw data on user demande.
    Ask user to display raw databy sequence of five.
    """
    # drop all new coulums created after loading raw data
    df = df.drop(['month', 'day_of_week'], axis = 1)

    # initialize rows index
    rows_count = 0

    # get userimput for display raw data
    raw_data = input("\n Would you like to display raw data used to compute statistics ? Please write 'yes' or 'no' \n").lower()
    while True:
        if raw_data == 'no':
            return

        if raw_data == 'yes':
            print(df[rows_count: rows_count + 5])
            rows_count += 5

        raw_data = input("\n Would you like to see five more rows of the raw data used to compute the stats? Please write 'yes' or 'no' \n").lower()


def main():
    while True:
        # get the filters whitin the main function
        city, month, day = get_filters()

        # create  dataset with the filters
        df = load_data(city, month, day)

        # call statistics functions
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        dsp_raw_data(df)

        # restart or not
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
