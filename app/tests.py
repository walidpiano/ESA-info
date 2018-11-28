from app import models, stores, instructor_store
import string

stt = stores.InstructorStore()


#walid = models.Instructor(name='walid', system_id=10, esa_number='eso34')
#walid2 = models.Instructor(name='walid', system_id=11, esa_number='es343o34')

#stt.add(walid)
#stt.add(walid2)

#print(stt.get_all())

#instructor = stt.get_by_id(1)


#inst = stores.InstructorStore.get_id_only(10)
#print(stt.get_all())


#print(inst)
#course = stores.InstructorCourseStore()
#print(course.get_all())

#test = stores.InstructorStore()
#print(test.get_all())

#neww = test.get_with_courses(11)
#print(neww)

inst = stores.InstructorStore()
#inst.delete(2)


print(inst.get_all())
print(inst.get_by_system_id(22))

existing_instructor = instructor_store.get_by_system_id(22)

