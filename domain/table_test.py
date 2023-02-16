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

# TODO: en vez de utilizar una distribucion de quadrado, hay que modificarlo para hacerlo en formato rectangulo

if __name__ == '__main__':
    unittest.main()