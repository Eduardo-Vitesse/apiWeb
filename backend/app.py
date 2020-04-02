from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

# Montado o Schema com Marsmallow
class ContactSchema(ma.Schema):
    class Meta:
        fields = ("name","email")

# Montando a tabela
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)

# TODAS AS ROTAS

@app.route("/contacts", methods=["GET"])
def contacts():
    contacts = Contact.query.all()
    contact_schema = ContactSchema(many=True)
    result = contact_schema.dump(contacts)

    return jsonify(result)


@app.route("/addcontacts", methods=["POST"])
def add_contacts():
    data = request.json

    c = Contact()
    c.name = data["name"]
    c.email = data["email"]

    db.session.add(c)
    db.session.commit()

    contact_schema = ContactSchema()
    result = contact_schema.dump(c)

    return jsonify(result)



if __name__ == "__main__":
    app.run(port=3001, debug=True)
