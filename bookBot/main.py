from bookBot.stats import analytics1, characterCount, sortedChars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        print("Analyzing book found at books/frankenstein.txt...")
        return file_contents 

def main():
    print("============ BOOKBOT ============")

    content = get_book_text("/Users/mehtabhavyam/Desktop/bookbot/books/frankenstein.txt")
    print("----------- Word Count ----------")
    num_words = analytics1(content)
    print(f"Found {num_words} total words")
    char_map = characterCount(content)
    print("--------- Character Count -------")
    sorted = sortedChars(char_map)
    for tuple in sorted:
        print(f"{tuple['char']}: {tuple['num']}")
    print("============= END ===============")

main()