from ebook import EBook


def main():

    # Create a book
    my_book = EBook("Harry Potter", "J.K. Rowling", 300)

    # Open a book
    my_book.open()

    # Display book status
    my_book.show_status()

    # Read a few pages
    my_book.next_page()
    my_book.next_page()
    my_book.next_page()

    # Display book status
    my_book.show_status()

    # Close a book
    my_book.close()

    # Try to read a few pages
    my_book.next_page()
    my_book.next_page()


if __name__ == "__main__":
    main()
