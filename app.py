
# imports 
from flask import Flask, request, make_response,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy 

# initializing Flask app 
app = Flask(__name__) 

# Google Cloud SQL (change this accordingly) 
PASSWORD ="athenahacks"
PUBLIC_IP_ADDRESS ="34.66.173.134"
DBNAME ="testing"
PROJECT_ID ="prime-amulet-306817 "
INSTANCE_NAME ="athenahacks "

# configuration 
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

db = SQLAlchemy(app) 

# User ORM for SQLAlchemy 
class Userinfo(db.Model): 
    id = db.Column(db.Integer, primary_key = True, nullable = False)    
    username = db.Column(db.String(50), nullable = False, unique = True) 
    pwd = db.Column(db.String(50), nullable = False) 
    age = db.Column(db.String(50), nullable = False) 

@app.route('/', methods =['GET']) 
def home(): 
    return app.send_static_file('about.html')
    # return render_template('index.html')

@app.route('/add', methods =['POST'])
def add(): 
    # geting name and email 
    print("add called")
    pwd = request.args.get('pwd') 
    age = request.args.get('age') 
    username = request.args.get('username') 
    print(pwd)
    print(age)
    print(username)
    print(request.args)
    # name = request.args.get("name")
    # email = request.args.get("email")

    # checking if user already exists 
    user = Userinfo.query.filter_by(username = username).first() 
    responseObject = dict()
    if not user: 
        try: 
            # creating Userinfo object 
            user = Userinfo( 
                pwd = pwd, 
                username = username,
                age = age
            ) 
            # adding the fields to Userinfo table 
            db.session.add(user) 
            db.session.commit() 
            # response 
            responseObject = { 
                'status' : 'success', 
                'message': 'Sucessfully registered.'
                # 'code' : 200
            } 
        except: 
            responseObject = { 
                'status' : 'fail', 
                'message': 'Some error occured !!'
                # 'code' : 400
            } 
    else: 
        # if user already exists then send status as fail 
        responseObject = { 
            'status' : 'fail', 
            'message': 'User already exists !!'
            # 'code' : 403
        } 

    return jsonify(responseObject)

@app.route('/view') 
def view(): 
    # fetches all the Userinfo 
    Users = Userinfo.query.all() 
    # response list consisting user details 
    response = list() 
    print(Userinfo)

    for user in Users: 
        response.append({ 
            "name" : user.username, 
            "pwd": user.pwd,
            "age" : user.age 
        }) 

    return make_response({ 
        'status' : 'success', 
        'message': response 
    }, 200) 

@app.route('/confirmlogin', methods =['GET']) 
def confirmlogin(): 
    # fetches all the Userinfo 
    name = request.args.get("name")
    pwd = request.args.get("pwd")

    Users = Userinfo.query.all() 
    # response list consisting user details 
    response = list() 
    print(Users)

    response = dict()

    for user in Users: 
        # print(user.name)
        # print(user.email)
        if user.username == name and user.pwd == pwd:
            response["status"] = 'success'
    if "status" not in response.keys():
        response["status"] = 'fail'

    print(response)
    return jsonify(response)

if __name__ == "__main__": 
    # serving the app directly 
    app.run() 
