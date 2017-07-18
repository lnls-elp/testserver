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
            parser.add_argument('resultado_teste', type=str)
            parser.add_argument('numero_serie_hradc', type=int)
            args = parser.parse_args()

            _resultado_teste        = args['resultado_teste']
            _numero_serie_hradc     = args['numero_serie_hradc']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_log_hradc', (_resultado_teste, _numero_serie_hradc))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddCalibHradc(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('temperatura_hradc', type=float)
            parser.add_argument('temperatura_dmm', type=float)
            parser.add_argument('temperatura_fonte', type=float)
            parser.add_argument('nome_operador', type=str)
            parser.add_argument('ganho_vin', type=float)
            parser.add_argument('offset_vin', type=float)
            parser.add_argument('ganho_lin', type=float)
            parser.add_argument('offset_lin', type=float)
            parser.add_argument('vref_p', type=float)
            parser.add_argument('vref_n', type=float)
            parser.add_argument('gnd', type=float)
            parser.add_argument('numero_serie_hradc', type=str)
            args = parser.parse_args()

            _temp_hradc             = args['temperatura_hradc']
            _temp_dmm               = args['temperatura_dmm']
            _temp_fonte             = args['temperatura_fonte']
            _nome_operador          = args['nome_operador']
            _ganho_vin              = args['ganho_vin']
            _offset_vin             = args['offset_vin']
            _ganho_lin              = args['ganho_lin']
            _offset_lin             = args['offset_lin']
            _vref_p                 = args['vref_p']
            _vref_n                 = args['vref_n']
            _gnd                    = args['gnd']
            _numero_serie_hradc     = args['numero_serie_hradc']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_calib_hradc', (_temp_hradc, _temp_dmm, _temp_fonte,
                                                    _nome_operador, ganho_vin, _offset_vin,
                                                    _ganho_lin, _offset_lin, _vref_p,
                                                    _vref_n, _gnd, _numero_serie_hradc))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}

        except Exception as e:
            return {'erro': str(e)}

class AddDcct(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('numero_serie', type=int)
            args = parser.parse_args()

            _numero_serie           = args['numero_serie']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_dcct', (_numero_serie,))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}

class AddLogDcct(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('resultado_teste', type=str)
            parser.add_argument('numero_serie_dcct', type=int)
            parser.add_argument('iload0', type=float)
            parser.add_argument('iload1', type=float)
            parser.add_argument('iload2', type=float)
            parser.add_argument('iload3', type=float)
            parser.add_argument('iload4', type=float)
            parser.add_argument('iload5', type=float)
            parser.add_argument('iload6', type=float)
            parser.add_argument('iload7', type=float)
            parser.add_argument('iload8', type=float)
            parser.add_argument('iload9', type=float)
            parser.add_argument('iload10', type=float)
            parser.add_argument('details', type=str)

            args = parser.parse_args()

            _resultado_teste        = args['resultado_teste']
            _numero_serie_dcct      = args['numero_serie_dcct']
            _iload0                 = args['iload0']
            _iload1                 = args['iload1']
            _iload2                 = args['iload2']
            _iload3                 = args['iload3']
            _iload4                 = args['iload4']
            _iload5                 = args['iload5']
            _iload6                 = args['iload6']
            _iload7                 = args['iload7']
            _iload8                 = args['iload8']
            _iload9                 = args['iload9']
            _iload10                = args['iload10']
            _details                = args['details']


            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_log_dcct', (_resultado_teste, _numero_serie_dcct,
                                                _iload0, _iload1, _iload2, _iload3,
                                                _iload4, _iload5, _iload6, _iload7,
                                                _iload8, _iload9, _iload10, _details))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddFonte(Resource):
    def post(self):
        try:
            #TODO: Fill implementation for this resource
            parser = reqparse.RequestParser()
            #TODO: Add arguments
            args = parser.parse_args()

            #TODO: create variables for callproc

            conn = mysql.connect()
            cursor = conn.cursor()
            #cursor.callproc('sp_add_fonte', (_resultado_teste, _numero_serie_dcct))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddLogFonte(Resource):
    def post(self):
        try:
            #TODO: Fill implementation for this resource
            parser = reqparse.RequestParser()
            #TODO: Add arguments
            args = parser.parse_args()

            #TODO: create variables for callproc

            conn = mysql.connect()
            cursor = conn.cursor()
            #cursor.callproc('sp_add_log_fonte', (_resultado_teste, _numero_serie_dcct))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddBastidor(Resource):
    def post(self):
        try:
            #TODO: Fill implementation for this resource
            parser = reqparse.RequestParser()
            #TODO: Add arguments
            args = parser.parse_args()

            #TODO: create variables for callproc

            conn = mysql.connect()
            cursor = conn.cursor()
            #cursor.callproc('sp_add_bastidor', (_resultado_teste, _numero_serie_dcct))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddLogBastidor(Resource):
    def post(self):
        try:
            #TODO: Fill implementation for this resource
            parser = reqparse.RequestParser()
            #TODO: Add arguments
            args = parser.parse_args()

            #TODO: create variables for callproc

            conn = mysql.connect()
            cursor = conn.cursor()
            #cursor.callproc('sp_add_log_bastidor', (_resultado_teste, _numero_serie_dcct))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddUdc(Resource):
    def post(self):
        try:
            #TODO: Fill implementation for this resource
            parser = reqparse.RequestParser()
            #TODO: Add arguments
            args = parser.parse_args()

            #TODO: create variables for callproc

            conn = mysql.connect()
            cursor = conn.cursor()
            #cursor.callproc('sp_add_udc', (_resultado_teste, _numero_serie_dcct))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddLogUdc(Resource):
    def post(self):
        try:
            #TODO: Fill implementation for this resource
            parser = reqparse.RequestParser()
            #TODO: Add arguments
            args = parser.parse_args()

            #TODO: create variables for callproc

            conn = mysql.connect()
            cursor = conn.cursor()
            #cursor.callproc('sp_add_log_udc', (_resultado_teste, _numero_serie_dcct))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddPowerModule(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('numero_serie', type=int)
            args = parser.parse_args()

            _numero_serie           = args['numero_serie']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_power_module', (_numero_serie,))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddLogPowerModule(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('resultado_teste', type=str)
            parser.add_argument('numero_serie_dcct', type=int)
            parser.add_argument('iload0', type=float)
            parser.add_argument('iload1', type=float)
            parser.add_argument('iload2', type=float)
            parser.add_argument('iload3', type=float)
            parser.add_argument('iload4', type=float)
            parser.add_argument('iload5', type=float)
            parser.add_argument('iload6', type=float)
            parser.add_argument('iload7', type=float)
            parser.add_argument('iload8', type=float)
            parser.add_argument('iload9', type=float)
            parser.add_argument('iload10', type=float)
            parser.add_argument('details', type=str)

            args = parser.parse_args()

            _resultado_teste        = args['resultado_teste']
            _numero_serie_dcct      = args['numero_serie_dcct']
            _iload0                 = args['iload0']
            _iload1                 = args['iload1']
            _iload2                 = args['iload2']
            _iload3                 = args['iload3']
            _iload4                 = args['iload4']
            _iload5                 = args['iload5']
            _vload0                 = args['vload0']
            _vload1                 = args['vload1']
            _vload2                 = args['vload2']
            _vload3                 = args['vload3']
            _vload4                 = args['vload4']
            _vload5                 = args['vload5']
            _vdclink0               = args['vdclink0']
            _vdclink1               = args['vdclink1']
            _vdclink2               = args['vdclink2']
            _vdclink3               = args['vdclink3']
            _vdclink4               = args['vdclink4']
            _vdclink5               = args['vdclink5']
            _temperatura            = args['temperatura0']
            _temperatura            = args['temperatura1']
            _temperatura            = args['temperatura2']
            _temperatura            = args['temperatura3']
            _temperatura            = args['temperatura4']
            _temperatura            = args['temperatura5']
            _details                = args['details']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_log_power_module', (_resultado_teste, _numero_serie_dcct,
                            _iload0, _iload1, _iload2, _iload3, _iload4, _iload5, _vload0,
                            _vload1, _vload2, _vload3, _vload4, _vload5, _vdclink0, _vdclink1,
                            _vdclink2, _vdclink3, _vdclink4, _vdclink5, _temperatura0,
                            _temperatura1, _temperatura2, _temperatura3, _temperatura4,
                            _temperatura5,))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(AddHradc, '/AddHradc')
api.add_resource(AddLogHradc, '/AddLogHradc')
api.add_resource(AddCalibHradc, '/AddCalibHradc')
api.add_resource(AddDcct, '/AddDcct')
api.add_resource(AddLogDcct, '/AddLogDcct')
api.add_resource(AddFonte, '/AddFonte')
api.add_resource(AddLogFonte, '/AddLogFonte')
api.add_resource(AddBastidor, '/AddBastidor')
api.add_resource(AddLogBastidor, '/AddLogBastidor')
api.add_resource(AddUdc, '/AddUdc')
api.add_resource(AddLogUdc, '/AddLogUdc')
api.add_resource(AddPowerModule, '/AddPowerModule')
api.add_resource(AddLogPowerModule, '/AddLogPowerModule')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True)
