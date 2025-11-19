import sys
from stats import count_words, count_characters, character_expansion , sorted_list

def get_book_text(f):
    with open(f) as book:
        buchinhalt = book.read()
        return buchinhalt

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    counted_words = count_words(book_text)
    counted_characters = count_characters(book_text)
    sorted_counted_characters = character_expansion(counted_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {counted_words} total words")
    print("--------- Character Count -------")
    for sorted_counted_character in sorted_counted_characters:
        if  sorted_counted_character["char"].isalpha() == True:
            print(f"{sorted_counted_character['char']}: {sorted_counted_character['num']}")
    print("============= END ===============")


main()