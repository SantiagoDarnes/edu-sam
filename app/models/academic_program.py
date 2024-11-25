from app.extensions import db


class AcademicProgram(db.Model):
    __tablename__ = 'academic_program'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False) 
    name = db.Column(db.String(100), unique=True, nullable=False)  

    department = db.Column(db.String(100)) 
    duration_years = db.Column(db.Integer) 

    def __repr__(self):
        return f'<AcademicProgram {self.name}>'
