from app.extensions import db


class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name
    
    @staticmethod
    def get_default_profile(user_id):
        return Profile.query.filter_by(name='default').first()
