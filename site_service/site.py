from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from controlers.utilisateur_controler import UtilisateursControler
site = Flask(__name__)

CORS(site)

site.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.99.101:3306/Utilisateurs'

db = SQLAlchemy(site)

UtilisateursControler.register(site)


if __name__ == "__name__":
    site.run(debug=True)



