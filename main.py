import sys
from stats import get_num_words, character_count, character_report

# Check for correct number of command-line arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Use the provided path
filepath = sys.argv[1]

# Print the full report in the required format
print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(filepath)} total words")
print("--------- Character Count -------")

# Get and print the sorted character report
total_count = character_count(filepath)
sorted_report = character_report(total_count)
for item in sorted_report:
    print(f"{item['char']}: {item['num']}")

print("============= END ===============")