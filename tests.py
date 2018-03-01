import unittest
""" importing testing libraries"""
from phone import Phone
"""importing phone class from phone.py """




class MyTest(unittest.TestCase):
    """importing testing library"""
    def test_delete_contact(self):
        """testing if deletion works"""
        dell = Phone()
        dell.create_contact('eve', 7079)
        dell.delete_contact('eve')
        deletion = True
        if str(7079) in str(dell.contact.get('eve')):
            deletion = False

        self.assertEqual(deletion, True)

def test_create_contact(self):
    """testing if create contact works"""
    create = Phone()
    create.create_contact('kelvin', 0707)
    if create.contact.get('kelvin') == 0707:
        creation = True

    self.assertEqual(creation, True)

def test_update_contact(self):
    """testing if updating contact works"""
    edit = Phone()
    edit.create_contact('miano', 900)
    edit.update_contact('miano', 900, 'trisha', 8000)
    update = False
    if str(900) not in str(edit.contact.get('miano')):
        if 'trisha' in edit.contact.keys():
            update = True

    self.assertEqual(update, True)

def test_check_no_duplicates(self):
    """check if creating duplicates fails"""
    create = Phone()
    create.create_contact('peter', 999)
    create.create_contact('peter', 999)
    duplicate = True
    if len(list(set(create.contact.keys()))) == len(create.contact.keys()):
        duplicate = False

    self.assertEqual(duplicate, False)

def test_wrong_data(self):
    """testing invalid input."""
    create = Phone()
    response = create.create_contact(999, 999)

    self.assertEqual(response, 'invalid input')

def test_view_all(self):
    """testing view_all_contacts."""
    create = Phone()
    create.create_contact('sam', 99669)
    response = create.view_all()

    self.assertEqual(response, create.contact)

def test_view_one(self):
    """testing if viewing one contact works."""
    create = Phone()
    create.create_contact('gimmz', 669)
    response = create.view_contact('gimmz')

    self.assertEqual(response, 669)
