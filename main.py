from stats import get_words_count, get_character_count, get_chars_info, print_alpha_chars
import sys

#Functions
def get_book_text(filepath: str) -> str:

    #Reading book data
    with open(filepath, encoding="utf-8") as file:
        read_data = file.read()

    return read_data





def main():

    if (len(sys.argv)) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...')
    book_data = get_book_text(sys.argv[1])
    
    print("----------- Word Count ----------")
    num_words = get_words_count(book_data)
    print(f'Found {num_words} total words')

    print("--------- Character Count -------")
    char_count = get_character_count(book_data)
    chars_list = get_chars_info(char_count)
    print_alpha_chars(chars_list)
    print("============= END ===============")

if __name__ == '__main__':
    main()