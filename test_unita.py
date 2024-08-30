import unittest
from datetime import datetime

class TestSistemaInventarioLibros(unittest.TestCase):

    def test_fecha_formato_valido(self):
        # Caso válido
        fecha_valida = "15/08/2023"
        try:
            datetime.strptime(fecha_valida, '%d/%m/%Y')
            resultado = True
        except ValueError:
            resultado = False
        self.assertTrue(resultado)

    def test_fecha_formato_invalido(self):
        # Caso inválido
        fecha_invalida = "31-12-2023"
        try:
            datetime.strptime(fecha_invalida, '%d/%m/%Y')
            resultado = True
        except ValueError:
            resultado = False
        self.assertFalse(resultado)

    def test_monto_numerico(self):
        # Prueba que el monto sea un número válido
        monto = "100.50"
        try:
            monto = float(monto)
            resultado = True
        except ValueError:
            resultado = False
        self.assertTrue(resultado)

    def test_categoria_seleccionada(self):
        # Verifica que la categoría seleccionada sea válida
        categorias = ["Ingenieria", "Literatura", "Administración", "Matematica"]
        categoria_seleccionada = "Ingenieria"
        self.assertIn(categoria_seleccionada, categorias)

    def test_genero_seleccionado(self):
        # Verifica que el género seleccionado sea válido
        generos = ["Femenino", "Masculino"]
        genero_seleccionado = "Femenino"
        self.assertIn(genero_seleccionado, generos)

if __name__ == '__main__':
    unittest.main()
