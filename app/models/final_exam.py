from app.extensions import db


class FinalExam(db.Model):
    __tablename__ = 'final_exam'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    subject = db.relationship('Subject', backref='final_exams')

    def __repr__(self):
        return f'<FinalExam {self.id}>'