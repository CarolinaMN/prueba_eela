
import unittest
import funciones

class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(funciones.primo(4))
        self.assertTrue(funciones.primo(2))
        self.assertTrue(funciones.primo(3))
        self.assertFalse(funciones.primo(8))
        self.assertFalse(funciones.primo(10))
        self.assertTrue(funciones.primo(7))
        self.assertTrue(funciones.primo(7))
        self.assertEqual(funciones.primo(-3), "No se permiten números negativos.")
    
    def test_cubic(self):
        self.assertEqual(funciones.cubica(2), 8)
        self.assertEqual(funciones.cubica(-2), -8)
        self.assertNotEqual(funciones.cubica(2), 4)
        self.assertNotEqual(funciones.cubica(-3), 27)

    def test_say_hello(self):
        self.assertEqual(funciones.saludo("Juan"), "Hola, Juan")
        self.assertEqual(funciones.saludo("Carlos"), "Hola, Carlos")
        self.assertNotEqual(funciones.saludo("Lili"), "Hola, Lilii")
        self.assertNotEqual(funciones.saludo("Maria"), "Hola, Mariaa")
        self.assertEqual(funciones.saludo("Karla"), "Hola, Karla")


if __name__ == '__main__':
    unittest.main()

