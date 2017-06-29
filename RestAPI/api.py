from flask import Flask
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

## MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'testserver'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

api = Api(app)

class AddEquipament(Resource):
    def post(self):
        try:
            #Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('serial_number', type=int, help='Serial number for equipament')
            parser.add_argument('type', type=str, help='Type of Equipament HRADC or UDC')
            args = parser.parse_args()

            _equipament_serial = args['serial_number']
            _equipament_type = args['type']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spAddEquipament', (_equipament_serial, _equipament_type))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200', 'Message': 'Add Sucess'}
            else:
                return {'StatusCode':'1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(AddEquipament, '/AddEquipament')

if __name__ == '__main__':
    app.run(debug=True)
