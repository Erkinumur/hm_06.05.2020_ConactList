import re

class ContactList(list):
    def search_by_name(self, name):
        result = list(filter(lambda x: re.search(name, x), self))
        return result

contacts = ContactList(["Ivan", 'Masha', 'Jenya', 'Ivan2', 'Ivan Popov'])
print(contacts.search_by_name('Ivan'))

