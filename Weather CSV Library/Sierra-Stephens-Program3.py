# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Weather CSV Library           |
# Sierra Stephens                          |
# Last Modified: March 1, 2019             |
# -----------------------------------------+
# Provides different statistics from a     |
# weather CSV library                      |
# -----------------------------------------+
    
def coldest_temperature(file_name):
    file = open(file_name, "r")
    minimum = 0
    file.readline()
    for line in file:
        split = line.split(",")
        list_min = int(split[-7])
        minimum = int(minimum)
        if list_min < minimum: 
            minimum = split[-7]
            city = split[1]
            state = split[6]
            date = split[4]
        if list_min == minimum:
            pass
        else:
            pass
    print("Coldest Fahrenheit temperature reading:", minimum)
    print("Location:", city, (state[1] + state[2]))
    print("Date:", date)


def average_temperature(file_name, location):
    file = open(file_name, "r")             
    file.readline()
    location = location.split(", ")
    user_city = str(location[0])
    user_city = user_city.lower()
    temperatures = 0
    count = 0                               
    for line in file:
        split = line.split(",")
        city = str(split[1])
        city = city.lower()
        if city == user_city:               
            count = count + 1
            temperatures += int(split[0])
    if count == 0:
        print("Number of readings: 0")
        print("Average temperature: Not Applicable")
    else:           
        print("Number of readings:", count)
        average = temperatures / count
        print("Average temperature:", (average - (average%.01)))
    

def all_stations_by_state(file_name, state):
    file = open(file_name, "r")
    file.readline()
    user_state = state
    user_state = user_state.lower()
    city_list = []
    for line in file:
        split = line.split(",")
        state = split[12]
        state = state.lower()
        if state == user_state and split[1] not in city_list:
            city_list.append(split[1])
        city_list.sort()
        list_count = int(len(city_list))
    if city_list == []:
        print("There are no recording stations")
    else:
        print("Recording Stations")
        print("------------------")
        for i in range(list_count):
            print((str(i+1) + ".").rjust(3), city_list[i])

def average_precipitation_by_state(file_name, state):
    file = open(file_name, "r")
    file.readline()
    precipitation = 0
    count = 0
    user_state = state
    user_state = user_state.lower()
    for line in file:
        split = line.split(",")
        state = split[12]
        state = state.lower()
        if state == user_state:
            precipitation += float(split[10])
            count += 1
        else:
            pass
    average = (precipitation / count)
    print("The average precipitation in", user_state.capitalize(), "is:", (average - (average%.01)))
        
    

# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+

def menu():
    print()
    print("1. Identify coldest temperature.")
    print("2. Identify average temperature for a given location.")
    print("3. Identify all recording station locations by state.")
    print("4. Something interesting, non-trivial and not a variation of the above options.")
    print("5. Quit.")
    print()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "weather.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            coldest_temperature(input_file)
        elif (choice == 2):
            location = input("Enter desired location (e.g. Miles City, MT): ")
            average_temperature(input_file, location)
        elif (choice == 3):
            state = input("Enter name of state (e.g. Montana): ")
            all_stations_by_state(input_file, state)
        elif (choice == 4):
            state = input("Enter name of state to calculate average precipitation(e.g. Montana): ")
            average_precipitation_by_state(input_file, state)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
