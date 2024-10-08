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
    print(count_words(content))

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
def count_words(text):
    words = text.split()
    return len(words)

main()
