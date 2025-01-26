def main():
    path = "books/frankenstein.txt"
    file_content = read_file(path)
    print(count_word(file_content))


def read_file(path):
    with open(path)as f:
        return f.read()

def count_word(file_content):
    new_list = file_content.split()
    return len(new_list)


main()
