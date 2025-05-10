def linear_search(numbers, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0
   
    for i in range(len(numbers)):
        comparisons = comparisons + 1
        if (numbers[i] == key):
           return i, comparisons
    return -1, comparisons

numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer key to search for: '))
print()

key_index, comparisons = linear_search(numbers, key)      
if (key_index == -1):
    print('Linear search: %d was not found with %d comparisons.' % (key, comparisons))
else:
    print('Linear search: Found %d at index %d with %d comparisons.' % (key, key_index, comparisons))
 