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
            if line != []: #Skips line if blank
                list_of_lists.append(line) #Appends each line created to the blank list created within the loop
    list_of_lists.pop(0) #pop removes the first item in the list
    for line in list_of_lists:  #Converts output to integers for use later
        line[1] = int(line[1])  #Converts column 2 (1 being second from 0) to integer.  This is required for future function use
        line[2] = int(line[2])
    return list_of_lists
# Complete initially without assistance, however an error occurred during later use when we combine all the functions together for use
# I added a section to convert column 1 & 2 in to integers to be easier for calculations later.


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    min_number = float(999) #Assigns maximum float value to min_number #Could instead convert string to float('inf')
    min_index = 0 #variable for counting the index of the min number as they are being checked
    if weather_data:  #ensures the list is not blank
        for index, number in enumerate(weather_data): #Loop to scan each number in the list while also counting index position
            if number: #Checks if number inside the list is not blank
                if float(number) < float(min_number):  #Checking if each number next on the list is smaller than the previous
                    min_number = float(number)  #Updates the minimum number
                    min_index = int(index)  #Updates the index number
                if float(number) == float(min_number):  #If number is equal, will instead update to the below
                    min_index = int(index)  #Updates the index number 
    if not weather_data: #If list is empty #Could add this at the top, as in if not weather data, then if everything else would proceed
        return ()  #Returns empty tuple
    return (min_number, min_index)  #Returns the minimum number while also converting to float and the index number
# Thank you for your help Ollie!  I got stuck on an index out of range error.


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    max_number = float(-999) #Assigns float value to max_number
    max_index = 0 #variable for counting the index of the max number as they are being checked
    if weather_data:  #ensures the list is not blank
        for index, number in enumerate(weather_data): #Loop to scan each number in the list while also counting index position
            if number: #Checks if number inside the list is not blank
                if float(number) > float(max_number):  #Checking if each number next on the list is larger than the previous
                    max_number = float(number)  #Updates the maximum number
                    max_index = int(index)  #Updates the index number
                if float(number) == float(max_number):  #If number is equal, will instead update to the below
                    max_index = int(index)  #Updates the index number 
    if not weather_data: #If list is empty #Could add this at the top, as in if not weather data, then if everything else would proceed
        return ()  #Returns empty tuple
    return (max_number, max_index)  #Returns the minimum number while also converting to float and the index number
# This is literally the same function as above, but I changed min to max


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    print(weather_data)
    print(weather_data[0])
    min_list = []  #Creates the empty lists to be used later
    max_list = []
    if not weather_data:  #Skips empty lines if empty
        pass  #Skips during loop
    for line in weather_data:  #For line in list
        if line:  #Skips any blank lines
            min_list.append (line[1])  #Intention is to add line of column to min list
            max_list.append (line[2])  #Intention is to add line of column to min list
    min_temp = format_temperature(convert_f_to_c(find_min(min_list)[0]))  #Calling the function to find min inside min list, while also converting to celsius and temp format
    max_temp = format_temperature(convert_f_to_c(find_max(max_list)[0]))  #Calling the function to find max inside max list, while also converting to celsius and temp format
    date_count = int(len(weather_data))  #Counts lines in provided list
    min_temp_date, min_temp_index = find_min(min_list) #Index number of min temp, run through date function
    min_temp_date = weather_data[min_temp_index][0] #Line 1 of obtaining the date - ISO String format
    min_temp_date = convert_date(min_temp_date)  #Line 2 - converting iso string in to readable format
    max_temp_date, max_temp_index = find_max(max_list) #Index number of max temp, run through date function
    max_temp_date = weather_data[max_temp_index][0] #Line 1 of obtaining the date - ISO String format
    max_temp_date = convert_date(max_temp_date)  #Line 2 - converting iso string in to readable format
    mean_min = format_temperature(convert_f_to_c(calculate_mean(min_list))) #Calculates mean of min list and converts to usable C temp format
    mean_max = format_temperature(convert_f_to_c(calculate_mean(max_list)))  #As above, but max
        
    return (
        f"{date_count} Day Overview\n"  # Best way to pull all the strings together not in one massive line
        f"  The lowest temperature will be {min_temp}, "  
        f"and will occur on {min_temp_date}.\n"  
        f"  The highest temperature will be {max_temp}, "  
        f"and will occur on {max_temp_date}.\n"  
        f"  The average low this week is {mean_min}.\n"  
        f"  The average high this week is {mean_max}.\n"  
    )
# The trickiest part about passing the test (after the code, obv) was getting the right amount of spaces in the text to pass the test parameters.

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    loops_combined = ""
    if not weather_data:  #Skips if line is empty at the start of the loop
        pass
    for line in weather_data:  #Iterates over each line in the data
        date_temp = convert_date(line[0])  #During each line loop returns date in first column, index 0.  Covnerts ISO date to human readable format.
        min_temp = format_temperature(convert_f_to_c(line[1]))  #During each line loop returns min temp in second column, index 1.  Also converts from f to c + and adds degree symbol.
        max_temp = format_temperature(convert_f_to_c(line[2]))  #During each line loop returns max temp in first column, index 2.  Also converts from f to c + and adds degree symbol.
        loops_combined += (  #Creates the following format for each iteration of data, returns it in a combined result line by line.
            f"---- {date_temp} ----\n"
            f"  Minimum Temperature: {min_temp}\n"
            f"  Maximum Temperature: {max_temp}\n"
            "\n")
    return loops_combined
# No comment, after the general summary the daily summary felt simple by comparison.
