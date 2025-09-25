def get_book_text(file_path): 
    with open(file_path) as f: 
        return f.read()

def count_words(file_path):
    book = get_book_text(file_path) 
    return len(book.split())

def create_dict_entry(char,num): 
    entry = {
        "char": char,
        "num": num
    }
    return entry

def count_chars(file_path):
    book = get_book_text(file_path) 
    book_low = book.lower()
    book_set = set(book_low)
    char_dict = []
    for char in book_set:
        if char.isalpha():
            char_dict.append(create_dict_entry(char,book_low.count(char)))
    return char_dict

def sort_dict_helper(dict):
    return dict["num"]

def sorted_dict(file_path):
    dict1 = count_chars(file_path)
    dict1.sort(reverse=True, key=sort_dict_helper)
    return dict1

def print_report(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_path)} total words")
    print("--------- Character Count -------")
    dict1 = sorted_dict(file_path)
    for char in dict1:
        print(f"{char['char']}: {char['num']} ")

    print("============= END ===============")