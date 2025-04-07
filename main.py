import sys
from stats import *

def main():
    if not len(sys.argv) == 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    report = generate_report(sys.argv[1])
    print(report)

def generate_report(file_path):
    book_contents = get_book_text(file_path)
    word_count = get_book_word_count(book_contents)
    char_count = get_book_char_count(book_contents)
    sorted_char_count = sort_char_count(char_count)

    report = '============ BOOKBOT ============\n'
    report += f'Analyzing book found at {file_path}...\n'
    report += '----------- Word Count ----------\n'
    report += f'Found {word_count} total words\n'
    report += '--------- Character Count ------\n'

    for char in sorted_char_count:
        if char['char'].isalpha():
            report += f"{char['char']}: {char['count']}\n"

    return report

main()
