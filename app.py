from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# In the URI. specify your username, your password, your port and your database name.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:5724/database_name'
db = SQLAlchemy(app) 

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, server_default=text('NOW()'))

    def __repr__(self):
        return '<Message %r>' % self.content

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('likes', lazy=True))

    def __repr__(self):
        return '<Like for message %r>' % self.message_id

#This code creates routes for a web application that allow users to post messages, like messages, and view the number of likes for a message.
@app.route('/messages', methods=['POST'])
def create_message():
    content = request.json['content']
    message = Message(content=content)
    db.session.add(message)
    db.session.commit()
    return jsonify(message='Message created successfully'), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.created_at.desc()).all()
    return jsonify([message.content for message in messages]), 200

@app.route('/messages/<int:message_id>/like', methods=['POST'])
def like_message(message_id):
    like = Like(message_id=message_id)
    db.session.add(like)
    db.session.commit()
    return jsonify(message='Message liked successfully'), 201

@app.route('/messages/<int:message_id>/like', methods=['DELETE'])
def unlike_message(message_id):
    like = Like.query.filter_by(message_id=message_id).first()
    db.session.delete(like)
    db.session.commit()
    return jsonify(message='Message unliked successfully'), 200

@app.route('/messages/<int:message_id>/likes', methods=['GET'])
def get_likes(message_id):
    count = db.session.query(Like).filter_by(message_id=message_id).count()
    return jsonify(likes=count), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)