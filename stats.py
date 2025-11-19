def count_words(book_text):
    book_words = book_text.split()
    return len(book_words)

def count_characters(book_text):
    book_lower_case = book_text.lower()
    #book_characters = " ".join(book_lower_case)       #removes the spaces between the words
    #book_characters = book_characters.split()         #creates a list with each character but without the spaces
    book_characters = list(book_lower_case)
    book_character_dictionary = {}
    for book_character in book_characters:
        if book_character not in book_character_dictionary:
            book_character_dictionary[book_character] = 1
        else:
            book_character_dictionary[book_character] += 1
    return book_character_dictionary

def character_expansion(counted_characters):
    expanded_counted_characters = []
    for counted_character in counted_characters:
        expanded_counted_characters_dictionary = {}
        expanded_counted_characters_dictionary["char"] = counted_character
        expanded_counted_characters_dictionary["num"] = counted_characters[counted_character]
        expanded_counted_characters.append(expanded_counted_characters_dictionary)
    expanded_counted_characters.sort(reverse=True, key=sorted_list)
    return expanded_counted_characters

def sorted_list(expanded_counted_characters):
        return expanded_counted_characters["num"]

