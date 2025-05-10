# CSC249
# M4HW1 - Gold
# Susanna Quayle
# 5.10.2025

def binary_search(numbers, key):
    """Bronze level implementation - Binary search on user input numbers"""
    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts with entire range.
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
   
    # Loop until "low" passes "high"
    while (high >= low):
        # calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        if (numbers[mid] < key):
            low = mid + 1
      
        elif (numbers[mid] > key):
            high = mid - 1
      
        else:
            return mid   
   
    return -1  # not found


def binary_search_demo():
    # binary search func
    print("\n=== Binary Search Demo ===")
    
    # Get the numbers from user input
    print("Enter sorted numbers separated by spaces:")
    numbers_input = input().split()
    numbers = [int(x) for x in numbers_input]
    
    print('NUMBERS:', numbers)
    
    key = int(input('Enter an integer value: '))
    key_index = binary_search(numbers, key)
    
    if (key_index == -1):
        print('%d was not found.' % key)
    else:
        print('Found %d at index %d.' % (key, key_index))


def binary_guess_game():
    # binary guessing game
    print("\n=== Binary Guess the Number Game ===")
    print("Choose a number from 0 to 99, and I'll try to guess it!")
    print("Respond with '<' if your number is lower, '>' if higher, or '=' if correct.")
    
    low = 0
    high = 99
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts and low <= high:
        # Calculate middle point
        guess = (low + high) // 2
        attempts += 1
        
        # Ask user if this is their number
        print(f"Attempt {attempts}: Is your number {guess}?")
        response = input("Enter '<', '>', or '=': ").strip()
        
        if response == '=':
            print(f"I guessed your number {guess} in {attempts} attempts!")
            return
        elif response == '<':
            high = guess - 1
        elif response == '>':
            low = guess + 1
        else:
            print("Invalid input. Please enter '<', '>', or '='.")
            attempts -= 1  # Don't count invalid attempts
    
    if attempts >= max_attempts:
        print(f"I couldn't guess your number in {max_attempts} attempts!")
    else:
        print("Something went wrong - the search space is empty!")


def main():
    while True:
        print("\n=== Binary Search Programs ===")
        print("1. Binary Search Demo")
        print("2. Binary Guess the Number Game")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            binary_search_demo()
        elif choice == '2':
            binary_guess_game()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()