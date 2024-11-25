from app.extensions import db


class Semester(db.Model):
    __tablename__ = 'semester'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # Relación con semester_schedule
    academic_period = db.relationship('AcademicPeriod', backref='semester', lazy=True)

    def __repr__(self):
        return f'<Semester {self.name}>'
