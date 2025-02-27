def linear_search(numbers, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0
   
    for i in range(len(numbers)):
        comparisons = comparisons + 1
        if (numbers[i] == key):
           return i, comparisons
    return -1, comparisons # not found

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