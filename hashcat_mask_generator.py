def generate_password_patterns():
    # Step 1: Get input from the user
    words_input = input("Enter words (comma-separated): ").strip()
    num_placeholders = int(input("Enter the number of '?1' placeholders: ").strip())
    
    # Split the input words into a list
    words = [word.strip() for word in words_input.split(",")]
    
    # Step 2: Define the variations for each word
    def get_variations(word):
        return [
            word.lower(),          # Lowercase entire word
            word.upper(),          # Uppercase entire word
            word.capitalize(),     # Uppercase first letter, lowercase rest
            word[0].lower() + word[1:].upper()  # Lowercase first letter, uppercase rest
        ]
    
    # Step 3: Generate patterns for each word
    patterns = []
    for word in words:
        variations = get_variations(word)
        word_length = len(word)
        total_length = word_length + num_placeholders
        
        # Generate all possible placements of the word within the total length
        for variation in variations:
            for start_pos in range(total_length - word_length + 1):
                # Create the pattern with the word at the current position
                pattern = ["?1"] * total_length
                pattern[start_pos:start_pos + word_length] = list(variation)
                patterns.append("".join(pattern))
    
    # Step 4: Save patterns to a text file
    filename = "password_patterns.txt"
    with open(filename, "w") as file:
        for pattern in patterns:
            file.write(pattern + "\n")  # Write each pattern on a new line
    
    print(f"\nAll {len(patterns)} patterns have been saved to '{filename}'.")

# Run the function
generate_password_patterns()