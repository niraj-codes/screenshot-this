import unittest
from Unit_Test.test_class import *


class TestThis(unittest.TestCase):
    the_class = TestClass()

    def testa_add_book(self):
        result = self.the_class.add_book('1093', 'The Last Fish', 'A.J. Styles', 'Comedy', 58, '2889')
        self.assertTrue(result)

    def testj_add_book_unintended_input1(self):
        result = self.the_class.add_book('1093', 'The Last Fish', 'A.J. Styles', 'Comedy', -98, '2889')
        expected_result = False
        self.assertEqual(result, expected_result)

    def testc_search_book(self):
        result = self.the_class.search_book('1093')
        self.assertTrue(result)

    def testd_issue_book(self):
        result = self.the_class.issue_book('1093', '199333')
        self.assertTrue(result)

    def testk_add_book_unintended_input2(self):
        result = self.the_class.add_book('1093', 'The Last Fish', '', 'Comedy', 98, '2889')
        expected_result = False
        self.assertEqual(result, expected_result)

    def testl_return_non_existent_book(self):
        result = self.the_class.return_book('99', '199333')
        expected_result = False
        self.assertEqual(result, expected_result)

    def testf_return_book(self):
        result = self.the_class.return_book('1093', '199333')
        self.assertTrue(result)

    def testb_list_all_books(self):
        result = self.the_class.list_all_books()
        expected_result = 7
        self.assertEqual(result, expected_result)

    def teste_search_all_activity(self):
        result = self.the_class.search_all_activity()
        expected_result = 10
        self.assertEqual(result, expected_result)

    def testg_delete_book(self):
        result = self.the_class.delete_book()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

    
    
