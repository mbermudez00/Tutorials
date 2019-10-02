/*
import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';

import './global.css';
import App from './components/App';

const container = document.getElementById('app');

ReactDOM.render(<App />, container);
*/

const express = require('express');
const app = express();
const morgan = require('morgan');

//middleawers
app.use(morgan('dev'));
app.use(express.json());
//app.use(morgan('dev'));

//settings


//starting the server
app.listen(3000, () => {
    console.log('server on port: ${3000}');
});