from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(150), unique=True)
    role = db.Column(db.String(10))


    def __repr__(self):
        return '<User %r>' % self.username
