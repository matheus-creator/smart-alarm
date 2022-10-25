const express = require('express');
const utils = require('./utils')

const app = express();
const port = process.env.PORT || 3000;

const users = []

app.use(express.json());

app.post('/signup', (req, res) => {
    const body = req.body
    const newUser = {
        id: users.length + 1,
        name: body.name,
        email: body.email,
        password: body.password
    }
    if (utils.checkUserExists(newUser, users)) {
        res.status(400).send()
    } else {
        users.push(newUser)
        res.status(200).send()
    }
    
})

app.post('/login', (req, res) => {
    const user = req.body
    if (utils.checkUserLogin(user, users)) {
        res.status(200).send()
    } else {
        res.status(400).send()
    }
})

app.listen(port, () => console.log(`Server is up on port ${port}.`));