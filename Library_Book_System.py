class Book:
    def __init__(self, title, author, isbn, year, genre):
        # Initialize a new Book object with core data and sets default availability.
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None
        
    def __str__(self):
        # Returns a cleanly formatted string layout of the detials using column width specifiers.
        return f"{self.title:<22} | {self.author:<20} | {self.isbn:<15} | {self.year} | {self.genre:<18} | {self.get_status()}"
    
    def check_out(self, patron_name):
        # Attempts to check out the book to a patron, returning True is successful or False if already checked out.
        if self.available:
            self.available = False
            self.borrower = patron_name
            return True
        else:
            return False
    def return_book(self):
        # Processes the return of the book, resetting availability and returning a confirmation string.
        self.available = True
        self.borrower = None
        return f"{self.title} has been returned and is now available for checkout."
    
    def get_status(self):
        # Returns a brief status string indicatiing availability or the current borrower.
        if self.available:
            return "Available"
        return f"Checked out by {self.borrower}"
    
# --- Main Program ---
if __name__ == "__main__":
    # Populate the collection list with 6 hardcoded Book objects
    collection = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925, "Fiction"),
        Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960, "Fiction"),
        Book("1984", "George Orwell", "9780451524935", 1949, "Dystopian"),
        Book("Pride and Prejudice", "Jane Austen", "9780141439518", 1813, "Romance"),
        Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", 1951, "Fiction"),
        Book("The Hobbit", "J.R.R. Tolkien", "9780547928227", 1937, "Fantasy")
    ]

    # 1. Display the full original collection
    print("\n--- Full Book Collection ---")
    for book in collection:
        print(book)
    print()

    # 2. Check out the first two books to different patrons
    print("--- Testing Checkouts ---")
    book1 = collection[0]
    book2 = collection[1]

    if book1.check_out("Alice"):
        print(f"{book1.title} has been checked out to Alice.")
    else:
        print(f"{book1.title} is already checked out.")
    if book2.check_out("Bob"):
        print(f"{book2.title} has been checked out to Bob.")
    else:
        print(f"{book2.title} is already checked out.")
    # 3. Attempt to check out the first book again (expecting failure_)
    if book1.check_out("Alex"):
        print(f"{book1.title} has been checked out to Alex.")
    else:
        print(f"{book1.title} is already checked out and cannot be checked out again.")
    # 4. Return the second checked-out book
    print("\n--- Testing Returns ---")
    print(book2.return_book())
    print()

    # 5. Display collection sorted by title (without mutating original list order)
    print("=== Sorted collection (By Title) ===")
    sorted_collection = sorted(collection, key=lambda b: b.title)
    for book in sorted_collection:
        print(book)

    # 6. Display only available books using a list comprehension
    print("\n=== Available Books ===")
    available_books = [book for book in collection if book.available]
    for book in available_books:
        print(book)     