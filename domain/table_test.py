import unittest
from table import Table

class TestTable(unittest.TestCase):
    def test_0_should_return_an_empty_table(self):
        table = Table(0)

        expectedResult = ""

        self.assertEqual(table.print(), expectedResult)

    def test_1_should_return_table_with_some_content(self):
        table = Table(125)

        self.assertEqual(table.getImageLength(), 84)
        self.assertEqual(table.getImageHeight(), 89)

        self.assertEqual(table.getLogoLength(), 266)
        self.assertEqual(table.getLogoHeight(), 202)

        expectedResult = "xxxxxxxxxxxxxxsxxxxxxxxxxxxxxsxxxxxxxxxxxxxxsxxxxxxllxxxxxxsxxxxxxllxxxxxxsxxxxxxxxxxxxxxsxxxxxxxxxxxxxxsxxxxxxxxxxxxxxsxxxxxxxxxxxxx"
        self.assertEqual(table.print(), expectedResult)
    
    def test_2_should_return_table_with_some_content(self):
        table = Table(89)

        self.assertEqual(table.getImageLength(), 106)
        self.assertEqual(table.getImageHeight(), 104)

        self.assertEqual(table.getLogoLength(), 310)
        self.assertEqual(table.getLogoHeight(), 232)

        expectedResult = "xxxxxxxxxxxxsxxxxxxxxxxxxsxxxxxxxxxxxxsxxxxxllxxxxxsxxxxxllxxxxxsxxxxxxxxxxxxsxxxxxxxxxxxxsxxxxx"
        self.assertEqual(table.print(), expectedResult)

if __name__ == '__main__':
    unittest.main()