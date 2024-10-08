import os

def main():
    print("Welcome to Book Bot!!")
    print("======================")
    print("")

    print("Here are a list of books you can choose:")
    books_list = os.listdir("./books")
    books = {}
    for file in books_list:
        name,extension = os.path.splitext(file)
        if file not in books:
            books[name] = {"ext":extension}
        print(f"{name}")
    book_name = input("Enter title of book:  ") 
    contents = ""
    file_extension = books[book_name]["ext"]
    if book_name == "frankenstein":
        with open(f"books/{book_name}{file_extension}") as b:
            contents = b.read()
        print(contents)
    else:
        print("Title not found!")
main()
