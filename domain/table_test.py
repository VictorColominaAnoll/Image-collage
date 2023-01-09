import unittest
from Table import Table
from Logo import Logo

class TestTable(unittest.TestCase):
    def test_0_should_return_an_empty_table(self):
        table = Table(0)

        expectedResult = ""

        self.assertEqual(table.print(), expectedResult)

    def test_1_should_return_table_with_some_content(self):
        logo = Logo(1, 1)
        table = Table(10, logo)

        expectedResult = "x x x x x l x x x x x"

        self.assertEqual(table.print(), expectedResult)

    def test_2_should_return_table_with_some_content(self):
        logo = Logo(1, 2)
        table = Table(12, logo)

        expectedResult = "x x x l x x x\nx x x l x x x"

        self.assertEqual(table.print(), expectedResult)




if __name__ == '__main__':
    unittest.main()


"""
TODO:
- Printar el contenido
- Tener espacios en blanco
- Tener el tamaño de las piezas (en este caso van a ser de 1) 
"""