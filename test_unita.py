# test_libro.py
import unittest
from libro import agregar_libro

class TestLibro(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para cada prueba
        self.inventario = []

    def test_agregar_libro(self):
        # Prueba para agregar un libro
        resultado = agregar_libro(self.inventario, "Ingeniería", "Femenino", "01/01/2024", 10.0)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['Categoría'], "Ingeniería")
        self.assertEqual(resultado[0]['Género'], "Femenino")
        self.assertEqual(resultado[0]['Fecha'], "01/01/2024")
        self.assertEqual(resultado[0]['Monto'], 10.0)

if __name__ == '__main__':
    unittest.main()
