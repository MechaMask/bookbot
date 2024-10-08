import os

def main():
    print("Welcome to Book Bot!!")
    print("======================")
    print("")

    print("Here are a list of books you can choose:")
    books = get_files_from_dir("./books")
    contents = ""
    while contents == "":
        book_title = input("\nPlease enter the title of a book:  ").lower()
        if book_title in books:
            file_extension = books[book_title]["ext"]
            content = read_book(f"./books/{book_title}{file_extension}")
            break
        else:
            print("Title not found!")
    print_report(content,book_title)

def get_files_from_dir(dir_path):
    items = os.listdir(dir_path)
    books = {}
    for file in items:
        if os.path.isfile(f"{dir_path}/{file}"):
            name,extension = os.path.splitext(file)
            if name not in books:
                books[name] = {"ext":extension}
            print(f"  - {name[0].upper()}{name[1:].lower()}")
    return books
def read_book(path):
    with open(path) as b:
        return b.read()
def print_report(text, title="book"):
    msg = []
    word_count = count_words(text)
    char_count = count_chars(text)
    msg.append(f"--- Begin report of {title} ---\n")
    if word_count == 1:
        msg.append(f"{word_count} word was ")
    else:
        msg.append(f"{word_count} words were ")
    msg.append(f"found in the document \'{title}\'\n\n")
    msg.append("character counts: \n")
    for item in char_count:
        if ord('a') <= ord(item) <= ord('z'): 
            msg.append(f"The character \'{item}\' appeared in {title} {char_count[item]} ")
            if char_count[item] != 1:
                msg.append("times\n")
            else:
                msg.append("time\n")
    msg.append("--- End report ---\n")
    msg = "".join(msg)
    print(msg)
def count_words(text):
    words = text.split()
    return len(words)
def count_chars(text):
    counts = {}
    for char in "".join(text.lower().split()):
        counts[char] = 1 + counts.get(char,0)
    return counts
main()
