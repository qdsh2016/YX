var express=require('express');
var swig=require('swig');

var app=express();
app.set('view engine','html');
app.engine('html',swig.renderFile);


app.get('/a',function(req,res ){
	//res.send('soga')
	var x=req; 
	res.render('a',{a:'okk'});
});


var server=app.listen(3000,function(){ 
	console.log('app is listening');
	console.log('---MVC---controller+model[jdbc..]+view[jade..]----');
});



// var mysql = require('mysql');
// var connection = mysql.createConnection({
//   host     : 'localhost',
//   user     : 'root',
//   password : '3306'
// });

// connection.connect();

// connection.query('show databases', function(err, rows, fields) {
//   if (err) throw err;
//   console.log(rows);
// });