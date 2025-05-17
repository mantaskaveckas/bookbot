def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}

    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_chars(chars):
    chars_list = []

    for char in chars:
        chars_list.append({
            "char": char,
            "num": chars[char]
        })

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
