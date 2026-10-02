from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('circulo.html', area=None, perimetro=None, radio="")

@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    area = None
    perimetro = None
    radio_val = ""
    error = None

    if request.method == 'POST':
        radio_val = request.form.get('radio', '')
        try:
            radio = float(radio_val)
            if radio <= 0:
                error = "El radio debe ser mayor que 0"
            else:
                area = math.pi * radio ** 2
                perimetro = 2 * math.pi * radio
        except ValueError:
            error = "Por favor ingresa un número válido"

    return render_template(
        'circulo.html',
        area=area,
        perimetro=perimetro,
        radio=radio_val,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)
    