from stats import count_word
import sys


def read_file(path):
    with open(path)as f:
        return f.read()

def report_of_book(name,words,characters):
    print(f"--- Begin report of {name} ---")
    print(f"{words} words found in the document\n")
    for i in characters:
        if i.isalpha():
            print(f"{i}: {characters[i]}")
    print("--- End report ---")


def count_character(file_content):
    new_string = file_content.lower()
    new_dict = {}
    for i in new_string:
        if i not in new_dict:
            new_dict[i]=1
        else:
            new_dict[i]+=1
    return new_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        file_content = read_file(path)
        report_of_book(path,count_word(file_content),count_character(file_content))


main()
