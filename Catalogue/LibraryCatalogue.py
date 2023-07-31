import time
print("Welcome to the DevOps Library Catalogue. Feel free to explore the service.")
time.sleep(1.5)
class LibraryCatalogue:
    def __init__(self):
        self.catalogue = {}
    def add_book(self, title, author, isbn):
        try:
            isbn = int(isbn)  # ISBN to integer
        except ValueError:
            print("ISBN should be a numerical value.")
            return
        time.sleep(1)
        if isbn in self.catalogue:
            print("Book with this ISBN already exists.")
        elif any(book['title'].lower() == title.lower() for book in self.catalogue.values()):
            print("Book with this title already exists.")
        else:
            self.catalogue[isbn] = {'title': title, 'author': author}
            print(f"'{title}' by {author} added to catalogue.")
    def search_book(self, title):
        time.sleep(1)
        found_books = []
        for isbn, book in self.catalogue.items():
            if title.lower() in book['title'].lower():
                found_books.append((isbn, book['title'], book['author']))
        return found_books
    def display_catalogue(self):
        time.sleep(1)
        if not self.catalogue:
            print("The catalogue is empty.")
        else:
            print("Catalogue:")
            print("{:<15} {:<40} {:<30}".format("ISBN", "Title", "Author"))
            print("="*85)
            for isbn, book in self.catalogue.items():
                print("{:<15} {:<40} {:<30}".format(isbn, book['title'], book['author']))
def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
def main():
    library = LibraryCatalogue()
    while True:
        print("\nLibrary Catalogue Menu:")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display Catalogue")
        print("4. Exit")
        choice = input("Enter your choice (1, 2, 3 or 4): ")
        if choice == '1':
            time.sleep(1)
            print("\nEnter book details:")
            title = input("Title: ")
            author = input("Author: ")
            isbn = get_positive_integer_input("ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == '2':
            time.sleep(1)
            search_title = input("Enter the title to search: ")
            found_books = library.search_book(search_title)
            if found_books:
                print("\nMatching books:")
                print("{:<15} {:<40} {:<30}".format("ISBN", "Title", "Author"))
                print("="*85)
                for isbn, title, author in found_books:
                    print("{:<15} {:<40} {:<30}".format(isbn, title, author))
            else:
                print("No matching books found.")
        elif choice == '3':
            time.sleep(1)
            library.display_catalogue()
        elif choice == '4':
            time.sleep(1)
            print("We're sorry to see you go, but we hope you visit again soon!")
            break
        else:
            print("Invalid choice. Please choose again.")
        time.sleep(2)  
if __name__ == "__main__":
    main()
