# CSC 249
# recursion
# implementing algorithms iteratively (loops) or recursively (repeating functions)
# classic algos
# factoral vs. fibonacci series vs. binary search
# implement any two both iteratively and recursively


# zybooks 2.3 linear search
def linear_search(numbers, key):
    for i in range(len(numbers)):
       if (numbers[i] == key):
           return i
    return -1  # not found

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

# Main program to test the linear_search() method   
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer value: '))
key_index = linear_search(numbers, key)
     
if (key_index == -1):
    print('%d was not found.' % key)
else:
    print('Found %d at index %d.' % (key, key_index))

# Main program to test the binary_search() function   
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer value: '))
key_index = binary_search(numbers, key)
     
if (key_index == -1):
    print('%d was not found.' % key)
else:
    print('Found %d at index %d.' % (key, key_index))