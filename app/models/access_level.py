from app.extensions import db


class AccessLevel(db.Model):
    __tablename__ = 'access_level'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50)) 
    level = db.Column(db.Integer, unique=True, nullable=False)  

    def __repr__(self):
        return f'<AccessLevel Level: {self.level}, Description: {self.description}>'
