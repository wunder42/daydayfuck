from models import DyCourse

def course_list_proc(request):
    course_list = DyCourse.objects.order_by("id")
    for course in course_list:
        course.course_class = course.dycourseclass_set.all()
    return {'course_list': course_list}