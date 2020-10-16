import pymongo

#Connecting to the mongodb server
client =   pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#creating database name house_rent
mydb = client['house_rent']

#Creating a  collection in db (collection is like tables in sql)
# information = mydb.user_input
information = mydb['user_input']