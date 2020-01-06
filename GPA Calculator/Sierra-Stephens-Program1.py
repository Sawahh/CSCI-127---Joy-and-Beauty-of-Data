# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Sierra Stephens
# Last Modified: January 25, 2019 
# ---------------------------------------
# This program helps a student calculate
# their GPA
# ---------------------------------------

def grades (grade, credit):
    if grade == "A":
        points = (4.0 * credit)
    elif grade == "A-":
        points = (3.7 * credit)
    elif grade == "B+":
        points = (3.3 * credit)
    elif grade == "B":
        points = (3.0 * credit)
    elif grade == "B-":
        points = (2.7 * credit)
    elif grade == "C+":
        points = (2.3 * credit)
    elif grade == "C":
        points = (2.0 * credit)
    elif grade == "C-":
        points = (1.7 * credit)
    elif grade == "D+":
        points = (1.3 * credit)
    elif grade == "D":
        points = (1.0 * credit)
    else:
        points = 0.0
    return points

def main():
    courses = int(input("Enter the number of courses you are taking: "))
    gpa = 0.0
    total_credits = 0
    total_points = 0
    for course in range(courses):
        print("    ")
        grade = input("Enter grade for course " + str(course + 1) + ": ").capitalize()
        credit = int(input("Enter credits for course " + str(course + 1) + ": "))
        total_credits = total_credits + credit
        points = grades(grade, credit)
        total_points += points
    gpa = total_points / total_credits
    final_gpa = "{:.2f}".format(gpa)
    print("Your GPA is " + str(final_gpa))

main()
