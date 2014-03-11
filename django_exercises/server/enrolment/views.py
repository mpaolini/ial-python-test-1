from django.shortcuts import render
from enrolment.models import student
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def home(request):
    if request.method == 'POST':
        body = request.body
        content = json.loads(body)
        stud = student(name = content['name'], surname = content['surname'])
        stud.save()
        return HttpResponse(status = 200)
    elif request.method == 'GET':
        stud = student.objects.all()
        student_list = [{'name': x.name,'surname': x.surname} for x in stud]
        resp = json.dumps(student_list)
        return HttpResponse(resp, content_type='application/json')