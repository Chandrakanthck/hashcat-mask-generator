# Function to generate patterns based on the number of ?1s
def generate_patterns(words, mask):
    patterns = []
    for word in words:
        patterns.extend([
            f"{word}{mask}",
            f"{word.upper()}{mask}",
            f"{mask}{word}",
            f"{mask}{word.upper()}",
            f"?1{word}{mask[:-2]}",
            f"?1{word.upper()}{mask[:-2]}",
            f"?1?1{word}{mask[:-4]}",
            f"?1?1{word.upper()}{mask[:-4]}",
        ])
    return patterns

# Get user input for words and ?1 mask length
input_words = input("Enter words separated by commas: ").split(',')
input_words = [word.strip() for word in input_words]
mask_length = int(input("Enter the number of ?1 (e.g., 2, 3, 4): "))

# Generate mask pattern based on user input
mask = "?1" * mask_length
patterns = generate_patterns(set(input_words), mask)

# Save the patterns into a file
def save_patterns_to_file(patterns, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(patterns))

output_filename = f"Patterns_{mask_length}_Mask.txt"
save_patterns_to_file(patterns, output_filename)

print(f"Pattern file '{output_filename}' generated successfully!")

