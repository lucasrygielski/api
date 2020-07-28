const users = [
    { id: 1, login: 'lucasr', email: 'email@sfr.fr', },
    { id: 2, login: 'paulb', email: 'email@free.fr', },
]

const deleteUser = event => {
    console.log(event.target.id)
}

const renderUsers = () => {
    const list = document.querySelector('#userList')
    for (user of users) {
        const li = document.createElement('li')
        const data = document.createTextNode(`Login : ${user.login}  Email: ${user.email}`)
        const button = document.createElement('button')
        button.setAttribute("id", user.id.toString())
        button.addEventListener('click', deleteUser)
        button.innerHTML = "Supprimer"
        li.appendChild(data)
        li.appendChild(button)
        list.appendChild(li)
    }
}

renderUsers()