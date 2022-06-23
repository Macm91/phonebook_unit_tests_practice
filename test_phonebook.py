import unittest

from phonebook import Phonebook

class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        phonebook = Phonebook
        with self.assertRaises(KeyError)
            phonebook.lookup("missing")

    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        phonebook = Phonebook()
        self.assertTrue(phonebook.is_consistent())
