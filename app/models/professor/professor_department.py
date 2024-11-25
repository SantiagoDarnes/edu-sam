from app.extensions import db


class ProfessorDepartment(db.Model):
    __tablename__ = 'professor_department'

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

    def __repr__(self):
        return f'<ProfessorDepartment Professor: {self.professor_id}, Department: {self.department_id}>'
