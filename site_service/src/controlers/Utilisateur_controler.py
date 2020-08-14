from flask_classful import FlaskView, route
from flask import jsonify
from flask import abort
from flask import request
import services.utilisateur_service as utilisateurService
from dto.utilisateur_dto import UtilisateurDto




class UtilisateursControler(FlaskView):

    route_base = '/api/utilisateurs'

    @route('/')
    def get_todos(self):
        utilisateurs = utilisateurService.get_utilisateurs()
        return jsonify(utilisateurs)

    @route('/<int:utilisateur_id')
    def get_utilsateur_by_id(self, utilisateur_id):
        utilisateur = utilisateurService.get_utilsateur_by_id(utilsateur_id)
        return jsonify(utilisateur)

    @route('/', methods=['POST'])
    def create_utilisateur(self):
        Nom = request.json['Nom']
        Prenom = request.json['Prenom']
        Naissance = request.json['Naissance']
        Email = request.json['Email']
        Pseudo = request.json['Pseudo']
        Password = request.json['Password']
        utilisateur = UtilisateurDto(Nom, Prenom, Naissance, Email, Pseudo, Password, False)
        return utilisateurService.create_utilisateur(utilisateur)

    @route('/<int:utilisateur_id>', methods=['PUT'])
    def update_utilisateur(self, utilisateur_id):
        utilisateur = utilisateurService.update_utilisateur(utilisateur_id)
        return jsonify(utilisateur)
    
    @route('/<int:utilisateur_id>', methods=['DELETE'])
    def delete_utilisateur(self, utilisateur_id):
        result = utilisateurService.delete_utilisateur(utilisateur_id)
        return jsonify(result)

    

    
