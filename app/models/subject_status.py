from app.extensions import db


class SubjectStatus(db.Model):
    __tablename__ = 'subject_status'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<SubjectStatus {self.name}>'