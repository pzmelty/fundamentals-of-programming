import queue

# Create a queue
customers = queue.Queue()

# Ticket number
ticket_number = 1

while True:
    print("1. Add customer")
    print("2. Serve customer")
    print("0. Quit")

    menu = input("Select an option: ")

    if menu == "1":
        name = input("Enter customer name: ")

        # Add customer with ticket number
        customers.put((ticket_number, name))

        print("Your ticket number is:", ticket_number)

        ticket_number += 1

    elif menu == "2":
        if not customers.empty():
            ticket, name = customers.get()

            print("Serving customer:", name)
            print("Ticket number:", ticket)
        else:
            print("No customers in queue")

    elif menu == "0":
        break