def find_strict_pivot(S):
    n = len(S)
    char_positions = {}

    # Record positions of each character in the string
    for i, char in enumerate(S):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)

    # Check each character's positions
    for char, positions in char_positions.items():
        if len(positions) == 2:  # Exactly twice
            start, end = positions
            if end - start > 1:  # At least one character between occurrences
                between_chars = S[start+1:end]
                if len(set(between_chars)) == len(between_chars):  # All unique
                    return char

    return -1

# Take input from the user
input_string = input()
print(find_strict_pivot(input_string))
