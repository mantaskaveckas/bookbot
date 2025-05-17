import sys
from stats import get_num_words, get_num_chars, get_sorted_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    number_of_words = get_num_words(book_text)
    number_of_chars = get_num_chars(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for line in get_sorted_chars(number_of_chars):
        print(f"{line["char"]}: {line['num']}")
    print("============= END ===============")

main()
