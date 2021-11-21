from pymongo import MongoClient

#mongoDB에 저장하기
client = MongoClient('localhost', 27017) #mongoDB는 27017포트로
db = client.dbtest #'dbsparta'라는 이름의 db를 만듭니다.

#MongoDB에 insert하기

#'users'라는 collection에 데이터 넣기
#db.users.insert_one({'name':'bobby','age':21})
#db.users.insert_one({'name':'key','age':27})
#db.users.insert_one({'name':'john','age':30})

#MongoDB에서 데이터 보기
all_users = list(db.users.find())

same_ages = list(db.users.find({'age': 21}))

print(all_users[0])
print(all_users[0]['name'])

for user in all_users:
    print(user)

#특정 결과 값을 뽑아 보기
user = db.users.find_one({'name':'bobby'})
print(user)

