
import pymongo

def connect_db():
	#Connecting to the mongodb server
	client =   pymongo.MongoClient('mongodb://127.0.0.1:27017/')
	return client

def insert_data(data):

	record = {
				'square_feet':data[0],
				'bed':data[1],
				'bathroom':data[2],
				'cats':data[3],
				'dogs':data[4],
				'smoking':data[5],
				'wheelchair':data[6],
				'electric':data[7],
				'furnished':data[8],
				'latitude':data[9],
				'longitude':data[10],
				'region':data[11],
				'state':data[12],
				'house_type':data[13],
				'laundry':data[14],
				'parking':data[15]
				
			}

	client = connect_db()
	client['house_rent']['user_input'].insert_one(record)

