from contact import Contact
from contact_list import Contact_List


# Create a contact list
my_contacts = Contact_List()

# Create contacts
contact1 = Contact("John Brown", "brown@onet.pl", "555234000")
contact2 = Contact("Anna May", "am@o2.pl", "232000199")
contact3 = Contact("George Small", "small@google.pl", "22299100")
contact4 = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")

# Add contacts to the list
my_contacts.add_contact(contact1)
my_contacts.add_contact(contact2)
my_contacts.add_contact(contact3)
my_contacts.add_contact(contact4)

# Display contact list
my_contacts.display_contact_list()
