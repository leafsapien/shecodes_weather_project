import csv
from datetime import datetime
# Use datetime for converting date & time - Google it

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"
# WOW that one was so easy, I am so *S* *M* *R* *T*  <https://www.youtube.com/watch?v=ls5BFzuxGw4> 


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.
    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string) #Converts string to datetime object
    Weekday = date.strftime("%A") #Extracts the weekday
    Date = date.strftime("%d") #Extracts the date day
    Month = date.strftime("%B") #Extracts the month
    Year = date.strftime("%Y") #Extracts the year
    return f"{Weekday} {Date} {Month} {Year}" #Returns all variables together in one line with space in between
# I like writing human readable code


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.
    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    # """
    temp = float(temp_in_fahrenheit) #Transforms temp_in_farenheit to float and assigns it to variable temp
    celsius = temp - 32 #Part one of mathematic conversion of farenheit to celsius
    celsius = celsius * 5 / 9 #Part two of mathematic conversion of farenheit to celsius, this was easier than figuring out the brackets
    return round(celsius, 1) #Returns result while also rounding down to one decimal point


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.
    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    count = len(weather_data) #Counts the amount of items in the list, to be used for mean calculation later
    sum = float(0) #Assigns an empty variable called sum, and makes it a float type
    for number in weather_data: #Creates a for loop for each item in the list, each item defined as number
        if number != "": # Skips any blank lines in the list
            sum += float(number) #During for each loop, manually adds each item in list and assigns total to sum while also converting to float type
    mean = sum / count #Calculates mean by dividing the sum of each item by the count of items
    return mean #Self explanatory
#This one was fun, I can't wait to see how everybody reached their answer!  I considered using the statistics mean module but decided to do it manually to practice my syntax.


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(file=csv_file) as csv_file: #This makes sure you are only opening and accessing the csv while this function is in use, so you don't have to close it later
        csv_reader = csv.reader(csv_file) # Making sure csv is in reading mode only, assigns variable to accessing the csv file using reader
        list_of_lists = [] #Create empty list to add each line list to during loop (Because it is a list of lists)
        for line in csv_reader: #For loop scanning each line in list
            if line != "": #Skips line if blank
                list = [] #Creates empty list for the line, reruns for each line
                list.append(line) #Appends each line created to the blank list created within the loop
    return list_of_lists
# I can't believe it, but I got this without any outside assistance (excluding referring to my notes and google for some syntax of course).  GO ME!  WOOT!

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    min_number = weather_data[0] #Assuming the first number is the smallest, by logic
    for number in weather_data: #Loop to scan each number in the list
        if number < min_number:  #Checking if each number next on the list is smaller than the previous
            min_number = number 
        else:
            return len(number in weather_data)
    return min_number


# list ** re-think
# 
# for each number in min column, compare to another number to see if smaller than the next?
# Also return index of position in the list
# ELSE condition to return index of last number on list
# ***Yeah, logic not greating on this one.  Will google it


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass
# Use the same function as above but opposite order, max over min lol


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
# totes combining all the functions above.  Will need to do this one second last.
# Goal is to basically obtain all results individually as var and return as a combined string.


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

# Same as above, totes combining all the functions.  Will need to do this one last.
# Goal is to basically obtain all results individually as var and return as a combined string.