const { Router } = require('express'); 
const router = Router();

//Routes
router.get('/test', (req, res) => {
    const data= {
        "name": "Mau",
        "website": "mau.com"
    };
    res.json(data);
});

module.exports = router;