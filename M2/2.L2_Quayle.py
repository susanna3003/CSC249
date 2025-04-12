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

# test with strings
values = ["Liam Lawson has crashed in the first practice session of the 2025 season.", "Max Verstappen sets out to win a 5th world championship with Redbull Racing", "Lewis Hamilton leaves Mercedes to join Ferrari, rivaling Charles Leclerc for the fight of World Champion in a Ferrari", "I am a huge dweeb who sucks at time management and cannot complete anything on time which unfortunately culminates in inadvertently taking advantage of my kindest most wonderful teacher's generosity and not turning in a single assignment on time :D"]
     
print('VALUES:', values)

# Input a value to search for (accepts any data type)
key = input('Enter a value to search for: ')

if len(key) != 1:
    print("Please enter exactly one character.")
else:
    found = False
    for i, string in enumerate(values):
        if key in string:
            print(f"Found '{key}' in string {i}: {string}")
            found = True

    if not found:
        print(f"Character '{key}' was not found in any string.")