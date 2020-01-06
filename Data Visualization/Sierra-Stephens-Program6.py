import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -----------------------------------
# CSCI 127, Joy and Beauty of Data  |
# Program 6: Data Visualization     |
# Sierra Stephens                   |
# Last Modified: April 26, 2019     |
# -----------------------------------
# This program visualy presents
# airline statistics
# -----------------------------------


# -----------------------------------
# This method displays in which
# months there are the most and least
# delays and how many delays there
# are in total
# -----------------------------------
def monthly_delays(file_name):
    # Read the file into a pandas dataframe
    df = pd.read_csv(file_name)
    file = open(file_name, "r")   # Open the file to read
    file.readline()
    # Create variables to be used later
    number_of_total_delays = 0
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    Oct = 0
    Nov = 0
    Dec = 0
    months = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
    # Give values to all the variables
    for line in file:
        split = line.split(",")
        number_of_total_delays += int(split[8])
        if split[19] == "January":
            months[0] += int(split[8])
        elif split[19] == "Febuary":
            months[1] += int(split[8])
        elif split[19] == "March":
            months[2] += int(split[8])
        elif split[19] == "April":
            months[3] += int(split[8])
        elif split[19] == "May":
            months[4] += int(split[8])
        elif split[19] == "June":
            months[5] += int(split[8])
        elif split[19] == "July":
            months[6] += int(split[8])
        elif split[19] == "August":
            months[7] += int(split[8])
        elif split[19] == "September":
            months[8] += int(split[8])
        elif split[19] == "October":
            months[9] += int(split[8])
        elif split[19] == "November":
            months[10] += int(split[8])
        elif split[19] == "December":
            months[11] += int(split[8])
        else:
            pass
    # Create a pandas dataframe
    df = pd.DataFrame({'Percentage of Delays Every Month': months}, index=['January','Febuary','March','April','May','June','July','August','September','October','November','December'])
    # Plot in the form of a pie chart
    plot = df.plot.pie(y='Percentage of Delays Every Month', figsize=(9,9), autopct='%.01f%%', colors=['b','y'])
    plt.title("Percentage of Delays Per Month\n" + "From a Total Number of " + str(number_of_total_delays) + " delays", bbox={'facecolor':'0.8', 'pad':5})
    plt.show()
    
# -----------------------------------
# This method displays a bar chart
# comparing the number of flights
# delayed and on time by the year
# the flights were scheduled
# -----------------------------------

def delays_vs_on_time(file_name):
    # Read the file into a pandas dataframe
    df = pd.read_csv(file_name)
    file = open(file_name, "r")   # Open the file to read
    file.readline()
    # Create variables to be used later
    delays = [0,0,0,0,0,0,0,0,0,0,0]
    on_time = [0,0,0,0,0,0,0,0,0,0,0]
    index = ['2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']
    # Give values to created variables
    for line in file:
        split = line.split(",")
        if int(split[-1]) == 2003:
            delays[0] += int(split[8])
            on_time[0] += int(split[-2])
        elif int(split[-1]) == 2004:
            delays[1] += int(split[8])
            on_time[1] += int(split[-2])
        elif int(split[-1]) == 2005:
            delays[2] += int(split[8])
            on_time[2] += int(split[-2])
        elif int(split[-1]) == 2006:
            delays[3] += int(split[8])
            on_time[3] += int(split[-2])
        elif int(split[-1]) == 2007:
            delays[4] += int(split[8])
            on_time[4] += int(split[-2])
        elif int(split[-1]) == 2008:
            delays[5] += int(split[8])
            on_time[5] += int(split[-2])
        elif int(split[-1]) == 2009:
            delays[6] += int(split[8])
            on_time[6] += int(split[-2])
        elif int(split[-1]) == 2010:
            delays[7] += int(split[8])
            on_time[7] += int(split[-2])
        elif int(split[-1]) == 2011:
            delays[8] += int(split[8])
            on_time[8] += int(split[-2])
        elif int(split[-1]) == 2012:
            delays[9] += int(split[8])
            on_time[9] += int(split[-2])
        elif int(split[-1]) == 2013:
            delays[10] += int(split[8])
            on_time[10] += int(split[-2])
        else:
            pass
    # Create pandas dataframe
    df = pd.DataFrame({'Delays': delays, 'On time': on_time}, index=index)
    # Plot a bar chart using the dataframe
    plot = df.plot.bar(title="Flights Delayed Compared to Flights On Time by Year",rot=0, color='by')
    plt.show()
        
def main(file_name):
    # delays_vs_on_time shows after monthly_delays is closed
    monthly_delays(file_name)
    delays_vs_on_time(file_name)

main("airlines.csv")
