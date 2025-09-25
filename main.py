import sys
from stats import count_words, count_chars,print_report, sorted_dict, sort_dict_helper
#("books/frankenstein.txt"

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def main():
    print_report(f"{sys.argv[1]}")


main()
