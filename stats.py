def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(filepath):    
    text = get_book_text(filepath)
    num_words = len(text.split())
    # old testing code, for reference only: print(f"Found {num_words} total words")  
    return num_words

def character_count(filepath):
    # Initialize empty dictionary
    total_count = {}
    text = get_book_text(filepath)
    text = text.lower()

    # Count occurrences of each character
    for ch in text:
        total_count[ch] = total_count.get(ch, 0) + 1
    return total_count

def character_report(char_counts):
    # Build list of dicts, skipping non-alphabetical characters
    report_list = []
    for ch in char_counts:
        if ch.isalpha():
            report_list.append({"char": ch, "num": char_counts[ch]})

    # Helper function for sorting by "num" key
    def get_num(item):
        return item["num"]

    # Sort from greatest to least
    report_list.sort(key=get_num, reverse=True)
    return report_list