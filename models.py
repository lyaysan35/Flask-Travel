import datetime
from peewee import *

DATABASE = SqliteDatabase('dogs.sqlite')

DEBUG = True 
PORT = 8000



class Place(Model):
    city = CharField()
    country = CharField()
    text = CharField()
    image = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta: #special constructor that give our class instructions
    # telling our model to connect to a specific db
        database = DATABASE




class User(Model):
   id = PrimaryKeyField(null=False)
   email = CharField()
   password = CharField()

   # def__repr__(self):
   # return '<User: {}, id: {}>'. format(self.email, self.id)


class Meta:	
	database = DATABASE 
# db_table = 'users'  




def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Place], safe=True)
    print("TABLES Created")
    DATABASE.close()












if __name__ == '__main__':
	models.initialize() #call f() that creates our table
	app.run(debug=DEBUG, port=PORT)