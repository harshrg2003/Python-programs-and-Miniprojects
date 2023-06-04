def count_digit_occurrences(number):
    # Convert the number to a string for easier digit extraction
    number_str = str(number)

    # Initialize a list to store the counts of each digit
    digit_counts = [0] * 10  # Initialize with zeros for digits 0-9

    # Iterate over each digit in the number
    for digit in number_str:
        # Convert the digit to an integer and increment the corresponding count
        digit_counts[int(digit)] += 1

    # Return the list containing the counts
    return digit_counts


# Get the input number from the user
number = int(input("Enter a number: "))

# Call the function to count the digit occurrences
occurrences = count_digit_occurrences(number)

# Print the digit occurrences
print("Occurrences of each digit:")
for digit in range(10):
    print("Number of occurences of ",digit,"is",occurrences[int(digit)])