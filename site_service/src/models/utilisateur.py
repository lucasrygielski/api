from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Utilisateur(db.Model):
    __tablename__ = "utilisateurs"
    id = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String)
    Prenom = db.Column(db.String)
    Naissance = db.Column(db.String)
    Email = db.Column(db.String)
    Pseudo = db.Column(db.String)
    Password = db.Column(db.String)
    done = db.Column(db.Boolean)

    def __init__(self, Nom, Prenom, Naissance, Email, Pseudo, Password, done):
        self.Nom = Nom
        self.Prenom = Prenom
        self.Naissance = Naissance
        self.Email = Email
        self.Pseudo = Pseudo
        self.Password = Password
        self.done = done
    
    def __repr__(self):
        return f'<Utilisateur id:{self.id} Nom:{self.Nom} Prenom:{self.Prenom} Naissance:{self.Naissance} Email:{self.Email} Pseudo:{self.Pseudo} Password:{self.Password} done: {self.done}>'

    