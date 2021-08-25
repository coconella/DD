from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


# 방명록 불러오기 index_2.html
@app.route('/')
def home():
    return render_template('index_2.html')

## 방명록 API index_2.html
@app.route('/comment', methods=['POST'])
def comment():
    comment_receive = request.form['comment_give']
    doc = {'comment':comment_receive}
    db.comments.insert_one(doc)
    return jsonify({'msg': '방명록 작성 완료:)'})

@app.route('/comment', methods=['GET'])
def comment_show():
   comment=list(db.comments.find({},{'_id':False}))
   return jsonify({'all_comments':comment})

# 리뷰 불러오기 test.html
@app.route('/review')
def review():
    return render_template('test.html')

## 리뷰 API test.html
@app.route('/review', methods=['POST'])
def make_review():
    writer_receive = request.form['writer_give']
    title_receive = request.form['title_give']
    season_receive = request.form['season_give']
    where_receive = request.form['where_give']
    photo_receive = request.form['photo_give']
    review_receive = request.form['review_give']
    type_receive = request.form['type_give']
    doc = {'writer':writer_receive,'title':title_receive,'season':season_receive,'where':where_receive,'photo':photo_receive,'review':review_receive,'type':type_receive}
    db.travel_reviews.insert_one(doc)
    return jsonify({'msg': '여행 리뷰 작성 완료:)'})

@app.route('/review', methods=['GET'])
def show_review():
   travel_reviews=list(db.travel_reviews.find({},{'_id':False}))
   return jsonify({'all_reviews':travel_reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
