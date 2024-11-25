from app.extensions import db


class ProfessorSubject(db.Model):
    __tablename__ = 'professor_subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

    def __repr__(self):
        return f'<ProfessorSubject Professor: {self.professor_id}, Subject: {self.subject_id}>'


