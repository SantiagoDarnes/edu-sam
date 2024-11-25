from app.extensions import db


class StudentSubject(db.Model):
    __tablename__ = 'student_subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)
    first_partial_grade = db.Column(db.Float,)
    second_partial_grade = db.Column(db.Float)
    status = db.Column(db.Integer, db.ForeignKey('subject_status.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    def __repr__(self):
        return f'<StudentSubject Student: {self.student_id}, Subject: {self.subject_id}>'
