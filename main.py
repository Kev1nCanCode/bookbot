from stats import count_words, count_chars

def main():
    total_words = count_words("books/frankenstein.txt")
    print(f"Found {total_words} total words")

    print(count_chars("books/frankenstein.txt"))
main()
