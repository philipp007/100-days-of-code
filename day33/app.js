#!/usr/bin/env node

'use strict';
var MongoClient = require('mongodb').MongoClient;
var url = 'mongodb://localhost/';

MongoClient.connect(url, function(err, db) {
  if (err) { 
      throw err;
  }

  var dbo = db.db("mydb");
  dbo.createCollection("customers", function(err, res) {
    if (err) throw err;
    console.log("Collection created!");    
  });

  const newCustomer = { name: "Dagny Taggart", company: "Taggart Transcontinental" };
  dbo.collection("customers").insertOne(newCustomer, (err, res) => {
      if (err) { 
        throw err;
      }

      console.log("Customer inserted!");
  })

  db.close();
});
