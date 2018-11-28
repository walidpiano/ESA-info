from sqlalchemy.ext.declarative import declarative_base

from app import models, db
from sqlalchemy import or_


class BaseStore:

    def __init__(self, data_provider):
        self.data_provider = data_provider

    def get_all(self):
        return self.data_provider.query.all()

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def get_by_id(self, id):
        return self.data_provider.query.get(id)

    def update(self, entity, fields):
        result = self.data_provider.query.filter_by(id=entity.id).update(fields)
        db.session.commit()
        return result

    def delete(self, id):
        result = self.data_provider.query.filter_by(id=id).delete()
        db.session.commit()
        return result

    def entity_exists(self, entity):
        result = True
        if self.get_by_id(entity.system_id) is None:
            result = False

        return result


class InstructorStore(BaseStore):

    def __init__(self):
        super().__init__(models.Instructor)

    def get_by_name(self, instructor_name):
        return self.data_provider.query.filter_by(name=instructor_name).all()

    def get_by_system_id(self, system_id):
        # result = session.query(models.Instructor).filter_by(system_id=system_id).order_by(models.Instructor.person_type).first()
        result = self.data_provider.query.filter_by(system_id=system_id).order_by(
            self.data_provider.person_type).first()

        print(result)
        return result

    def get_id_only(self, system_id):
        # result = session.query(models.Instructor.id).filter_by(system_id=system_id).order_by(models.Instructor.person_type).one()
        result = self.data_provider.query.filter_by(system_id=system_id).order_by(self.data_provider.person_type).one()
        return result.id

    def get_with_courses(self, system_id):
        # result = session.query(models.Instructor).join(models.Instructor.courses).all()
        result = self.data_provider.query.join(self.data_provider.courses).all()
        return result

    def get_instructor(self, name, esa_number, date_of_birth):
        # result = session.query(models.Instructor).filter_by(date_of_birth=date_of_birth)\
        #    .filter(or_(esa_number==esa_number, name==name)).first()
        result = self.data_provider.query.filter_by(date_of_birth=date_of_birth) \
            .filter(or_(esa_number == esa_number, name == name)).order_by(self.data_provider.person_type).first()
        return result

    def update(self, entity):
        fields = {
            'esa_number': entity.esa_number,
            'name': entity.name,
            'certificate_date': entity.certificate_date,
            'tax_code': entity.tax_code,
            'sex': entity.sex,
            'date_of_birth': entity.date_of_birth,
            'place_of_birth': entity.place_of_birth,
            'nationality': entity.nationality,
            'home_phone': entity.home_phone,
            'cell_phone': entity.cell_phone,
            'email_address': entity.email_address,
            'annual_renewal': entity.annual_renewal,
            'annual_renewal_date': entity.annual_renewal_date,
            'prof_number': entity.prof_number,
            'first_annual_renewal': entity.first_annual_renewal,
            'first_annual_renewal_date': entity.first_annual_renewal_date,
            'fa_no': entity.fa_no,
            'country': entity.country,
            'state_name': entity.state_name,
            'city': entity.city,
            'street': entity.street,
            'teaching_status': entity.teaching_status,
            'esa_level': entity.esa_level,
            'esa_fa_level': entity.esa_fa_level,
            'fa_teaching_status': entity.fa_teaching_status,
            'person_type': entity.person_type
        }
        return super().update(entity, fields)


class InstructorCourseStore(BaseStore):

    def __init__(self):
        super().__init__(models.InstructorCourse)

    def delete_for_instructor(self, instructor_id):
        result = self.data_provider.query.filter_by(instructor_id=instructor_id).delete()
        db.session.commit()
        return result

    def get_by_instructor(self, instructor_id):
        # result = session.query(models.InstructorCourse).filter_by(instructor_id=instructor_id).all()
        result = self.data_provider.query.filter_by(instructor_id=instructor_id).all()
        return result
