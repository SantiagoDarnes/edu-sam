from app.extensions import db


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    enrollment_number = db.Column(db.String(50), unique=True, nullable=False) 
    admission_date = db.Column(db.Date, nullable=False)

    careers = db.relationship('StudentCareer', backref='student')
    subjects = db.relationship('StudentSubject', backref='student')

    def __repr__(self):
        return f'<Student {self.enrollment_number}>'
    
    def set_enrollment_number(self):
        last_student = Student.query.order_by(Student.id.desc()).first()
        if last_student:
            self.enrollment_number = str(last_student.enrollment_number + 1)
        else:
            self.enrollment_number = '1'
    
    