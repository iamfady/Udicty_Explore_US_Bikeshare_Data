import time
import pandas as pd
#import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#print('chicago')
#df = pd.read_csv('chicago.csv')
#print(df.columns)

#print('new_york_city')
#df = pd.read_csv('new_york_city.csv')
#print(df.columns)

#print('washington.csv')
#df = pd.read_csv('washington.csv')
#print(df.columns)




MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june','all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #print('Hello! Let\'s explore some US bikeshare data!')
    print('\n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city= ""
    
    
    while city not in CITY_DATA.keys():
        print('_'*40)
        print("\n")

        print("\nWelcome to the program that give you statistics for US Bikeshare Data :")
        print('*'*70)

        print("\nPlease Choose The City:")
        print("\n1. Chicago \t 2. New York City \t 3. Washington")
        print("\n You can write only the first letter, the side number, or the whole word ")


        user_input = str(input().lower())

        if user_input == "1" or user_input == "c" or user_input == "chicago":
            city = "chicago"
            print(f"\nYou have chosen:  {city.title()}." )


        elif user_input == "2" or user_input == "n" or user_input == "new york city":
            city = "new york city"
            print(f"\nYou have chosen:  {city.title()}." )


        elif user_input == "3" or user_input == "w" or user_input == "washington":
            city = "washington"
            print(f"\nYou have chosen:  {city.title()}." )

        else: 
            print("\nSorry.. check your input, You have specified the city name incorrectly")
            print("\nTry Again...")


    # TO DO: get user input for month (all, january, february, ... , june)

    month = ""
    
    while month not in MONTH_DATA:

        print("\n enter the month:")
        print("\n1. January \t2. February \t3. March \t4.April \t5. May \t6. June \t7.All")
        print("\n You can write only the first 3 letters, the side number, or the whole word ")


        user_input = str(input().lower())

        if user_input == "1" or user_input == "jan" or user_input == "january":
            month = "january"
            print(f"\nYou have chosen {month.title()}.")


        elif user_input == "2" or user_input == "feb" or user_input == "february":
            month = "february"
            print(f"\nYou have chosen {month.title()}.")


        elif user_input == "3" or user_input == "mar" or user_input == "march":
            month = "march"
            print(f"\nYou have chosen {month.title()}.")
            
        elif user_input == "4" or user_input == "apr" or user_input == "april":
            month = "april"
            print(f"\nYou have chosen {month.title()}.")
            
        elif user_input == "5"  or user_input == "may":
            month = "may"
            print(f"\nYou have chosen {month.title()}.")
            
        elif user_input == "6" or user_input == "jun" or user_input == "june":
            month = "june"
            print(f"\nYou have chosen {month.title()}.")
            
          
        elif user_input == "7" or user_input == "all":
            month = "all"
            print(f"\nYou have chosen {month.title()}.")
        else: 
            print("\nSorry.. check your input, You have specified the Month name incorrectly")
            print("\nTry Again...")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    
    
    day= ""

    
    while day not in DAY_DATA:

        print("\n enter the day:")
        print("\n1. Monday \t2. Tuesday \t3. Wednesday \t4.Thursday \t5. Friday \t6. Saturday \t7.Sunday \t8.All")
        print("\n You can write only the first 2 letters, the side number, or the whole word ")


        user_input = str(input().lower())

        if user_input == "1" or user_input == "ja" or user_input == "monday":
            day = "monday"
            print(f"\nYou have chosen {day.title()}.")


        elif user_input == "2" or user_input == "fe" or user_input == "tuesday":
            day = "tuesday"
            print(f"\nYou have chosen {day.title()}.")


        elif user_input == "3" or user_input == "we" or user_input == "wednesday":
            day = "wednesday"
            print(f"\nYou have chosen {day.title()}.")
            
        elif user_input == "4" or user_input == "th" or user_input == "thursday":
            day = "thursday"
            print(f"\nYou have chosen {day.title()}.")
            
        elif user_input == "5" or user_input == "fr" or user_input == "friday":
            day = "friday"
            print(f"\nYou have chosen {day.title()}.")
            
        elif user_input == "6" or user_input == "sa" or user_input == "saturday":
            day = "saturday"
            print(f"\nYou have chosen {day.title()}.")
        
        elif user_input == "7" or user_input == "su" or user_input == "sunday":
            day = "sunday"
            print(f"\nYou have chosen {day.title()}.")
            
          
        elif user_input == "8" or user_input == "al" or user_input == "all":
            day = "all"
            print(f"\nYou have chosen {day.title()}.")
        else: 
            print("\nSorry.. check your input, You have specified the Day name incorrectly")
            print("\nTry Again...")
    
   


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
    df['day_of_week'] = df['Start Time'].dt.day
    #weekday_name
    


    
   
    #df_cust['Start Time'] = df_cust.to_datetime(df_cust['Start Time'])    
    #df_cust['month'] = df_cust['Start Time'].dt.month
    #df_cust['day_of_week'] = df_cust['Start Time'].dt.weekday_name
    
    #print(df.head(3))
    
    

    
    return df 


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    popular_month = df['month'].mode()[0]
    print(f"Most Popular Month: {popular_month}")

    # TO DO: display the most common day of week
    print("-"*30)

    
    if  month == "all":
        popular_day = df['day_of_week'].mode()[0]
        print(f"\n Most Popular Day at ALL: {popular_day}.")

    else:
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        popular_day = df['day_of_week'].mode()[0]
        print(f"\n Most popular day at {month.title()}: {popular_day}.")

    
        
    

    

    # TO DO: display the most common start hour
    #Uses mode method to find the most popular hour

    print("-"*30)
    if day == "all" and month == "all":
        df['hour'] = df['Start Time'].dt.time
        popular_start_time = df['hour'].mode()[0] 
        print(f"\n Most Common Start Hour At All Months and All Days: {popular_start_time}.")

    
    elif day != "all" and month == "all":
        
        df = df[df['day_of_week'] == day.title()]             
       
        df['hour'] =  df['Start Time'].dt.time       
        popular_start_time = df['hour'].mode()[0] 
        print(f"\n Most Common Start Hour At ALL Months on {day}: {popular_start_time}.")
    
    
    
    elif day == "all" and month != "all":
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        df['hour'] =  df['Start Time'].dt.time       
        popular_start_time = df['hour'].mode()[0] 
        print(f"\n Most Common Start Hour At  {month} on All days: {popular_start_time}.")
    
    
    
    elif day != "all" and month != "all":
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        df = df[df['day_of_week'] == day.title()]  
        df['hour'] =  df['Start Time'].dt.time       
           
        popular_start_time = df['hour'].mode()[0]                    
        print(f"\n Most Common Start Hour At {month} on {day}: {popular_start_time}.")
    

    
    
    




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    print("-"*30)
    if day == "all" and month == "all":
        popular_start_Station = df['Start Station'].mode()[0] 
        print(f"\n Most Common Start Station At All Months and All Days: {popular_start_Station}.")
    
    
    elif day != "all" and month == "all":
        
        df = df[df['day_of_week'] == day.title()]             
       
        popular_start_Station = df['Start Station'].mode()[0] 

        print(f"\n Most Common Start Station At ALL Months on {day}: {popular_start_Station}.")
    
    
    
    elif day == "all" and month != "all":
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        df['hour'] =  df['Start Time'].dt.time       
        popular_start_Station = df['Start Station'].mode()[0] 
        print(f"\n Most Common Start Station At  {month} on All days: {popular_start_Station}.")
    
    
    
    elif day != "all" and month != "all":
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        df = df[df['day_of_week'] == day.title()]  
        popular_start_Station = df['Start Station'].mode()[0] 
           
        print(f"\n Most Common Start Station At {month} on {day}: {popular_start_Station}.")




    # TO DO: display most commonly used end station


    print("-"*30)
    if day == "all" and month == "all":
        popular_end_Station = df['End Station'].mode()[0] 
        group_field=df.groupby(['Start Station','End Station'])
        print(f"\n Most Common End Station At All Months and All Days: {popular_end_Station}.")
    
    
    elif day != "all" and month == "all":
        
        df = df[df['day_of_week'] == day.title()]             
        group_field=df.groupby(['Start Station','End Station'])
        popular_end_Station = df['End Station'].mode()[0] 
    
        print(f"\n Most Common End Station At ALL Months on {day}: {popular_end_Station}.")
    
    
    
  
    
    
    elif day == "all" and month != "all":
        
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        group_field=df.groupby(['Start Station','End Station'])
        popular_end_Station = df['End Station'].mode()[0] 
        print(f"\n Most Common End Station At  {month} on All days: {popular_end_Station}.")
    
    
    
    
    elif day != "all" and month != "all":
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        df = df[df['day_of_week'] == day.title()]  
        group_field=df.groupby(['Start Station','End Station'])
        popular_end_Station = df['End Station'].mode()[0] 
           
        print(f"\n Most Common End Station At {month} on {day}: {popular_end_Station}.")
    




    # TO DO: display most frequent combination of start station and end station trip
    print("-"*30)

    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df,month, day):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
        # TO DO: display total travel time
    
    print("-"*30)
    if day == "all" and month == "all":       
        total_travel_time = df['Trip Duration'].sum()
        print(f"\n Total Travel Time At All Months and All Days: {total_travel_time}")
            
        
        
    elif day != "all" and month == "all":
            
        df = df[df['day_of_week'] == day.title()]             
        total_travel_time = df['Trip Duration'].sum() 
        print(f"\n Total Travel Time At ALL Months on {day}: {total_travel_time}.")
        
            
        
            
    elif day == "all" and month != "all":
            
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        total_travel_time = df['Trip Duration'].sum()  
        print(f"\n Total Travel Time At  {month} on All days: {total_travel_time}.")
        
        
        
        
    elif day != "all" and month != "all":
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        df = df[df['day_of_week'] == day.title()]
        total_travel_time = df['Trip Duration'].sum()               
        print(f"\n Total Travel Time At {month} on {day}: {total_travel_time}.")
    



    # TO DO: display mean travel time








    print("-"*30)
    if day == "all" and month == "all":       
        mean_travel_time = df['Trip Duration'].mean()
        print(f"\n The Mean Travel Time At All Months and All Days: {mean_travel_time}")
            
        
        
    elif day != "all" and month == "all":
            
        df = df[df['day_of_week'] == day.title()]             
        mean_travel_time = df['Trip Duration'].mean() 
        print(f"\n The Mean Travel Time At ALL Months on {day}: {mean_travel_time}.")
        
            
        
            
    elif day == "all" and month != "all":
            
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        mean_travel_time = df['Trip Duration'].mean()  
        print(f"\n The Mean Travel Time At  {month} on All days: {mean_travel_time}.")
        
        
        
        
    elif day != "all" and month != "all":
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        df = df[df['day_of_week'] == day.title()]  
        mean_travel_time = df['Trip Duration'].mean()               
        print(f"\n The Mean Travel Time At {month} on {day}: {mean_travel_time}.")






    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,month,day,city):
   
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print("-"*30)
    if day == "all" and month == "all":       
        counts_user_types = df['User Type'].value_counts()
        print(f"\n The Counts of User Types At All Months and All Days: {counts_user_types}")
            
        
        
    elif day != "all" and month == "all":
            
        df = df[df['day_of_week'] == day.title()]             
        counts_user_types = df['User Type'].value_counts() 
        print(f"\n The Counts of User Types At ALL Months on {day}: {counts_user_types}.")
        
            
        
            
    elif day == "all" and month != "all":
            
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        counts_user_types = df['User Type'].value_counts()  
        print(f"\n The Counts of User Types At  {month} on All days: {counts_user_types}.")
        
        
        
        
    elif day != "all" and month != "all":
        df = df[df['month'] == MONTH_DATA.index(month) + 1]
        df = df[df['day_of_week'] == day.title()]  
        counts_user_types = df['User Type'].value_counts()               
        print(f"\n The Counts of User Types At {month} on {day}: {counts_user_types}.")




    # TO DO: Display counts of gender

    if city=="washington":
        print("Sorry, We Don't Have Data About The gender")
    else:
        print("-"*30)
        if day == "all" and month == "all":       
            counts_user_gender = df['Gender'].value_counts()
            print(f"\n The Counts of User Gender At All Months and All Days: {counts_user_gender}")
                
            
            
        elif day != "all" and month == "all":
                
            df = df[df['day_of_week'] == day.title()]             
            counts_user_gender = df['Gender'].value_counts() 
            print(f"\n The Counts of User Gender At ALL Months on {day}: {counts_user_gender}.")
            
                
            
                
        elif day == "all" and month != "all":
                
            df = df[df['month'] == MONTH_DATA.index(month) + 1]
            counts_user_gender = df['Gender'].value_counts()  
            print(f"\n The Counts of User Gender At  {month} on All days: {counts_user_gender}.")
            
            
            
            
        elif day != "all" and month != "all":
            df = df[df['month'] == MONTH_DATA.index(month) + 1]
            df = df[df['day_of_week'] == day.title()]  
            counts_user_gender = df['Gender'].value_counts()               
            print(f"\n The Counts of User Gender At {month} on {day}: {counts_user_gender}.")        



    # TO DO: Display earliest, most recent, and most common year of birth



    if city=="washington":
        print("Sorry, We Don't Have Data About The Year of birth")
    else:
        print("-"*30)
        if day == "all" and month == "all":       
            earliest = df['Birth Year'].min()
            most_recent = df['Birth Year'].max()
            most_common = df['Birth Year'].mode()[0]
            
            print("\n The Earliest, Most Recent, and Most Common Year of Birth At All Months and All Days:")
            print(f"\n The Earliest: {int(earliest)} , The Most Recent: {int(most_recent)} , The Most Common: {int(most_common)}")
                
            
            
        elif day != "all" and month == "all":
                
            df = df[df['day_of_week'] == day.title()]             
            earliest = df['Birth Year'].min()
            most_recent = df['Birth Year'].max()
            most_common = df['Birth Year'].mode()[0]            
            
            
            print(f"\n The Earliest, Most Recent, and Most Common Year of Birth At ALL Months on {day}:")
            print(f"\n The Earliest: {int(earliest)} , The Most Recent: {int(most_recent)} , The Most Common: {int(most_common)}")

                
            
                
        elif day == "all" and month != "all":
                
            df = df[df['month'] == MONTH_DATA.index(month) + 1]
            earliest = df['Birth Year'].min()
            most_recent = df['Birth Year'].max()
            most_common = df['Birth Year'].mode()[0]
           
            print(f"\n The Earliest, Most Recent, and Most Common Year of Birth At  {month} on All days:")
            print(f"\n The Earliest: {int(earliest)} , The Most Recent: {int(most_recent)} , The Most Common: {int(most_common)}")

            
            
            
        elif day != "all" and month != "all":
            df = df[df['month'] == MONTH_DATA.index(month) + 1]
            df = df[df['day_of_week'] == day.title()]  
            
            earliest = df['Birth Year'].min()
            most_recent = df['Birth Year'].max()
            most_common = df['Birth Year'].mode()[0]      
      
            print(f"\n The Earliest, Most Recent, and Most Common Year of Birth At {month} on {day}:")
            print(f"\n The Earliest: {int(earliest)} , The Most Recent: {int(most_recent)} , The Most Common: {int(most_common)}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_5_data(df,month,day):
    """how some rows of data upon request"""
        
    Response_list = ['yes', 'no']
    view_data = ''  
    start_loc = 0
    
    while view_data not in Response_list:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
        if view_data == "yes":
            
                        
            print("-"*30)
            if day == "all" and month == "all":       
                print(f"\n The Data At All Months and All Days: {df[:5]}")
                    
                
                
            elif day != "all" and month == "all":
                    
                df = df[df['day_of_week'] == day.title()]             
                print(f"\n The Data At ALL Months on {day}: {df[:5]}.")
                
                    
                
                    
            elif day == "all" and month != "all":
                    
                df = df[df['month'] == MONTH_DATA.index(month) + 1]
                print(f"\n The Data At  {month} on All days: {df[:5]}.")
                
                
                
                
            elif day != "all" and month != "all":
                df = df[df['month'] ==  MONTH_DATA.index(month) + 1]
                df = df[df['day_of_week'] == day.title()]  
                print(f"\n The Data At {month} on {day}: {df[:5]}.")
            
            
            
            
        elif view_data not in Response_list:
            print("INPUT DOSE NOT SEEM TO MATCH ANY OF THE ACCEPTED RESPONSES.")
    
    while view_data == 'yes':
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
        if view_data == 'yes':
            print(df[start_loc:start_loc+5])
        elif view_data == 'no':
            break
        else:           
            print("INPUT DOSE NOT SEEM TO MATCH ANY OF THE ACCEPTED RESPONSES.")
            view_data = input("Do you wish to continue?: ").lower()
            
            
            
            
    
    
    

def main():
    while True:
        city, month, day = get_filters()
        
        df= load_data(city, month, day)

        #time_stats(df)
        time_stats(df,month, day)

        station_stats(df,month, day)

        trip_duration_stats(df,month, day)
        user_stats(df,month,day,city)
        #UPDATE
        display_5_data(df,month,day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("See You Soon :)")
            break


if __name__ == "__main__":
	main()
