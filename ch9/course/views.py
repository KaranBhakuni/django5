from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# def learn_django(req):
#     try:
#         # Try loading the template directly using the loader
#         template = loader.get_template('course/django.html')
#         return HttpResponse(template.render())
#     except Exception as e:
#         return HttpResponse(f"Error: {str(e)}")


# def learn_django(req):
#     try:
#         template = loader.get_template("course/django.html")
#         return HttpResponse(template.render())
#     except Exception as e:
#         return HttpResponse(f"Error: {str(e)}")


# variables in django

# type 1 how define variable 

# def learn_django(req):
#     return render(req,"course/django.html",context={'name':'django'})


# type 2 how define variable 
# def learn_django(req):
#     name='karan'
#     course='ml'
#     return render(req,"course/django.html",context={'name':name,'course_name':course})

# filter in django 

# def learn_django(req):
#     return render(req,"course/django.html",context={'name':'django'})


# datetime

# def learn_django(req):
#     d=datetime.now()
#     return render(req,"course/django.html",context={'dt':d})

# if tag 
# def learn_django(req):
#     d=10
#     var='hello world'
#     return render(req,"course/django.html",context={'dt':d,'word':var})

# for loop 
def learn_django(req):
    students = {'names': ['karan','deepak','alex','ramu']}
    return render(req,"course/django.html",context=students)


def learn_second(req):
    return HttpResponse('<p>hello from second function</p>')