from app.extensions import db


class ProfessorCareer(db.Model):
    __tablename__ = 'professor_career'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    career_id = db.Column(db.Integer, db.ForeignKey('career.id'), nullable=False)

    def __repr__(self):
        return f'<ProfessorCareer Professor: {self.professor_id}, Career: {self.career_id}>'
