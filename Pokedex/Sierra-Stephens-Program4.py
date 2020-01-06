import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Sierra Stephens                       |
# Last Modified: 14, 2019               |
# ---------------------------------------
# With a modified Pokedex, be able to run
# certain tasks based on user input
# ---------------------------------------

def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")
    print("")

class Pokemon:
    def __init__(self, name, number, combat_points, types):
        self.name = name
        self.number = number
        self.combat_points = combat_points
        self.types = types
    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
    def get_combat_points(self):
        return self.combat_points
    def get_types(self):
        return self.types
    def __str__(self):
        strings = ("Number: " + str(self.number) + ", " + "Name: " + self.name.capitalize() + \
               ", " + "CP: " + str(self.combat_points) + ": " + "Type: ")
        for item in self.types:
            strings += item
            if self.types.index(item) != (len(self.types) - 1):
                strings += (" and ")
        return(strings)

def print_pokedex(pokedex):
    print("The Pokedex")
    print("-----------")
    for pokemon in pokedex:
        print(pokemon)
def lookup_by_name(pokedex, name):
    found = False
    for i in pokedex:
        if name == i.get_name():
            print(i)
            found = True
    if found == False:
        print("There is no Pokemon named", name)
def lookup_by_number(pokedex, number):
    found = False
    for i in pokedex:
        if number == i.get_number():
            print(i)
            found = True
    if found == False:
        print("There is no Pokemon number", number)
def total_by_type(pokedex, pokemon_type):
    count = 0
    for i in pokedex:
        for n in i.get_types():
            if pokemon_type == n:
                count += 1
    print("Number of Pokemon that contain type", pokemon_type, "=", count)
def average_hit_points(pokedex):
    count = 0
    points = 0
    for i in pokedex:
        count += 1
        points += i.get_combat_points()
    average = points / count
    print("Average Pokemon combat points =", ('{0:.2f}'.format(average)))

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()
