import os

# Function to load the library from a file
def load_library(filename="library.txt"):
    library = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                title, author, year, genre, read_status = line.strip().split("|")
                library.append({
                    "Title": title,
                    "Author": author,
                    "Publication Year": int(year),
                    "Genre": genre,
                    "Read Status": read_status == "True",
                })
    return library

# Function to save the library to a file
def save_library(library, filename="library.txt"):
    with open(filename, "w") as file:
        for book in library:
            file.write(
                f"{book['Title']}|{book['Author']}|{book['Publication Year']}|{book['Genre']}|{book['Read Status']}\n"
            )

# Function to display the menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Function to add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    library.append({
        "Title": title,
        "Author": author,
        "Publication Year": year,
        "Genre": genre,
        "Read Status": read_status,
    })
    print("Book added successfully!")

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Function to search for books
def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the title: ")
        results = [book for book in library if title.lower() in book["Title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ")
        results = [book for book in library if author.lower() in book["Author"].lower()]
    else:
        print("Invalid choice!")
        return

    if results:
        print("Matching Books:")
        for book in results:
            print(
                f"{book['Title']} by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Unread'}"
            )
    else:
        print("No matching books found.")

# Function to display all books
def display_all_books(library):
    if library:
        print("Your Library:")
        for book in library:
            print(
                f"{book['Title']} by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Unread'}"
            )
    else:
        print("Your library is empty.")

# Function to display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["Read Status"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

# Main function
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
