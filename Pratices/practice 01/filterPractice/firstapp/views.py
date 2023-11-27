from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    courses = [
        {'id': 1, 'name': 'Python', 'fee': 5000},
        {'id': 2, 'name': 'Django', 'fee': 10000},
        {'id': 3, 'name': 'C', 'fee': 1000},
    ]

    # Add 2 to each fee
    for course in courses:
        course['fee'] += 2

    context = {'author': "Capt'n Jack",
               'name':'niloy', 
               'age': 5,
               'colors': ['Red', None, 'Blue', '', 'Yellow'], 
               'courses': courses,
               'birthday' : datetime.datetime.now(),
               'cars': 
               [
                        {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
                        {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
                        {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
                        {'brand': 'Ford', 'model': 'Focus', 'year': 2004},
                ],
                'heading': 'Hello &lt;i>my&lt;/i> World!',
                'size': 26214400,
                'fruits': ['Apple', 'Banana', 'Cherry', 'Orange'],
                'mynumber': 7.122489,
                'mytext': 'Hello\nmy name is Leo.\n\nI am a student.',   
                'text': 'Hi, my name is Linus',  
                'mybirthdate': datetime.datetime(2004, 11, 18),   
                'mydate': datetime.datetime(2020, 5, 17),   
                'arr': [0, 1, 2] 
               }
    return render(request, 'firstapp/home.html', context)