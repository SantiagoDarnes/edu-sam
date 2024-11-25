from app.extensions import db


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    enrollment_number = db.Column(db.String(50), unique=True, nullable=False) 
    admission_date = db.Column(db.Date, nullable=False)

    programs = db.relationship('AcademicProgram', secondary='student_program', backref='students')

    def __repr__(self):
        return f'<Student {self.enrollment_number}>'
