from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.username,
            'email': self.email,
        }
        return data

    def from_dict(self, data):
        for attr in ['name', 'email']:
            if attr in data:
                setattr(self, attr, data[attr])
        

    def __repr__(self):
        return '<User {}>'.format(self.username)  