from app.extensions import db


class Career(db.Model):
    __tablename__ = 'career'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)  
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    subjects = db.relationship('Subject', backref='career', lazy=True)

    def __repr__(self):
        return f'<Career {self.name}, Department: {self.department.name}>'
