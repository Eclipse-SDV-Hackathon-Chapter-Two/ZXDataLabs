db = connect( 'mongodb://localhost/myDatabase' );

db.car.insertOne({"userdata": 1, "message": "hell world"})
