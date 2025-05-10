def find_global_max(arr):
    # Initialize current_max with first element
    current_max = arr[0]
    
    # Iterate through array starting from second element
    for i in range(1, len(arr)):
        if arr[i] > current_max:
            current_max = arr[i]
    
    return current_max


# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([3, 7, 1, 9, 4, 6], "Global max from mixed positive array"),
        ([-5, -2, -8, -1, -9], "Global max from all negative array"),
        ([-10, 0, 5, -3, 8], "Global max from mixed positive/negative array"),
    ]
    
    for arr, description in test_cases:
        result = find_global_max(arr)
        print(f"{description}: {result}")