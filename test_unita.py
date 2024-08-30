import unittest
from libro import app

class TestLibro(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Cambia b'Ingeniería' a 'Ingeniería'
        self.assertIn('Ingeniería'.encode('utf-8'), response.data)

    def test_add_book(self):
        response = self.client.post('/add', data={
            'categoria': 'Ciencia',
            'genero': 'Neutro',
            'fecha': '05/05/2024',
            'monto': '25.0'
        })
        self.assertEqual(response.status_code, 302)  # Redirecciona después de agregar el libro
        # Cambia b'Ciencia' a 'Ciencia'
        self.assertIn('Ciencia'.encode('utf-8'), self.client.get('/').data)

if __name__ == '__main__':
    unittest.main()
