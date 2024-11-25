from app.extensions import db


class AcademicPeriod(db.Model):
    __tablename__ = 'academic_period'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True) 
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False) 
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    inscription_start_date = db.Column(db.Date, nullable=False)
    inscription_end_date = db.Column(db.Date, nullable=False)
    final_exams_start_date = db.Column(db.Date, nullable=False)
    final_exams_end_date = db.Column(db.Date, nullable=False)
    final_exams_inscription_start_date = db.Column(db.Date, nullable=False)
    final_exams_inscription_end_date = db.Column(db.Date, nullable=False)  
    is_active = db.Column(db.Boolean, default=False, nullable=False) 

    subjects = db.relationship('Subject', backref='academic_period', lazy=True)

    def __repr__(self):
        return f'<AcademicPeriod {self.name}, Semester: {self.dim_semester.name}>'

    @staticmethod
    def validate_dates(start_date, end_date):
        if start_date >= end_date:
            raise ValueError("The start_date must be earlier than the end_date.")
