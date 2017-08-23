#!/usr/bin/env python3

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
            parser.add_argument('numero_serie', type=int)
            parser.add_argument('variante', type=str)
            #parser.add_argument('data_instalacao', type=str)
            #parser.add_argument('nome_operador', type=str)
            parser.add_argument('resistor_burden', type=float)
            parser.add_argument('frequencia_corte', type=float)
            parser.add_argument('ordem_filtro', type=int)
            parser.add_argument('controlador_temperatura', type=int)
            parser.add_argument('amplificador_burden', type=str)
            parser.add_argument('jumper_gnd', type=bool)
            parser.add_argument('jumper_burden',type=bool)
            parser.add_argument('filtro_modo_comum', type=bool)
            args = parser.parse_args()

            _numero_serie           = args['numero_serie']
            _variante               = args['variante']
            #_data_instal            = args['data_instalacao']
            #_nome_operador          = args['nome_operador']
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
            cursor.callproc('sp_add_hradc', (_numero_serie, _variante, _resistor_burden, _freq_corte,
                                                _ordem_filtro, _control_temperatura, _amplificador_burden,
                                                _jumper_gnd, _jumper_burden, _filtro_modo_comum))
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
            parser.add_argument('id_medida', type=int)
            parser.add_argument('gnd', type=float)
            parser.add_argument('vref_p', type=float)
            parser.add_argument('vref_n', type=float)
            parser.add_argument('temperatura', type=float)
            parser.add_argument('vin_p', type=float)
            parser.add_argument('vin_n', type=float)
            parser.add_argument('lin_p', type=float)
            parser.add_argument('lin_n', type=float)
            parser.add_argument('details', type=str)
            args = parser.parse_args()

            _resultado_teste        = args['resultado_teste']
            _numero_serie_hradc     = args['numero_serie_hradc']
            _id_medida              = args['id_medida']
            _gnd                    = args['gnd']
            _vref_p                 = args['vref_p']
            _vref_n                 = args['vref_n']
            _temp                   = args['temperatura']
            _vin_p                  = args['vin_p']
            _vin_n                  = args['vin_n']
            _lin_p                  = args['lin_p']
            _lin_n                  = args['lin_n']
            _details                = args['details']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_log_hradc', (_resultado_teste, _numero_serie_hradc, _id_medida,
                                                    _gnd, _vref_p, _vref_n, _temp, _vin_p, _vin_n,
                                                    _lin_p, _lin_n, _details))

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
            #parser.add_argument('nome_operador', type=str)
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
            #_nome_operador          = args['nome_operador']
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
                                                    _ganho_vin, _offset_vin, _ganho_lin,
                                                    _offset_lin, _vref_p, _vref_n, _gnd,
                                                    _numero_serie_hradc))

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
            parser.add_argument('variante', type=str)
            args = parser.parse_args()

            _numero_serie   = args['numero_serie']
            _variante       = args['variante']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_dcct', (_numero_serie, _variante))
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
            parser.add_argument('id_canal_dcct', type=int)
            parser.add_argument('resultado_teste', type=str)
            parser.add_argument('numero_serie_dcct', type=int)
            parser.add_argument('iload_desligado', type=float)
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

            _id_canal_dcct          = args['id_canal_dcct']
            _resultado_teste        = args['resultado_teste']
            _numero_serie_dcct      = args['numero_serie_dcct']
            _iload_off              = args['iload_desligado']
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
            cursor.callproc('sp_add_log_dcct', (_id_canal_dcct, _resultado_teste,
                                                _numero_serie_dcct, _iload_off, _iload0,
                                                _iload1, _iload2, _iload3, _iload4,
                                                _iload5, _iload6, _iload7, _iload8,
                                                _iload9, _iload10, _details))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class DcctReport(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_get_dcct_report')
            data = cursor.fetchall()
            return str(data)
        except Exception as e:
            return {'error': str(e)}

class AddPowerSupply(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('numero_serie', type=int)
            args = parser.parse_args()

            _numero_serie           = args['numero_serie']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_power_supply', (_numero_serie,))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddLogPowerSupply(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id_tipo_teste_fonte', type=int)
            parser.add_argument('id_canal_fonte', type=int)
            parser.add_argument('resultado_teste', type=str)
            parser.add_argument('numero_serie_fonte', type=int)
            parser.add_argument('resultado_teste_on_off', type=str)
            parser.add_argument('iout_mais_20_duty_cycle', type=float)
            parser.add_argument('iout_menos_20_duty_cycle', type=float)
            parser.add_argument('iout0', type=float)
            parser.add_argument('iout1', type=float)
            parser.add_argument('vout0', type=float)
            parser.add_argument('vout1', type=float)
            parser.add_argument('vdclink0', type=float)
            parser.add_argument('vdclink1', type=float)
            parser.add_argument('temperatura0', type=float)
            parser.add_argument('temperatura1', type=float)
            parser.add_argument('details', type=str)
            args = parser.parse_args()

            _id_tipo_teste              = args['id_tipo_teste_fonte']
            _id_canal_ps                = args['id_canal_fonte']
            _resultado_teste            = args['resultado_teste']
            _numero_serie_ps            = args['numero_serie_fonte']
            _result_test_on_off         = args['resultado_teste_on_off']
            _iout_add_20_duty_cycle     = args['iout_mais_20_duty_cycle']
            _iout_less_20_duty_cycle    = args['iout_menos_20_duty_cycle']
            _iout0                      = args['iout0']
            _iout1                      = args['iout1']
            _vout0                      = args['vout0']
            _vout1                      = args['vout1']
            _vdclink0                   = args['vdclink0']
            _vdclink1                   = args['vdclink1']
            _temperatura0               = args['temperatura0']
            _temperatura1               = args['temperatura1']
            _details                    = args['details']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_log_power_supply', (_id_tipo_teste, _id_canal_ps, _resultado_teste,
                                                        _numero_serie_ps, _result_test_on_off,
                                                        _iout_add_20_duty_cycle, _iout_less_20_duty_cycle,
                                                        _iout0, _iout1, _vout0, _vout1, _vdclink0,
                                                        _vdclink1, _temperatura0, _temperatura1, _details))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddRack(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('numero_serie', type=int)
            args = parser.parse_args()

            _numero_serie           = args['numero_serie']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_rack', (_numero_serie,))

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Sucesso'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}

class AddLogRack(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('resultado_teste', type=str)
            parser.add_argument('numero_serie_bastidor', type=int)
            parser.add_argument('iout0', type=float)
            parser.add_argument('iout1', type=float)
            parser.add_argument('iout2', type=float)
            parser.add_argument('iout3', type=float)
            parser.add_argument('delta_iout0', type=float)
            parser.add_argument('delta_iout1', type=float)
            parser.add_argument('delta_iout2', type=float)
            parser.add_argument('delta_iout3', type=float)
            parser.add_argument('details', type=str)
            args = parser.parse_args()

            _resultado_teste        = args['resultado_teste']
            _numero_serie_rack      = args['numero_serie_bastidor']
            _iout0                  = args['iout0']
            _iout1                  = args['iout1']
            _iout2                  = args['iout2']
            _iout3                  = args['iout3']
            _delta_iout0            = args['delta_iout0']
            _delta_iout1            = args['delta_iout1']
            _delta_iout2            = args['delta_iout2']
            _delta_iout3            = args['delta_iout3']
            _details                = args['details']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_log_rack', (_resultado_teste, _numero_serie_rack, _iout0,
                                                _iout1, _iout2, _iout3, _delta_iout0, _delta_iout1,
                                                _delta_iout2, _delta_iout3, _details))
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
            parser = reqparse.RequestParser()
            parser.add_argument('numero_serie', type=int)
            args = parser.parse_args()

            _numero_serie           = args['numero_serie']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_udc', (_numero_serie, ))

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
            parser = reqparse.RequestParser()
            parser.add_argument('resultado_teste', type=str)
            parser.add_argument('numero_serie_udc', type=int)
            parser.add_argument('io_expander0', type=str)
            parser.add_argument('io_expander1', type=str)
            parser.add_argument('leds', type=str)
            parser.add_argument('buzzer', type=str)
            parser.add_argument('eeprom', type=str)
            parser.add_argument('flash', type=str)
            parser.add_argument('ram', type=str)
            parser.add_argument('rtc_communication', type=str)
            parser.add_argument('rtc_interrupt', type=str)
            parser.add_argument('sensor_temperatura_com', type=str)
            parser.add_argument('sensor_temperatura_val', type=str)
            parser.add_argument('control_aliment_plano_isolado', type=str)
            parser.add_argument('rs4850', type=str)
            parser.add_argument('rs4851', type=str)
            parser.add_argument('rs4852', type=str)
            parser.add_argument('sdcard_inserido', type=str)
            parser.add_argument('sdcard_communication', type=str)
            parser.add_argument('ethernet_inicializacao', type=str)
            parser.add_argument('ethernet_ping', type=str)
            parser.add_argument('loopback', type=str)
            parser.add_argument('details', type=str)
            args = parser.parse_args()

            _resultado_teste        = args['resultado_teste']
            _numero_serie_udc       = args['numero_serie_udc']
            _io_expander0           = args['io_expander0']
            _io_expander1           = args['io_expander1']
            _leds                   = args['leds']
            _buzzer                 = args['buzzer']
            _eeprom                 = args['eeprom']
            _flash                  = args['flash']
            _ram                    = args['ram']
            _rtc_communication      = args['rtc_communication']
            _rtc_interrupt          = args['rtc_interrupt']
            _sensor_temperatura_com = args['sensor_temperatura_com']
            _sensor_temperatura_val = args['sensor_temperatura_val']
            _control_plano_isol     = args['control_aliment_plano_isolado']
            _rs4850                 = args['rs4850']
            _rs4851                 = args['rs4851']
            _rs4852                 = args['rs4852']
            _sdcard_inserido        = args['sdcard_inserido']
            _sdcard_communication   = args['sdcard_communication']
            _ethernet_inicializacao = args['ethernet_inicializacao']
            _ethernet_ping          = args['ethernet_ping']
            _loopback               = args['loopback']
            _details                = args['details']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_log_udc', (_resultado_teste, _numero_serie_udc, _io_expander,
                                                _leds, _buzzer, _eeprom, _flash, _ram, _rtc_communication,
                                                _rtc_interrupt, _sensor_temperatura, _control_plano_isol,
                                                _rs485, _details))

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
            parser.add_argument('vload0', type=float)
            parser.add_argument('vload1', type=float)
            parser.add_argument('vload2', type=float)
            parser.add_argument('vload3', type=float)
            parser.add_argument('vload4', type=float)
            parser.add_argument('vload5', type=float)
            parser.add_argument('vdclink0', type=float)
            parser.add_argument('vdclink1', type=float)
            parser.add_argument('vdclink2', type=float)
            parser.add_argument('vdclink3', type=float)
            parser.add_argument('vdclink4', type=float)
            parser.add_argument('vdclink5', type=float)
            parser.add_argument('temperatura0', type=float)
            parser.add_argument('temperatura1', type=float)
            parser.add_argument('temperatura2', type=float)
            parser.add_argument('temperatura3', type=float)
            parser.add_argument('temperatura4', type=float)
            parser.add_argument('temperatura5', type=float)
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
            _temperatura0           = args['temperatura0']
            _temperatura1           = args['temperatura1']
            _temperatura2           = args['temperatura2']
            _temperatura3           = args['temperatura3']
            _temperatura4           = args['temperatura4']
            _temperatura5           = args['temperatura5']
            _details                = args['details']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_add_log_power_module', (_resultado_teste, _numero_serie_dcct,
                            _iload0, _iload1, _iload2, _iload3, _iload4, _iload5, _vload0,
                            _vload1, _vload2, _vload3, _vload4, _vload5, _vdclink0, _vdclink1,
                            _vdclink2, _vdclink3, _vdclink4, _vdclink5, _temperatura0,
                            _temperatura1, _temperatura2, _temperatura3, _temperatura4,
                            _temperatura5, _details))

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
api.add_resource(AddPowerSupply, '/AddPowerSupply')
api.add_resource(AddLogPowerSupply, '/AddLogPowerSupply')
api.add_resource(AddRack, '/AddRack')
api.add_resource(AddLogRack, '/AddLogRack')
api.add_resource(AddUdc, '/AddUdc')
api.add_resource(AddLogUdc, '/AddLogUdc')
api.add_resource(AddPowerModule, '/AddPowerModule')
api.add_resource(AddLogPowerModule, '/AddLogPowerModule')

api.add_resource(DcctReport, '/DcctReport')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True)
