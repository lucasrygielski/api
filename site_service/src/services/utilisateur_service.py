import repositories.utilisateur_repo as utilisateurRepo 
from models.utilisateur import utilisateur
import jsonpickle


def get_utilisateurs():
    utilisateurs = utilisateurRepo.get_utilisateurs()
    return jsonpickle.encode(utilisateurs)

def get_utilisateur_by_id(utilisateur_id):
    return utilisateur_id

def create_utilisateur(utilisateurDto):
    utilisateur = Utilisateur(utilisateurDto.Nom, utilisateurDto.Prenom, utilisateurDto.Naissance, utilisateurDto.Email, utilisateurDto.Pseudo, utilisateurDto.Password, utilisateurDto.done)
    date = utilisateurRepo.create_utilisateur(utilisateur)
    utilisateurDto = jsonpickle.encode(data,max_depth=2)
    return utilisateurDto 

def update_utilisateur(utilisateur_id):
    return utilisateur_id

def delete_utilisateur(utilisateur_id):
    return utilisateur_id
    

