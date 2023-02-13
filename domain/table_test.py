import unittest
from table import Table

class TestTable(unittest.TestCase):
    def test_0_should_return_an_empty_table(self):
        table = Table(0)

        expectedResult = ""

        self.assertEqual(table.print(), expectedResult)

    def test_1_should_return_table_with_some_content(self):
        table = Table(60)

        expectedResult = "xxxxxxxxsxxxxxxxxsxxxxxxxxsxxxllxxxsxxxllxxxsxxxxxxxxsxxxxxxxxsxxxxxxxxs"

        self.assertEqual(table.print(), expectedResult)
    
    def test_2_should_return_table_with_some_content(self):
        table = Table(59)

        expectedResult = "xxxxxxxxsxxxxxxxxsxxxxxxxxsxxxllxxxsxxxllxxxsxxxxxxxxsxxxxxxxxsxxxxxxxs"

        self.assertEqual(table.print(), expectedResult)

    def test_3_should_return_table_with_some_content(self):
        table = Table(32)

        expectedResult = "xxxxxxsxxxxxxsxxllxxsxxllxxsxxxxxxsxxxxxxs"

        self.assertEqual(table.print(), expectedResult)
    
    def test_4_should_return_error_if_custom_rows_x_columns_are_lower_than_total_number_of_images(self):
        with self.assertRaises(Exception):
            Table(11, 3, 2)

    def test_5_should_return_table_with_custom_rows_and_columns(self):
        table = Table(13, 5, 4)

        expectedResult = "xxxxsxllxsxllxsxxxxsx"

        self.assertEqual(table.print(), expectedResult)

if __name__ == '__main__':
    unittest.main()