from app import db


class Instructor(db.Model):
    __tablename__ = "instructor"

    id = db.Column(db.Integer, primary_key=True)
    system_id = db.Column(db.String(10))
    esa_number = db.Column(db.String, nullable=False)
    name = db.Column(db.String(200))

    certificate_date = db.Column(db.DateTime)
    tax_code = db.Column(db.String(50))
    sex = db.Column(db.String(10))
    date_of_birth = db.Column(db.DateTime)
    place_of_birth = db.Column(db.String(100))
    nationality = db.Column(db.String(80))
    home_phone = db.Column(db.String(20))
    cell_phone = db.Column(db.String(20))
    email_address = db.Column(db.String(150))
    annual_renewal = db.Column(db.String(3))
    annual_renewal_date = db.Column(db.DateTime)
    prof_number = db.Column(db.String(15))
    first_annual_renewal = db.Column(db.String(3))
    first_annual_renewal_date = db.Column(db.DateTime)
    fa_no = db.Column(db.String(15))
    country = db.Column(db.String(80))
    state_name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(250))
    teaching_status = db.Column(db.String(10))
    esa_level = db.Column(db.String(100))
    esa_fa_level = db.Column(db.String(100))
    fa_teaching_status = db.Column(db.String(10))
    person_type = db.Column(db.String(1))
    courses = db.relationship("InstructorCourse", backref="courses")

    def __repr__(self):
        return f"Id: {self.id}, Name: {self.name}, birth: {self.date_of_birth}, esa_number: {self.esa_number}, system_id: {self.system_id}"

    def as_dict(self):
        return {
            'id': self.id,
            'system_id': self.system_id,
            'esa_number': self.esa_number,
            'name': self.name,
            'certificate_date': self.certificate_date,
            'tax_code': self.tax_code,
            'sex': self.sex,
            'date_of_birth': self.date_of_birth,
            'place_of_birth': self.place_of_birth,
            'nationality': self.nationality,
            'home_phone': self.home_phone,
            'cell_phone': self.cell_phone,
            'email_address': self.email_address,
            'annual_renewal': self.annual_renewal,
            'annual_renewal_date': self.annual_renewal_date,
            'prof_number': self.prof_number,
            'first_annual_renewal': self.first_annual_renewal,
            'first_annual_renewal_date': self.first_annual_renewal_date,
            'fa_no': self.fa_no,
            'country': self.country,
            'state_name': self.state_name,
            'city': self.city,
            'street': self.street,
            'teaching_status': self.teaching_status,
            'esa_level': self.esa_level,
            'esa_fa_level': self.esa_fa_level,
            'fa_teaching_status': self.fa_teaching_status,
            'person_type': self.person_type,
        }


class InstructorCourse(db.Model):
    __tablename__ = 'instructor_course'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(200))
    course_date = db.Column(db.DateTime)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    instructor = db.relationship(Instructor)

    def as_dict(self):
        return {
            'id': self.id,
            'course_name': self.course_name,
            'course_date': self.course_date,
        }


db.drop_all()
db.create_all()
