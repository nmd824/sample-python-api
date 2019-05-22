#Customer Data Model
I've created a SQL file to create this table as well as some sample data in the folder "Customer Data Model".

The SQL query to names of the youngest customers is also in the "Customer Data Model" folder.

#Basic JSON API App
In order to run, there has to be a database called "gigacover" and a table called "customers". 

I'm using gunicorn as the Web Server Gateway Interface. 

To run, please execute the following command:
gunicorn sample-python-api:api

As I was not really experienced with RESTful API, I refered to this tutorial on Youtube: https://www.youtube.com/watch?v=W6JvboT8Uo8

Postgresql tutorial from: http://www.postgresqltutorial.com/postgresql-python/

For the POST, PUT, and DELETE methods, I put the JSON data in the Body section of the Postman app and work with the JSON data from there.

The JSON data is in the following format:
{
   "name": "flask",
   "dob": "2017-01-09",
   "updated_at": "2019-05-22 19:23:24"
}

As it was a simple implementation, I did not perform any error handlings. Also, since the ID is auto increment, I thought it made more sense for all queries to be based on names (i.e. where name = ...)

Honestly, I'm not really sure if what I did is correct but it seems to be working from what I can tell.

#Postman collection

Postman collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/c5514f4b5ad06a957147)