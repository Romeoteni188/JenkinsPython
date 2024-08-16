import unittest
from datetime import datetime
class TestFormatearFecha(unittest.TestCase):

    def test_formatear_fecha(self):
        entrada = "12"
        esperado = "12/"
        resultado = entrada + "/"
        self.assertEqual(resultado, esperado)

    def test_validacion_fecha(self):
        fecha_valida = "01/01/2023"
        try:
            datetime.strptime(fecha_valida, '%d/%m/%Y')
            resultado = True
        except ValueError:
            resultado = False
        self.assertTrue(resultado)

    def test_editar_libro(self):
        inventario = [
            {"Categoría": "Literatura", "Género": "Femenino", "Fecha": "01/01/2023", "Monto": 150.0}
        ]
        libro_index = 0
        nuevo_categoria = "Ingenieria"
        inventario[libro_index]["Categoría"] = nuevo_categoria
        self.assertEqual(inventario[libro_index]["Categoría"], "Ingenieria")

if __name__ == '__main__':
    unittest.main()
