
var path = require('path');
var fs = require('fs');
var express = require('express');

var router = express.Router();

// Basic object demo
router.get('/py-1', function(req, res) {
  res.render('py-1');
}); 

// Challenge escape
router.get('/ch-1', function(req, res) {
  res.render('ch-1');
}); 

// Challenge escape with code
router.get('/ch-2', function(req, res) {
  res.render('ch-2');
}); 

// Object creation
router.get('/py-2', function(req, res) {
  res.render('py-2');
}); 

// Challenge : create a 1d array for row 3
router.get('/ch-3', function(req, res) {
  res.render('ch-3');
}); 




module.exports = router;

