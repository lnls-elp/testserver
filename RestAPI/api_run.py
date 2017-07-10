from flask import Flask
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

## MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'testserverdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

api = Api(app)

class AddHradc(Resource):
    def post(self):
        try:
            #Parse the arguments
            parser = reqparse.RequestParser()
            #parser.add_argument('numero_serie', type=int, help='Número de série para o equipamento')
            parser.add_argument('numero_serie', type=int)
            parser.add_argument('variante', type=str)
            parser.add_argument('data_instalacao', type=str)
            parser.add_argument('nome_operador', type=str)
            parser.add_argument('resistor_burden', type=float)
            parser.add_argument('frequencia_corte', type=float)
            parser.add_argument('ordem_filtro', type=int)
            parser.add_argument('controlador_temperatura', type=int)
            parser.add_argument('amplificador_burden', type=str)
            parser.add_argument('jumper_gnd', type=int)
            parser.add_argument('jumper_burden',type=int)
            parser.add_argument('filtro_modo_comum', type=int)
            args = parser.parse_args()

            _numero_serie           = args['numero_serie']
            _variante               = args['variante']
            _data_instal            = args['data_instalacao']
            _nome_operador          = args['nome_operador']
            _resistor_burden        = args['resistor_burden']
            _freq_corte             = args['frequencia_corte']
            _ordem_filtro           = args['ordem_filtro']
            _control_temperatura    = args['controlador_temperatura']
            _amplificador_burden    = args['amplificador_burden']
            _jumper_gnd             = args['jumper_gnd']
            _jumper_burden          = args['jumper_burden']
            _filtro_modo_comum      = args['filtro_modo_comum']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_hradc', (_numero_serie, _variante, _data_instal, _nome_operador,
                                                _resistor_burden, _freq_corte, _ordem_filtro,
                                                _control_temperatura, _amplificador_burden, _jumper_gnd,
                                                _jumper_burden, _filtro_modo_comum))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}

class AddLogHradc(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
        except Exception as e:
            return {'error': str(e)}

class AddCalibHradc(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
        except Exception as e:
            return {'erro': str(e)}

api.add_resource(AddHradc, '/AddHradc')
api.add_resource(AddLogHradc, '/AddLogHradc')

if __name__ == '__main__':
    #app.run(host='0.0.0.0:5000')
    app.run(debug=True)
