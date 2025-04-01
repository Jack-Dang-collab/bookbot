from stats import get_num_words, get_character_counts, ordered_character_list
import sys

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_text = get_book_text(sys.argv[1])
    count = get_character_counts(book_text)
    list_count = ordered_character_list(count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for c in list_count:
      print(f"{c["character"]}: {c["num"]}")
    print("============= END ===============")

main()