import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Peg Rectangle Solitaire    |
# Sierra Stephens                       |
# Last Modified: April 12, 2019         |
# ---------------------------------------
# This program runs a model of the IQ
# tester game, Peg Solitaire 
# ---------------------------------------

# ---------------------------------------
# Start of PegRectangleSolitaire Class  |
# ---------------------------------------

class PegRectangleSolitaire:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1

# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " * |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|

    def game_won(self):
        """Determine if the user has won the game"""
        if self.pegs_left == 1:
            return True
        else:
            return False

    def final_message(self):
        """Return a final message for the user to see at end of game"""
        if self.pegs_left == 1:
            print("You're a genius!")
        elif self.pegs_left == 2:
            print("You're pretty smart.")
        elif self.pegs_left == 3:
            print("You're just average.")
        else:
            print("You're just plain dumb.")

    def legal_move(self, row_start, col_start, row_end, col_end):
        """Determine if a move is legal"""
        if self.board[row_end][col_end] == False and self.board[row_start][col_start]:
            if (abs(row_start - row_end) == 2) or (abs(row_start - row_end) == 0):
                if (abs(col_start - col_end) == 2) or (abs(col_start - col_end) == 0):
                    if self.board[(row_start + int((row_end - row_start) / 2))][(col_start + int((col_end - col_start) / 2))]:
                        return True
        return False
        
    def make_move(self, row_start, col_start, row_end, col_end):
        """Move the peg to a new destination"""
        self.board[row_start][col_start] = False
        self.board[row_end][col_end] = True
        self.board[(row_start + int((row_end - row_start) / 2))][(col_start + int((col_end - col_start) / 2))] = False
        self.pegs_left -= 1

# ---------------------------------------
# End of PegRectangleSolitaire Class    |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
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
    print("Welcome to Peg Rectangle Solitaire!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = PegRectangleSolitaire(rows, columns, row, column)
    print()

    keep_going = "yes"
    print(game)
    while (not game.game_won() and keep_going.lower() == "yes"):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)
        if not game.game_won():
            keep_going = input("Do you want to continue (yes or no): ")

    game.final_message()

# ---------------------------------------

main()
