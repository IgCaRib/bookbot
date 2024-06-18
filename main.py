
def open_book(book):
    path_to_book = "./books/" + book + ".txt"
    with open(path_to_book) as f:
      return f.read()

def count_words(text):
   words = text.split()
   return len(words)


def main():
   test = open_book("frankenstein")
   print(count_words(test))


if __name__ == "__main__":
   main()
