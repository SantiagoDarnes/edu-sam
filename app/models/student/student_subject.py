from app.extensions import db


class StudentSubject(db.Model):
    __tablename__ = 'student_subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False) 

    def __repr__(self):
        return f'<StudentSubject Student: {self.student_id}, Subject: {self.subject_id}>'
