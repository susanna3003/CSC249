# CSC 249
# recursion
# implementing algorithms iteratively (loops) or recursively (repeating functions)
# classic algos
# factoral vs. fibonacci series vs. binary search
# implement any two both iteratively and recursively


# zybooks 2.3 binary search
def binary_search(numbers, key):
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
   
    return -1 # not found

def fibonacci_search(arr, key):
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = fib_minus_1 + fib_minus_2
    
    while fib < len(arr):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2

    offset = -1
    
    while fib > 1:
        i = min(offset + fib_minus_2, len(arr) - 1)
        
        if arr[i] < key:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            offset = i
        
        elif arr[i] > key:
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1
        
        # found key
        else:
            return i
    
    # key not found
    if fib_minus_1 and offset + 1 < len(arr) and arr[offset + 1] == key:
        return offset + 1
    
    return -1


# main program to test the binary_search() function 
print('BINARY SEARCH FUNCTION')  
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer value: '))
key_index = binary_search(numbers, key)
     
if (key_index == -1):
    print('%d was not found.' % key)
else:
    print('Found %d at index %d.' % (key, key_index))

# main to test fib
print('FIBONACCI SERIES SEARCH FUNCTION')
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer value: '))
key_index = fibonacci_search(numbers, key)
     
if (key_index == -1):
    print('%d was not found.' % key)
else:
    print('Found %d at index %d.' % (key, key_index))

# binary and fib search loop
while True:
    # Show options to the user
    print("\nLooped Search Options:")
    print("1. Binary Search")
    print("2. Fibonacci Search")
    print("3. Quit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '3':
        print("Exiting program. Goodbye!")
        break
    
    try:
        key = int(input('Enter an integer value to search for: '))
        
        if choice == '1':
            print("Using Binary Search (In-Loop Version)...")
            
            # implementing binary search in the loop
            low = 0
            high = len(numbers) - 1
            key_index = -1
            
            while (high >= low):
                mid = (high + low) // 2
                
                if (numbers[mid] < key):
                    low = mid + 1
                
                elif (numbers[mid] > key):
                    high = mid - 1
                
                else:
                    key_index = mid
                    break
            
            if (key_index == -1):
                print(f'{key} was not found in the list.')
            else:
                print(f'Found {key} at index {key_index}.')
                
        elif choice == '2':
            # fib looped search
            print("Using Fibonacci Search (In-Loop Version)...")
            
            # implementing fibonacci search in the loop
            fib_minus_2 = 0
            fib_minus_1 = 1
            fib = fib_minus_1 + fib_minus_2
            
            while fib < len(numbers):
                fib_minus_2 = fib_minus_1
                fib_minus_1 = fib
                fib = fib_minus_1 + fib_minus_2
            
            offset = -1
            key_index = -1
            
            while fib > 1:
                i = min(offset + fib_minus_2, len(numbers) - 1)
                
                if numbers[i] < key:
                    fib = fib_minus_1
                    fib_minus_1 = fib_minus_2
                    fib_minus_2 = fib - fib_minus_1
                    offset = i
                
                elif numbers[i] > key:
                    fib = fib_minus_2
                    fib_minus_1 = fib_minus_1 - fib_minus_2
                    fib_minus_2 = fib - fib_minus_1
                
                else:
                    key_index = i
                    break
            
            # Check the last element if needed
            if key_index == -1 and fib_minus_1 and offset + 1 < len(numbers) and numbers[offset + 1] == key:
                key_index = offset + 1
            
            if (key_index == -1):
                print(f'{key} was not found in the list.')
            else:
                print(f'Found {key} at index {key_index}.')
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            
    except ValueError:
        print("Error: Please enter a valid integer.")