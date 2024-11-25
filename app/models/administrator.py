from app.extensions import db


class Administrator(db.Model):
    __tablename__ = 'administrator'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    access_level_id = db.Column(db.Integer, db.ForeignKey('access_level.id'), nullable=False)

    access_level = db.relationship('AccessLevel', backref='administrators')

    def __repr__(self):
        return f'<Administrator Position: {self.position}, Access Level: {self.access_level.level}>'
