class Contact_List:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contact_list(self):
        for contact in self.contacts:
            print(contact.name, "\t", contact.email, "\t", contact.telephone)
