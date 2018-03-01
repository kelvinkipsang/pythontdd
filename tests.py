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
