def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---")

    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    print()

    dict_letters = count_letters_in_text(text)
    final_sorted_list= sorted_list_dict(dict_letters)

    for item in final_sorted_list:
        if not item["character"].isalpha():
            continue
        print(f"The '{item['character']}' character was found {item['num']} times")
    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    individual_words = text.split()
    return len(individual_words)

def count_letters_in_text(text):
    letter_count = {}
    for x in text:
        lowered = x.lower()
        if lowered in letter_count :
            letter_count[lowered] += 1
        else:
            letter_count[lowered] = 1
    return letter_count

def sorted_list_dict(dict_letters):
    dict_to_list = []
    for char in dict_letters:
        dict_to_list.append({'character': char, 'num' : dict_letters[char]})

    dict_to_list.sort(reverse = True, key=give_value_of_dict)
    return dict_to_list
    
def give_value_of_dict(d):
    return d['num']
    


    


    




main()