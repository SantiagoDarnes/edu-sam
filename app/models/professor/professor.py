from app.extensions import db


class Professor(db.Model):
    __tablename__ = 'professor'

    # Identificación
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    professor_code = db.Column(db.String(50), unique=True, nullable=False)

    careers = db.relationship('ProfessorCareer', backref='professor')
    subjects = db.relationship('ProfessorSubject', backref='professor')

    def __repr__(self):
        return f'<Professor {self.professor_code}>'