from flask import Flask

app = Flask (__name__)

@app.route('/')
def app_usandoflaskk():
    return 'app_usando_Flask'

@app.route('/ventas')
def ventas():
    return 'página de ventas'

@app.route('/articulos/<id>')
def articulitos(id):
    return 'página de articulos numero {}'.format(id)

@app.errorhandler(404)
def pagina_noencontrada(error):
    return 'página no encontrada',404



if __name__ == '__main__':
    app.run(port=3000, debug=True)
