import jwt

from flask import Flask, jsonify, request
from database import db, ma, mail
from models.members import Members, members_schema
from config.config import BaseConfig
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(BaseConfig())
db.init_app(app)
ma.init_app(app)
mail.init_app(app)

@app.route('/')
def index():
    MembersModel = Members.query.all()
    members = members_schema.dumps(MembersModel)
    return members

@app.route('/register', methods=['POST'])
def register():

    responseMessage = "OK"
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    member = {
        'username': username,
        'email': email,
        'password': password
    }
    membersModel = Members()
    registered = membersModel.create(member)

    if registered == False:
        responseMessage = "None"
    return responseMessage

@app.route('/update_member', methods=['PUT'])
def updateMember():
    responseMessage = "OK"

    memberID = request.form["member_id"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    member = {
        'id': memberID,
        'username': username,
        'email': email,
        'password': password
    }

    membersModel = Members()
    updated = membersModel.update(member)
    if updated == False:
        responseMessage = "None"
    return responseMessage

@app.route('/delete_member', methods=['DELETE'])
def deleteMember():
    memberID = request.form["member_id"]
    responseMessage = Members().delete(memberID)

    if responseMessage is not False:
        return "OK"
    else:
        return "Failed."

@app.route('/test_jwt')
def jwt():
    data = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": 1516239022
    }

    token = jwt.encode(data, 'secret', algorithm='HS256')
    return token.decode()

@app.route('/test_request', methods=['POST'])
def test_request():
    user = request.form["nm"]
    return user

@app.route('/test_json', methods=['GET'])
def test_json():
    response = jsonify({'msg': 'welcome'})
    return response

@app.route("/mail")
def send_mail():
    config = BaseConfig()
    msg = Message("Hello", recipients=[config.MAIL_TEST_RECIPIENTS])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)

    return 'You Send Mail by Flask Mail Success!!'

if __name__ == '__main__':
    app.run(debug=True)