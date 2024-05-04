import random
import time
import sys

# Constants
WIDTH = 20
HEIGHT = 10
SNAKE = [(WIDTH // 2, HEIGHT // 2)]
FOOD = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
DIRECTION = (1, 0)
SNAKE_CHAR = '#'
FOOD_CHAR = '*'
EMPTY_CHAR = '.'
LEVELS = {'E': 0.2, 'M': 0.1, 'H': 0.05}  # Speeds for Easy, Moderate, Hard

# Functions
def display_board(score):
    print("\n" + "=" * (WIDTH * 2 + 2))  # Top border
    for y in range(HEIGHT):
        print("|", end=" ")  # Side border
        for x in range(WIDTH):
            if (x, y) in SNAKE:
                print(SNAKE_CHAR, end=" ")
            elif (x, y) == FOOD:
                print(FOOD_CHAR, end=" ")
            else:
                print(EMPTY_CHAR, end=" ")
        print("|")  # Side border
    print("=" * (WIDTH * 2 + 2))  # Bottom border
    
    # Print score at top center
    padding = " " * ((WIDTH * 2 - len(str(score))) // 2)
    print("\n" + padding + f"Score: {score}")

def print_instructions():
    print("Welcome to the Snake Game!")
    print("Use the WASD keys to move the snake:")
    print("  - W: Move Up")
    print("  - A: Move Left")
    print("  - S: Move Down")
    print("  - D: Move Right")
    print("Eat the food (marked as *) to grow the snake.")
    print("Don't run into the walls or into yourself!")
    print("You can choose the level of difficulty at the beginning.")
    print("Enjoy the game!")

def move_snake(score):
    global SNAKE, DIRECTION, FOOD
    
    head = SNAKE[0]
    new_head = (head[0] + DIRECTION[0], head[1] + DIRECTION[1])
    
    if (new_head in SNAKE or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        print("Game Over! You collided with yourself or hit the wall.")
        print("Your final score is:", score)
        return False, score  # Game over
    
    SNAKE.insert(0, new_head)
    if new_head == FOOD:
        FOOD = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        score += 1  # Increase score when food is eaten
    else:
        SNAKE.pop()
        
    return True, score

def change_direction(new_direction):
    global DIRECTION
    
    if (DIRECTION[0] + new_direction[0] != 0 or
        DIRECTION[1] + new_direction[1] != 0):
        DIRECTION = new_direction

def select_level():
    while True:
        print("Select a level:")
        print("  - Easy (E)")
        print("  - Moderate (M)")
        print("  - Hard (H)")
        level = input("Enter your choice (E/M/H): ").upper()
        if level in LEVELS:
            return LEVELS[level]
        else:
            print("Invalid choice. Please select again.")

def ask_continue():
    while True:
        choice = input("Do you want to continue? (Y/N): ").upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print("Invalid choice. Please enter Y or N.")

# Main game loop
while True:
    choice = input("Do you want to play a snake game? Y for Yes and N for No: ").upper()
    if choice != 'Y':
        print("Exiting...\n")
        sys.exit()  # Exit the program
    print_instructions()
    score = 0  # Initialize score
    speed = select_level()
    while True:
        display_board(score)
        time.sleep(speed)
        direction = input("Enter direction WASD keys (W for up, A for left, S for down, D for right): ").upper()
        if direction == 'W':
            change_direction((0, -1))
        elif direction == 'A':
            change_direction((-1, 0))
        elif direction == 'S':
            change_direction((0, 1))
        elif direction == 'D':
            change_direction((1, 0))
            
        result, score = move_snake(score)
        if not result:
            if ask_continue():
                SNAKE.clear()
                SNAKE.append((WIDTH // 2, HEIGHT // 2))
                FOOD = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
                score = 0  # Reset score
            else:
                print("Exiting...\n")
                sys.exit()  # Exit the program