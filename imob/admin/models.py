from imob import db

class User(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(180),unique=True, nullable=False)
    password = db.Column(db.String(180),unique=True, nullable=False)
 
    def __init__(self, name, username,  email, password):
        self.name = name
        self.username = username
        
        self.email= email
        self.password= password

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()