# python school_client.py --name Elia --surname Sgolmin

import requests
import json
import argparse

HOST = 'localhost:8000'

def enroll_student(name, surname):
    resp =requests.post('http://{}/home'.format(HOST), json.dumps({'name': name, 'surname': surname}))
    if resp.status_code == 200:
        print 'OK'
    else:
        print 'ERROR'

def search_student(student):
    resp = requests.get('http://{}/home'.format(HOST))
    content = json.loads(resp.content)
    for student_x in content:
        if(student_x['name'] == student or student_x['surname'] == student):
            print student_x['name'] + " " + student_x['surname']

parser = argparse.ArgumentParser('student client')
parser.add_argument('command')
parser.add_argument('--name')
parser.add_argument('--surname')
parser.add_argument('--student')
args = parser.parse_args()

if args.command == 'enroll':
    enroll_student(args.name, args.surname)
elif args.command == 'search':
    search_student(args.student)
else:
    print 'ERROR'