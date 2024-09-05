#!/usr/bin/python3
import random
import os

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Minesweeper class, responsible for the game logic
class Minesweeper:
    # Constructor: initializes the board with dimensions and randomly placed mines
    def __init__(self, width=10, height=10, mines=10):
        self.width = width  # width of the board
        self.height = height  # height of the board
        # Mines are randomly placed using their linear index
        self.mines = set(random.sample(range(width * height), mines))
        # Create a 2D list for the game board, initially filled with empty spaces
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        # Keeps track of which cells are revealed
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    # Method to print the game board
    def print_board(self, reveal=False):
        clear_screen()  # clear the screen to provide a clean view
        # Print the top numbers representing column indices
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')  # print the row index at the start of each row
            for x in range(self.width):
                if reveal or self.revealed[y][x]:  # if reveal is True, show everything
                    # Check if current cell has a mine
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # print '*' for mines
                    else:
                        # Count the number of mines nearby and display it
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    # Print '.' for unrevealed cells
                    print('.', end=' ')
            print()  # move to the next line

    # Method to count the number of mines surrounding a cell
    def count_mines_nearby(self, x, y):
        count = 0
        # Check all surrounding cells in a 3x3 grid around (x, y)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy  # calculate neighbor coordinates
                # Ensure the neighbor is within the board bounds
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    # Convert (x, y) to a linear index and check if it contains a mine
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count  # return the total number of surrounding mines

    # Method to reveal a cell and possibly trigger a chain reaction for empty cells
    def reveal(self, x, y):
        # Check if the cell clicked is a mine
        if (y * self.width + x) in self.mines:
            return False  # return False to indicate the game is over (mine hit)
        
        self.revealed[y][x] = True  # mark the cell as revealed
        
        # If no mines are nearby, reveal the surrounding cells
        if self.count_mines_nearby(x, y) == 0:
            # Check all neighbors in a 3x3 grid
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy  # calculate neighbor coordinates
                    # Ensure neighbor is within bounds and not already revealed
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)  # recursively reveal surrounding cells
        return True  # return True if no mine was hit

    # Method to check if all non-mine cells are revealed (i.e., player wins)
    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                # If there are still unrevealed non-mine cells, return False
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    return False
        return True  # return True if all non-mine cells are revealed

    def play(self):
        while True:
            self.print_board()  # print the current state of the board
            try:
                # Ask the player to enter both coordinates, separated by a space
                coords = input("Enter x and y coordinates (separated by space): ")
                x, y = map(int, coords.split())  # split input and convert to integers

                # If a mine is revealed, the game ends
                if not self.reveal(x, y):
                    self.print_board(reveal=True)  # reveal all cells
                    print("Game Over! You hit a mine.")  # end message
                    safe_count = self.find_safe_cells()  # Get the count of remaining safe cells
                    print(f"Remaining safe cells: {safe_count}")  # Print the count of remaining safe cells
                    break  # exit the game loop

                # Check if the player has won the game
                if self.check_win():
                    self.print_board(reveal=True)  # reveal all cells
                    print("Congratulations! You have won the game.")  # win message
                    safe_count = self.find_safe_cells()  # Get the count of remaining safe cells
                    print(f"Remaining safe cells: {safe_count}")  # Print the count of remaining safe cells
                    break  # exit the game loop

            # Handle invalid input
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")

    # Method to find and print the number of remaining safe cells
    def find_safe_cells(self):
        safe_cells = []
        # Loop through all cells on the board
        for y in range(self.height):
            for x in range(self.width):
                # If the cell is not revealed and it's not a mine
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    safe_cells.append((x, y))  # Append the safe cell coordinates

        # Return the count of remaining safe cells
        return len(safe_cells)


# Run the game if this file is executed as a script
if __name__ == "__main__":
    game = Minesweeper()  # create a new Minesweeper game
    game.play()  # start playing
