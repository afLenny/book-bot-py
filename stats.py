from collections import Counter


#Utility functions

def sort_dict(dict: dict):
    for value in dict.values():
        return value


#Stats functions

def get_words_count(data: str) -> int:
    words = data.split()
    return len(words)

def get_character_count(data: str) -> dict:
    text_lower = data.lower()
    return (dict(Counter(text_lower)))

def get_chars_info(char_dict: dict) -> list:
    char_list = []
    for key, value in char_dict.items():
        char_list.append({ key: value })
    char_list.sort(reverse=True, key=sort_dict)

    return char_list

def print_alpha_chars(char_list: list):
    for char_dict in char_list:
        for key, value in char_dict.items():
            if key.isalpha():
                print(f'{key}: {value}')
            else:
                continue