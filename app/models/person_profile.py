from app.extensions import db


class PersonProfile(db.Model):
    __tablename__ = 'person_profile'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)

    person = db.relationship('Person', backref='person_profiles')
    profile = db.relationship('Profile', backref='person_profiles')

    def __repr__(self):
        return self.profile
