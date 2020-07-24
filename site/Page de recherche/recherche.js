const send = (event) => {
    event.preventDefault();

    var tabLignes = document.querySelector("#monTableau").rows;
    
    let i = 0;
    for (ligne of tabLignes) {
        ligne.cells[0].innerHTML = tabUtil[i].nom;
        ligne.cells[1].innerHTML = tabUtil[i].prenom;
        ligne.cells[2].innerHTML = tabUtil[i].dateNaissance;
        ligne.cells[3].innerHTML = tabUtil[i].email;
        ligne.cells[4].innerHTML = tabUtil[i].login;
        ligne.cells[5].innerHTML = tabUtil[i].password;
        i++;
    }

    console.log(event);

}
document.querySelector("#formRecherche").addEventListener('submit', send);
