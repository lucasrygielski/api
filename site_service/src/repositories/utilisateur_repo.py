from flask_sqlalchemy import SQLAlchemy
from models.utilisateur import Utilisateur

db = SQLAlchemy()

def get_utilisateurs():
    utilisateurs = Utilisateur.query.all()
    return utilisateurs

def get_utilisateur_by_id(utilisateur_id):
    return utilisateur_id

def create_utilisateur(utilisateur):
    db.session.add(utilisateur)
    db.session.commit()
    return utilisateur.id 

def update_utilisateur(utilisateur_id):
    return utilisateur_id

def delete_utilisateur(utilisateur_id):
    return utilisateur_id

