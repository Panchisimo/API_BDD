from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

bd = mysql.connector.connect(host='localhost',user='Francisco',passwd='JAVIER',database='contactos')
cursor = bd.cursor()

@app.route('/create/', methods=["GET","POST"])
def agenda():
    if request.method == "GET":
        contactos = []
        query = "SELECT * FROM contacto"
        cursor.execute(query)

        for contacto in cursor.fetchall():
            d = {
                'id': contacto[0],
                'correo': contacto[1],
                'avatar': contacto[2],
                'nombre': contacto[3],
                'telefono': contacto[4],
                'facebook': contacto[5],
                'instagram': contacto[6],
                'twitter': contacto[7]
            }
            contactos.append(d)

        return jsonify(contactos)
    else:
        data = request.get_json()
        print(data)

        query = "INSERT INTO contacto(correo, avatar, nombre, telefono, facebook, instagram, twitter) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (data['correo'], data['avatar'], data['nombre'], data['telefono'], data['facebook'], data['instagram'], data['twitter']))
        bd.commit()

        if cursor.rowcount:
            return jsonify({'data':'ok'})
        else:
            return jsonify({'data':'ok'})

@app.route('/delete/', methods=['post'])
def remove():
    data = request.get_json();

    query = "DELETE FROM contacto WHERE id = %s;"
    cursor.execute(query, (data['id'],))
    bd.commit()

    if cursor.rowcount:
        return jsonify({'data': 'ok'})
    else:
        return jsonify({'data': 'ok'})

@app.route('/update/', methods=['post'])
def edit():
    data = request.get_json()

    query = "UPDATE contacto SET correo = %s, avatar = %s, nombre = %s, telefono = %s, facebook = %s, instagram = %s, twitter = %s WHERE id = %s;"
    cursor.execute(query, (
    data['correo'], data['avatar'], data['nombre'], data['telefono'], data['facebook'], data['instagram'],
    data['twitter'], data['id']))
    bd.commit()

    if cursor.rowcount:
        return jsonify({'data': 'ok'})
    else:
        return jsonify({'data': 'ok'})

app.run(debug=True)
