from app.extensions import db


class Subject(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False) 
    career_id = db.Column(db.Integer, db.ForeignKey('career.id'), nullable=False)
    academic_period_id = db.Column(db.Integer, db.ForeignKey('academic_period.id'), nullable=False)
    min_passing_grade = db.Column(db.Float, nullable=False)
    min_promotion_grade = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    students = db.relationship('StudentSubject', backref='subject')
    professors = db.relationship('ProfessorSubject', backref='subject')

    def __repr__(self):
        return f'<Subject {self.name}, Career: {self.career.name}>'
