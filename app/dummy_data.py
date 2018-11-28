from app import models, db
from app import stores


dummy_instructors = [
    models.Instructor(name='walid', esa_number='es1'),
    models.Instructor(name='donna', esa_number='es2'),
    models.Instructor(name='samah', esa_number='es3'),
]

db.drop_all()
db.create_all()
test = stores.InstructorStore()
for i in dummy_instructors:
    test.add(i)


