def get_book_text(file_path): 
    with open(file_path) as f: 
        return f.read()

def count_words(file_path):
    book = get_book_text(file_path) 
    return len(book.split())

def count_chars(file_path):
    book = get_book_text(file_path) 
    book_low = book.lower()
    book_set = set(book_low)
    char_dict = {}
    for char in book_set:
        char_dict[char] = book_low.count(char)
    return char_dict