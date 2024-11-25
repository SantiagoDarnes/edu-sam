from app.extensions import db


class StudentProgram(db.Model):
    __tablename__ = 'student_program'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('academic_program.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<StudentProgram Student: {self.student_id}, Program: {self.program_id}>'
