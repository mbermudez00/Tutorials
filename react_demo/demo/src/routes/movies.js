const {Router} = require('express');
const router = Router();

const movies = require('../sample.json');
console.log(movies);

router.get('/movies', (req, res) => {
    res.json(movies);
});

router.post('/movies', (req, res) => {
    const {id, title, director, rating }= req.body;
    if (id && title && director  && rating){
        const id = movies.length + 1;
        const newMovie = {...req.body, id};
        movies.push(newMovie);
        res.send('Saved');
    } else{
        res.send('Data missing')
    }
    res.send('recived');
});

module.exports = router;