from app.extensions import db


class StudentFinalExam(db.Model):
    __tablename__ = 'student_final_exam'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)  
    final_exam_id = db.Column(db.Integer, db.ForeignKey('final_exam.id'), nullable=False) 
    grade = db.Column(db.Float)
    attendance = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)


    student = db.relationship('Student', backref='final_exam_records')
    final_exam = db.relationship('FinalExam', backref='student_records')

    def __repr__(self):
        return f'<StudentFinalExam Student: {self.student_id}, FinalExam: {self.final_exam_id}>'
    
    @staticmethod
    def register(student_id: int, final_exam_id: int, grade: float=0.0):
        student_exam = StudentFinalExam(
            student_id=student_id,
            final_exam_id=final_exam_id,
            grade=grade
        )
        db.session.add(student_exam)
        db.session.commit()
        
    
