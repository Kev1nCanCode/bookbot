def get_book_text(file_path): 
    with open(file_path) as f: 
        return f.read()

def count_words(book): 
    return len(book.split())

def main():
    book1 = get_book_text("books/frankenstein.txt")
    total_words = count_words(book1)
    return print(f"Found {total_words} total words")

main()
