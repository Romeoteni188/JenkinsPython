from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='.')

# Lista para almacenar libros
inventario = [
    {"Categoría": "Ingeniería", "Género": "Femenino", "Fecha": "01/01/2024", "Monto": 10.0},
    {"Categoría": "Literatura", "Género": "Masculino", "Fecha": "02/02/2024", "Monto": 15.0},
    {"Categoría": "Astrologia", "Género": "Femenino", "Fecha": "03/01/2024", "Monto": 20.0},
    {"Categoría": "Curiosidades", "Género": "Masculino", "Fecha": "04/02/2024", "Monto": 135.0}
]

@app.route('/')
def index():
    return render_template('index.html', inventario=inventario)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        categoria = request.form['categoria']
        genero = request.form['genero']
        fecha = request.form['fecha']
        monto = float(request.form['monto'])
        
        nuevo_libro = {
            "Categoría": categoria,
            "Género": genero,
            "Fecha": fecha,
            "Monto": monto
        }
        inventario.append(nuevo_libro)
        return redirect(url_for('index'))
    
    return render_template('libro.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Cambia el puerto si es necesario
