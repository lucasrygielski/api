class Utilisateur {
    constructor(nom, prenom, dateNaissance, email, login, password) {
        this.nom = nom;
        this.prenom = prenom;
        this.dateNaissance = dateNaissance;
        this.email = email;
        this.login = login;
        this.password = password;
    }
}

let util1 = new Utilisateur("Dupont", "Guy", "17/09/1960", "email@orange.fr", "login", "password");
let util2 = new Utilisateur("Devermelle", "Monique", "11/08/1964", "email@gmail.com", "login", "password");
let util3 = new Utilisateur("Girond", "Phillipe", "27/10/1970", "email@hotmail.fr", "login", "password");
let util4 = new Utilisateur("Durant", "Morgane", "15/07/2002", "email@hotmail.com", "login", "password");
let util5 = new Utilisateur("Rygielski", "Lucas", "17/02/1997", "email@sfr.fr", "login", "password");
let util6 = new Utilisateur("Bernard", "Paul", "20/12/1997", "email@free.fr", "login", "password");

let tabUtil = [util1, util2, util3, util4, util5, util6]