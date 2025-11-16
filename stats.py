def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words():    
    num_words = 0
    text = get_book_text("books/frankenstein.txt")
    num_words = len(text.split())
    # print(f"Found {num_words} total words")
    return num_words

def character_count():
    # intialize varaible and dictionary
    total_count = {    }
    text = get_book_text("books/frankenstein.txt")
    text = text.lower()

    # Check if character is in dictionary
    # if not, add it
    # if it is, add to count for that character
    for ch in text:
        total_count.setdefault(ch, 0)
        total_count[ch] = total_count[ch] + 1

    return total_count
