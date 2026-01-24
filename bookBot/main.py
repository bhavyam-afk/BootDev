from stats import analytics1, characterCount, sortedChars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}...")

    content = get_book_text(book_path)

    print("---------- Word Count ----------")
    num_words = analytics1(content)
    print(f"Found {num_words} total words")

    char_map = characterCount(content)

    print("---------- Character Count ----------")
    sorted_chars = sortedChars(char_map)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("========== END ==========")



main()