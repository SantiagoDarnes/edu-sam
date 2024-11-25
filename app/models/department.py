from app.extensions import db


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    careers = db.relationship('Career', backref='department', lazy=True)

    def __repr__(self):
        return f'<Department {self.name}>'
