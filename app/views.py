from flask import render_template, request, redirect, url_for, jsonify, abort
from app import app, models
from app import instructor_store, instructor_course_store
import base64
import datetime
import re
import os
import random
import shutil


@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route('/api/add/instructor', methods=['POST'])
def add_instructor():
    request_data = request.get_json()

    new_instructor = models.Instructor(esa_number=remove_letters(request_data[0]['esa_number']),
                                       system_id=request_data[0]['system_id'],
                                       name=request_data[0]['name'],
                                       certificate_date=string_to_date(request_data[0]['certificate_date'], 1900),
                                       tax_code=request_data[0]['tax_code'],
                                       sex=request_data[0]['sex'],
                                       date_of_birth=string_to_date(request_data[0]['date_of_birth'], 1900),
                                       place_of_birth=request_data[0]['place_of_birth'],
                                       nationality=request_data[0]['nationality'],
                                       home_phone=request_data[0]['home_phone'],
                                       cell_phone=request_data[0]['cell_phone'],
                                       email_address=request_data[0]['email_address'],
                                       annual_renewal=request_data[0]['annual_renewal'],
                                       annual_renewal_date=string_to_date(request_data[0]['annual_renewal_date'], 2000),
                                       prof_number=request_data[0]['prof_number'],
                                       first_annual_renewal=request_data[0]['first_annual_renewal'],
                                       first_annual_renewal_date=string_to_date(
                                           request_data[0]['first_annual_renewal_date'], 2000),
                                       fa_no=request_data[0]['fa_no'],
                                       country=request_data[0]['country'],
                                       state_name=request_data[0]['state_name'],
                                       city=request_data[0]['city'],
                                       street=request_data[0]['street'],
                                       teaching_status=request_data[0]['teaching_status'],
                                       esa_level=request_data[0]['esa_level'],
                                       esa_fa_level=request_data[0]['esa_fa_level'],
                                       fa_teaching_status=request_data[0]['fa_teaching_status'],
                                       person_type=request_data[0]['person_type'])

    existing_instructor = instructor_store.get_by_system_id(request_data[0]['system_id'])
    if existing_instructor:
        old_id = instructor_store.get_id_only(request_data[0]['system_id'])
        new_instructor.id = old_id

        instructor_store.update(new_instructor)

        save_pic(request_data[0]['photo'], str(request_data[0]['system_id']))
        instructor_course_store.delete_for_instructor(old_id)

        for i in request_data:
            course = models.InstructorCourse(course_name=i['course_name'],
                                             course_date=string_to_date(i['course_date'], 2000),
                                             instructor_id=old_id)
            instructor_course_store.add(course)

    else:
        instructor_store.add(new_instructor)
        for i in request_data:
            course = models.InstructorCourse(course_name=i['course_name'],
                                             course_date=string_to_date(i['course_date'], 2000),
                                             instructor_id=new_instructor.id)
            instructor_course_store.add(course)

        save_pic(request_data[0]['photo'], str(new_instructor.system_id))
    return jsonify(new_instructor.as_dict())


@app.route('/get/instructor', methods=['PUT'])
def get_instructor():
    request_data = request.get_json()
    instructor_name = request_data['name']
    date_of_birth = string_to_date_two(request_data['date_of_birth'])
    esa_number = request_data['esa_number']
    esa_number = remove_letters(esa_number)
    instructor = instructor_store.get_instructor(instructor_name, esa_number, date_of_birth)
    result = 0

    if instructor:
        # return jsonify(instructor.as_dict() + instructor.as_dict())
        result = instructor.system_id

    return jsonify({"result": result})


@app.route('/instructor/<string:system_id>')
def get_profile(system_id):
    instructor = instructor_store.get_by_system_id(system_id)

    if instructor:
        instructor_image = get_picture(instructor.system_id)
        other_data = 'Professional'
        if instructor.person_type == 'B':
            other_data = 'Recreational'

        courses = instructor_course_store.get_by_instructor(instructor.id)
        # to fix image caching
        random_image_code = random.randint(111111111,999999999)

        return render_template('instructor.html', instructor=instructor, picture=instructor_image,
                               other_data=other_data, courses=courses, image_code=random_image_code)
    else:
        return abort(404, f'Incorrect data!')


@app.route('/clear/cache')
def clear_cache():
    shutil.rmtree(f'app/static/instructor_images')
    os.mkdir(f'app/static/instructor_images')
    return jsonify({"result": True})


def save_pic(string_image, image_name):
    result = True
    if string_image == 'None':
        result = False
    else:
        image_data = base64.b64decode(string_image)
        with open(f'app/static/instructor_images/{image_name}.jpg', 'wb') as f:
            f.write(image_data)
    return result


def get_picture(instructor_id):
    image_found = os.path.isfile(f'app/static/instructor_images/{instructor_id}.jpg')
    result = f'../static/instructor_images/{instructor_id}.jpg'
    if not image_found:
        result = f'../static/img/empty-profile.jpg'
    return result


def string_to_date(date_string, additional_number):
    result = datetime.datetime(1900, 1, 1, 0, 0, 0)
    if date_string:
        date_list = date_string.split('-')
        year = date_list[2]
        month = date_list[1]
        day = date_list[0]
        result = datetime.datetime(int(year) + additional_number, int(month), int(day), 0, 0, 0)
    return result


def remove_letters(input_string):
    result = re.sub('[^0-9]', '', input_string)
    return result


def string_to_date_two(date_string):
    result = datetime.datetime(1900, 1, 1, 0, 0, 0)
    if date_string:
        try:
            date_list = date_string.split('-')
            year = date_list[0]
            month = date_list[1]
            day = date_list[2]
            result = datetime.datetime(int(year), int(month), int(day), 0, 0, 0)
        except ValueError:
            pass
    return result


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", message=error.description)
