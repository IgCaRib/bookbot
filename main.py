
def open_book(name):
    path_to_book = "./books/" + name + ".txt"
    with open(path_to_book) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    def sort_on(dict):
        return dict["num"]
    letter_count = {}
    list = []
    for letter in text:
        lt = letter.lower()
        if lt not in letter_count:
            letter_count[lt] = 0
        letter_count[lt] += 1
    for char in letter_count:
        temp = {"name": char, "num": letter_count[char]}
        list.append(temp)
    list.sort(reverse=True, key=sort_on)
    return list



def main(name):
    book = open_book(name)
    letter_count = count_chars(book)
    print(f"--- Begin report of {name} ---")
    print(f"{count_words(book)} words found in document")
    print("\n")
    
    for letter in letter_count:
        char = letter["name"]
        count = letter["num"]
        if char.isalpha() == True:
            print(f"The {char} character was found {count} times")

    print("--- End report ---")



if __name__ == "__main__":
    main("frankenstein")



