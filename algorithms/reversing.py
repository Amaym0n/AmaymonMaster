def reverse_in_place(array):      # Declare a function
    size = len(array)             # Get the length of the sequence
    hiindex = size - 1
    its = size//2                # Number of iterations required
    for i in range(0, its): # i is the low index pointer
        temp = array[hiindex] # Perform a classic swap
        array[hiindex] = array[i]
        array[i] = temp
        hiindex -= 1            # Decrement the high index pointer
    print("Done!")

# Now test it!!
array = [2, 5, 8, 9, 12, 19, 25, 27, 32, 60, 65, 1, 7, 24, 124, 654]

print(array)                    # Print the original sequence
reverse_in_place(array)        # Call the function passing the list
print(array)                    # Print reversed list