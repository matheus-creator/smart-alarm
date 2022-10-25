const checkUserExists = (user, users) => {
    for (let i = 0; i < users.length; i++) {
        if (user.email === users[i].email) return true
    }
    return false
}

const checkUserLogin = (user, users) => {
    let found = false
    for (let i = 0; i < users.length; i++) {
        if (users[i].email === user.email) {
            if (users[i].password === user.password) {
                found = true
            }
        }
    }
    return found
}

module.exports = {
    checkUserExists,
    checkUserLogin
}