const send = (event) => {
    event.preventDefault();
    

    console.log(event);

    for (elt of event.target) {
        console.log(elt.value)
    }

}
document.querySelector("#formInscription").addEventListener('submit', send);
