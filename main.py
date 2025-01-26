def main():
    path = "books/frankenstein.txt"
    file_content = read_file(path)
    print(count_character(file_content))
    


def read_file(path):
    with open(path)as f:
        return f.read()

def count_word(file_content):
    new_list = file_content.split()
    return len(new_list)

def count_character(file_content):
    new_string = file_content.lower()
    new_dict = {}
    for i in new_string:
        if i not in new_dict:
            new_dict[i]=1
        else:
            new_dict[i]+=1
    return new_dict



main()
