from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbreview                      

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    #클라이언트 측 데이터 가져오기
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    #DB에 삽입할 review 데이터 생성
    review = {
        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive
    }

    db.reviews.insert_one(review)
    return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 작성됐습니다.'})

@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({}, {'_id':0}))
    return jsonify({'result':'success', 'reviews':reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)