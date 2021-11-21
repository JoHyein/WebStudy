from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbtest

doc = {'name':'selly', 'age':'30'}
db.users.insert_one(doc)
print()

user = db.users.find_one({'name' : 'selly'})
print(user)
print()

same_ages = list(db.users.find({'age':30},{'_id':False}))
print(same_ages)
print()

db.users.update_one({'name':'selly'}, {'$set':{'age':19}})

db.users.delete_one({'name':'bobby'})

all_users = list(db.users.find())

for user in all_users:
    print(user)