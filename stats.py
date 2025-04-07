def get_book_text(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_book_word_count(book_contents):
    if not type(book_contents) == str:
        raise Exception('Type needs to be string')

    word_count = 0
    lines = book_contents.split('\n')

    for line in lines:
        for word in line.split(' '):
            if word == '':
                continue
            word_count += 1

    return word_count

def get_book_char_count(book_contents):
    if not type(book_contents) == str:
        raise Exception('Type needs to be string')

    char_count = {}
    for char in book_contents:
        lower_char = char.lower()
        if not lower_char in char_count:
            char_count[lower_char] = 1
        else:
            char_count[lower_char] += 1
    return char_count

def sort_char_count(char_dict):
    if not type(char_dict) == dict:
        raise Exception('Type needs to be dictionary')

    sorted_list = []
    def sort_on(dict):
        return dict['count']
    
    for char in char_dict:
        sorted_list.append({'char': char, 'count': char_dict[char]})
    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list

