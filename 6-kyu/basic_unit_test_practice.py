from unittest import TestCase


class TestPhoneBook(TestCase):

    def setUp(self):
        self.phone_book = PhoneBook()

    def test_create_method(self):                                 # Statement 1
        self.phone_book.create("User", "12345678")
        self.assertEqual(self.phone_book["User"], "12345678")

    def test_retrieve_method_when_the_name_does_not_exist(self):  # Statement 3
        with self.assertRaises(KeyError):
            self.phone_book.retrieve('User2')

    def test_retrieve_method_when_the_name_exists(self):          # Statement 2
        self.phone_book.create('User', '12345678')
        self.assertEqual(self.phone_book.retrieve('User'), '12345678')
        
    def test_update_method_when_the_name_exists(self):            # Statement 4
        self.phone_book.create('User', '12345678')
        self.phone_book.update('User', '87654321')
        self.assertEqual(self.phone_book.retrieve('User'), '87654321')

    def test_delete_method_when_the_name_exists(self):            # Statement 5
        self.phone_book.create('User', '12345678')
        self.phone_book.delete('User')
        self.assertNotIn('User', self.phone_book)
