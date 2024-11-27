from app.extensions import db
from app.models.career import Career


class StudentCareer(db.Model):
    __tablename__ = 'student_career'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    career_id = db.Column(db.Integer, db.ForeignKey('career.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return db.session.query(Career).filter_by(id=self.career_id).first().name
