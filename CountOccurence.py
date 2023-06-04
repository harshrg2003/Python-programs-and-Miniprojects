def count_characters(sentence):
    word_count = len(sentence.split())

    digit_count = 0
    uppercase_count = 0
    lowercase_count = 0

    for char in sentence:
        if char.isdigit():
            digit_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return word_count, digit_count, uppercase_count, lowercase_count


# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Count the characters
word_count, digit_count, uppercase_count, lowercase_count = count_characters(sentence)

# Display the results
print("Word count:", word_count)
print("Digit count:", digit_count)
print("Uppercase count:", uppercase_count)
print("Lowercase count:", lowercase_count)