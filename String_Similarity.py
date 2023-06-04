def calculate_string_similarity(string1, string2):
    # Convert the strings to sets of characters
    set1 = set(string1)
    set2 = set(string2)

    # Calculate the intersection and union of the character sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # Calculate the Jaccard similarity coefficient
    similarity_score = len(intersection) / len(union)

    return similarity_score

# Prompt the user to enter two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Calculate the string similarity
similarity_score = calculate_string_similarity(string1, string2)

# Display the similarity score
print("String Similarity Score:", similarity_score)